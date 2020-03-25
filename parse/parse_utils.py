import re

from model.edge import Edge
from domain.chemistry_utils import PU,CE


def generate_edges_from_question_variables(question_varaibles):
    variable_edges=[]
    for variable in question_varaibles:
        edge=None
        if variable['type'] == 'physical unit':
            #physical_unit_pattern=re.compile(r"([\w ]+) \[OF\] ([\w ]+) \[IN\] ([\w ]+)")
            #physical_unit_match=physical_unit_pattern.search(variable['value'])
            #print(variable['value'])
            #if physical_unit_match:
            edge=Edge.generate_edge_from_triplet([variable['value']['subject'],
                                                      variable['value']['predicate'],
                                                      PU(unit=variable['value']['unit'])])
        elif variable['type'] == 'chemical formula':
            edge=Edge.generate_edge_from_triplet([variable['value']['subject'],
                                             variable['value']['predicate'],
                                             None])
        elif variable['type'] == 'chemical equation':
            #print("Haven't implement chemical equation")
            edge=Edge.generate_edge_from_triplet([variable['value']['subject'],
                                             variable['value']['predicate'],
                                             None])

        elif variable['type'] == 'other':
            pass

        if edge is not None:
            variable_edges.append(edge)

    return variable_edges

def generate_edges_from_conditions(conditions):
    condition_edges=[]
    for condition in conditions:
        edge=None
        if condition["type"] == "physical unit":
            #physical_unit_pattern=re.compile(r"([\w ]+) \[OF\] ([\w ]+) \[=\](.*)")
            #physical_unit_match=physical_unit_pattern.search(condition['value'])
            #if physical_unit_match:
            #parsed_PU=PU.parse_from_text(condition['value']['value'])
            parsed_PU = PU.parse_pu_from_text(condition['value']['value'])
            if parsed_PU:
                    edge=Edge.generate_edge_from_triplet([condition['value']['subject'],
                                                          condition['value']['predicate'],
                                                          parsed_PU])

            else:
                print('debug by zhuoyu, cannot parsed condition = {}'.format(condition))
                print('PU parsed Fail: {}'.format(condition['value']['value']))

        elif condition['type'] == 'chemical formula' \
                or condition['type'] == 'chemical equation':
            edge=Edge.generate_edge_from_triplet([condition['value']['subject'],
                                             condition['value']['predicate'],
                                             condition['value']['value']])
        if edge is not None:
            condition_edges.append(edge)

    return condition_edges


'''
#old format
def generate_edges_from_question_variables_old(question_varaibles):
    variable_edges=[]
    for variable in question_varaibles:
        if variable['type'] == 'physical unit':
            physical_unit_pattern=re.compile(r"([\w ]+) \[OF\] ([\w ]+) \[IN\] ([\w ]+)")
            physical_unit_match=physical_unit_pattern.search(variable['value'])
            #print(variable['value'])
            if physical_unit_match:
                edge=Edge.generate_edge_from_triplet([physical_unit_match.group(2),
                                                      physical_unit_match.group(1),
                                                      PU(unit=physical_unit_match.group(3))])
                variable_edges.append(edge)
    return variable_edges



def generate_edges_from_conditions_old(conditions):
    condition_edges=[]
    for condition in conditions:
        if condition["type"] == "physical unit":
            physical_unit_pattern=re.compile(r"([\w ]+) \[OF\] ([\w ]+) \[=\](.*)")
            physical_unit_match=physical_unit_pattern.search(condition['value'])
            if physical_unit_match:
                parsed_PU=PU.parse_from_text(physical_unit_match.group(3))
                if parsed_PU:
                    edge=Edge.generate_edge_from_triplet([physical_unit_match.group(2),
                                                      physical_unit_match.group(1),parsed_PU])
                    condition_edges.append(edge)
            else:
                print('debug by zhuoyu, cannot parsed condition = {}'.format(condition))
    return condition_edges
'''