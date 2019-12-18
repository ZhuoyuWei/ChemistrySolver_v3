import requests
import json

from parse.parse_utils import (generate_edges_from_question_variables,
                                generate_edges_from_conditions)
from model.graph import Graph
from solving.dfs_solver import DFSSolver


if __name__ == '__main__':
    question="How many moles of sodium carbonate are present in 6.80 grams of sodium carbonate?"
    #call http://10.177.74.166:36521/parse?q="" to obtain the parser result
    parsed_question = requests.get(url='http://10.177.74.166:36521/parse', params={'q': question}).json()
    print(parsed_question)



    question_varible_edges=generate_edges_from_question_variables(parsed_question['question_variable'])
    print("question_varible_edges[0], edge")
    print(question_varible_edges[0].predicate)
    print(question_varible_edges[0].in_node.name)
    print(question_varible_edges[0].out_node.unit)
    exit(-1)
    conditions_edges=generate_edges_from_conditions(parsed_question['conditions'])

    graph=Graph.build_graph_from_edges(question_varible_edges+conditions_edges)
    solver=DFSSolver()
    for question_edge in question_varible_edges:
        solver.solving(question_edge)
        #check solving result:

