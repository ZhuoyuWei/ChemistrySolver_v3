import re

from domain.chemistry_utils import (ChemicalSubstance,
                                    ChemicalMixture,
                                    ChemicalEquation)
from domain.math_utils import solve_linear_equations

LEFT_RIGHT_DELIMITERS_LIST=[r'-->', r'->', '==', '=']

def ParseSubstance(matterText=None,**kwargs):
    if matterText == None:
        return None
    pattern = re.compile('([A-Z]{1}[a-z]*)([0-9]*)')
    matches=re.findall(pattern, matterText)
    elements=[]
    for one_match in matches:
        element_count=1
        if one_match[1].strip() != "":
            element_count=int(one_match[1])
        element = one_match[0]
        elements.append({'element':element,'count':element_count})
    if len(elements) > 0:
        chemicalSubstance=ChemicalSubstance(elements)
        print(elements)
    else:
        print('Parse Matter Error: {}'.format(matterText))
        chemicalSubstance=None
    return chemicalSubstance

def ParseMixture(mixtureText=None,**kwargs):
    if mixtureText == None:
        return {'mixture':None}
    mixtureText = mixtureText.replace('(g)', '').replace(' ', '')
    matter_spans = mixtureText.strip().split('+')
    matters=[]
    #print('debug by zhuoyu matter_spans={}'.format(matter_spans))
    for matter_span in matter_spans:
        pattern = re.compile(r'([0-9]*)(.+)')
        matches = re.findall(pattern, matter_span)
        matter_text=None
        matter_count=-1
        #print('{}\t{}'.format(len(matches),matches))
        if len(matches) == 1:
            matter_count=1
            if matches[0][0] != "":
                matter_count=int(matches[0][0])
            matter_text=matches[0][1]
        else:
            print('Parse Mixture Error: {}'.format(mixtureText))
        matter=ParseSubstance(matter_text)
        #print(tmp_matter)
        #matter=tmp_matter['matter']
        if matter:
            matters.append({'matter':matter,'count':matter_count})
        else:
            pass

    if len(matters) > 0:
        chemicalMixture=ChemicalMixture(matters)
    else:
        print('Parse Mixture Error: {}'.format(mixtureText))
        chemicalMixture=None
    #print(chemicalMixture.matters)
    return {'mixture':chemicalMixture}


def ParseChemicalEquation(chemicalEquationText=None,**kwargs):
    if chemicalEquationText == None:
        return {'chemicalEquation':None}
    mixture_texts=None
    for delimiter in LEFT_RIGHT_DELIMITERS_LIST:
        if delimiter in chemicalEquationText:
            mixture_texts=chemicalEquationText.strip().split(delimiter)
            if len(mixture_texts)!=2:
                mixture_texts=None
            break

    if mixture_texts:
        mixtures=[]
        for mixture_text in mixture_texts:
            mixture=ParseMixture(mixture_text)['mixture']
            if mixture:
                mixtures.append(mixture)
            else:
                pass
        #print(mixtures)
        if len(mixtures) == 2:
            chemicalEquation=ChemicalEquation(*mixtures)
            chemicalEquation=BalanceChemicalEquation(chemicalEquation)
        else:
            print('Parse Equation Error: {}'.format(chemicalEquationText))
            chemicalEquation=None
        return {'chemicalEquation': chemicalEquation}
    return {'chemicalEquation': None}


def BalanceChemicalEquation(chemicalEquation):
    print("[BALANCE] BEFORE:{}".format(chemicalEquation))
    left_substances=chemicalEquation.left_substances.substances  #substances=[{"count","matter"}]
    right_substances=chemicalEquation.right_substances.substances

    lefts=[1]*len(left_substances)
    rights=[1]*len(right_substances)


    #Get all elements
    element_set=set()
    substances=left_substances+right_substances
    for substance in substances:
        substance=substance["matter"]
        elements=substance.elements
        for element in elements:
            element=element["element"]
            element_set.add(element)

    # Material conservation, each element has an equation
    element_list=list(element_set)
    paras=[[0]*len(substances) for element in element_list]
    b=[0]*len(element_list)
    for i,element in enumerate(element_list):
        for j,substance in enumerate(substances):
            element_count=0
            elements=substance["matter"].elements
            for item in elements:
                if element == item["element"]:
                    element_count=item["count"]
            if j >= len(left_substances):
                element_count*=-1
            paras[i][j]=element_count

    print("Will Solve: {}".format(paras))
    #solving linear equations
    solved=True
    try:
        x=solve_linear_equations(paras,b)
    except:
        solved=False

    if solved:
        i=0
        for j in range(len(chemicalEquation.left_substances.substances)):
            chemicalEquation.left_substances.substances[j]["count"]=x[i]
            i+=1
        for j in range(len(chemicalEquation.right_substances.substances)):
            chemicalEquation.right_substances.substances[j]["count"]=x[i]
            i+=1
        print("[BALANCE] x:{}".format(x))
    else:
        print("[BALANCE] x:unsolved")

    print("[BALANCE] AFTER:{}".format(chemicalEquation))
    #exit(-1)
    return chemicalEquation








#unit test
if __name__ == '__main__':
    ce_str="Na + H2O = NaOH + H2"
    ce=ParseChemicalEquation(ce_str)
