
import re

from model.edge import Edge
from domain.chemistry_utils import PU,CE

def generate_edges_from_question_variables(question_varaibles):
    variable_edges=[]
    for variable in question_varaibles:
        if variable['type'] == 'physical unit':
            physical_unit_pattern=re.compile(r"([\w ]+) \[OF\] ([\w ]+) \[IN\] ([\w ]+)")
            physical_unit_match=physical_unit_pattern.search(variable['value'])
            print(variable['value'])
            if physical_unit_match:
                edge=Edge.generate_edge_from_triplet([physical_unit_match.group(2),
                                                      physical_unit_match.group(1),
                                                      PU(unit=physical_unit_match.group(3))])
                variable_edges.append(edge)
    return variable_edges


def generate_edges_from_conditions(conditions):
    pass