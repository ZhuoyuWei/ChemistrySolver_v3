import requests
import json

from parse.parse_utils import (generate_edges_from_question_variables,
                                generate_edges_from_conditions)
from model.graph import Graph
from solving.dfs_solver import DFSSolver
from func.chemistry_func import (Func_Name2CE, Func_Mole2Atom,Func_CE2MolarMass,Func_Mass2Mole)


if __name__ == '__main__':
    question="How many moles of sodium carbonate are present in 6.80 grams of sodium carbonate?"
    #call http://10.177.74.166:36521/parse?q="" to obtain the parser result
    parsed_question = requests.get(url='http://10.177.74.166:36521/parse', params={'q': question}).json()
    print(parsed_question)



    question_varible_edges=generate_edges_from_question_variables(parsed_question['question_variable'])
    conditions_edges = generate_edges_from_conditions(parsed_question['conditions'])

    '''
    #debug parser info
    print("question_varible_edges[0], edge")
    print(question_varible_edges[0].predicate)
    print(question_varible_edges[0].in_node.name)
    print(question_varible_edges[0].out_node.unit)
    for i,condition_edge in enumerate(conditions_edges):
        print('condition {}'.format(i))
        print(condition_edge.predicate)
        print(condition_edge.in_node.name)
        print("{}\t{}".format(condition_edge.out_node.value,condition_edge.out_node.unit))
    '''

    graph=Graph.build_graph_from_edges(question_varible_edges+conditions_edges)
    graph.print_all_edges()
    graph.add_name_into_edges_for_all_node()
    graph.print_all_edges()
    func_list=[Func_Name2CE, Func_Mole2Atom,Func_CE2MolarMass,Func_Mass2Mole]
    solver=DFSSolver(graph,func_list)
    for question_edge in question_varible_edges:
        solved_flag=solver.solving(question_edge)
        #check solving result:
        if solved_flag:
            print('Final Result: {} {}'.format(question_edge.out_node.value,question_edge.out_node.unit))
        else:
            print('unsolved')

