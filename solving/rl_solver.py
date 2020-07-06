import numpy as np
import collections

from .solver_utils import Solver
from .rl_util import (Exec_Function_Action,
                      Merge_Nodes_Action,
                      Split_Node_Action,
                      Remove_Fact_Action,
                      Extract_Fact_Action,
                      Infer_Fact_Action,
                      Estimator_Policy_Fix,
                      correct_answer_reward)

from domain.chemistry_utils import PU,CE

from model.graph import Graph
from model.edge import Edge
from model.node import Node




class RLSolver(Solver):

    def __init__(self,graph,func_list,max_steps=10):
        super(RLSolver, self).__init__()
        self.action_spaces=None
        self.state_spaces=None
        self.reward_func=correct_answer_reward

        self.estimator_policy=Estimator_Policy_Fix(self.action_spaces,func_list)

        self.graph=graph
        self.func_list=func_list
        self.func_indexed_by_return_type={}

        self.max_steps=max_steps
        self.cur_steps=0


    def training(self):
        pass


    def _convert_graph_to_state(self,graph):
        return graph

    def step(self,action,target_edge,correct_answer=None):
        action.applying()
        next_state=self._convert_graph_to_state(self.graph)
        reward = self.reward_func(target_edge.out_node,correct_answer)
        if target_edge.out_node is None \
                or (type(target_edge.out_node) is PU and target_edge.out_node.value is None):
            done=False
        else:
            done=True

        self.cur_step+=1
        if self.cur_step >= self.max_steps:
            done=True

        _=None

        return next_state, reward, done, _

    def _solving(self,target_edge,correct_answer=None):
        done = False
        episode = []
        Transition = collections.namedtuple("Transition", ["state", "action", "reward", "next_state", "done"])
        while not done:
            if state is None:
                state = self._convert_graph_to_state(self.graph)
            # trans_prods=self._policy_estimating(state)
            action_probs = self.estimator_policy.predict(state)
            action_type = np.random.choice(np.arange(len(self.action_spaces)), p=action_probs)
            action=action_type(state=state,
                               text=None,
                               graph=self.graph,
                               function_list=self.func_list)
            next_state, reward, done, _ = self.step(action,target_edge=target_edge,correct_answer=correct_answer)

            # Keep track of the transition
            episode.append(Transition(
                state=state, action=action, reward=reward, next_state=next_state, done=done))

            if done:
                break

            state = next_state

        if target_edge.out_node is None \
                or (type(target_edge.out_node) is PU and target_edge.out_node.value is None):
            flag=False
        else:
            flag=True

        return flag,episode


    def solving(self,target_edge):
        self._solving(target_edge)