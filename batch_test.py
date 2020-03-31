'''
From questions text to results, including logging intermediante result
'''

import json
import sys

from parse.parse_utils import (generate_edges_from_question_variables,
                                generate_edges_from_conditions)
from model.graph import Graph
from solving.dfs_solver import DFSSolver
from func import CHEMISTRY_FUNC_LIST
from domain.chemistry_utils import PU,ChemicalEquation

def solve_one_question(parsed_question,fdebug):

    print(parsed_question)
    question_varible_edges=generate_edges_from_question_variables(parsed_question['question_variable'])

    print('DEBUG question varible: {}'.format(question_varible_edges))
    conditions_edges = generate_edges_from_conditions(parsed_question['conditions'])
    print('DEBUG conditions: {}'.format(conditions_edges))
    if question_varible_edges is None or conditions_edges is None:
        return None

    graph=Graph.build_graph_from_edges(question_varible_edges+conditions_edges)
    graph.print_all_edges()
    graph.add_name_into_edges_for_all_node()
    graph.print_all_edges()
    func_list=CHEMISTRY_FUNC_LIST

    #print(len(func_list))
    solver=DFSSolver(graph,func_list,max_depth=4)
    #print(solver.func_indexed_by_return_type)
    #exit(-1)
    predicted=None
    for question_edge in question_varible_edges:
        debug_tree=[] if fdebug is not None else None
        solved_flag=solver.solving(question_edge,debug_tree)
        #check solving result:
        if solved_flag:
            #print('Final Result: {} {}'.format(question_edge.out_node.value,question_edge.out_node.unit))
            if isinstance(question_edge.out_node,PU):
                predicted='{} {}'.format(question_edge.out_node.value,question_edge.out_node.unit)
            elif isinstance(question_edge.out_node,ChemicalEquation):
                predicted = question_edge.out_node.to_str()
            else:
                predicted=str(question_edge.out_node)
        else:
            print('unsolved')

        if debug_tree is not None and fdebug is not None:
            fdebug.write('\t'.join([json.dumps(parsed_question,ensure_ascii=False),
                                    ' '.join(debug_tree),debug_tree[-1]])+'\n')
        break

    return predicted


with open(sys.argv[1],'r',encoding='utf-8') as f:
    with open(sys.argv[2],'w',encoding='utf-8') as fout:
        with open(sys.argv[3], 'w', encoding='utf-8') as fdebug:
            for line in f:
                ss = line.strip().split('\t')
                if len(ss) == 6:
                    predicted = solve_one_question(json.loads(ss[4]),fdebug=fdebug)
                    ss.append(str(predicted))
                    fout.write('\t'.join(ss) + '\n')

