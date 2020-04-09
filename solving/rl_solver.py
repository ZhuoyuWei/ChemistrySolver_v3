import numpy as np
import collections

from .solver_utils import Solver
from model.graph import Graph
from model.edge import Edge
from model.node import Node






class RLSolver(Solver):

    def __init__(self,graph,func_list):
        super(RLSolver, self).__init__()
        self.action_spaces=None
        self.state_spaces=None
        self.reward=None

        self.estimator_policy=None

        self.graph=graph
        self.func_list=func_list
        self.func_indexed_by_return_type={}


    def training(self):
        pass


    def _convert_graph_to_state(self,graph):
        pass

    def step(self,action):
        next_state=None
        reward=None
        done=False
        _=None
        return next_state, reward, done, _

    def solving(self,target_edge):
        done=False
        t=0
        episode=[]
        Transition = collections.namedtuple("Transition", ["state", "action", "reward", "next_state", "done"])
        while not done:
            state=self._convert_graph_to_state(self.graph)
            #trans_prods=self._policy_estimating(state)
            action_probs = self.estimator_policy.predict(state)
            action = np.random.choice(np.arange(len(action_probs)), p=action_probs)
            next_state, reward, done, _ = self.step(action)


            # Keep track of the transition
            episode.append(Transition(
                state=state, action=action, reward=reward, next_state=next_state, done=done))

            if done:
                break

            state = next_state