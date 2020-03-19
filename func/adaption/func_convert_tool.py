import json
import sys



def read_predicates_set(filename):
    vocab_set=set()
    with open(filename,'r',encoding='utf-8') as f:
        for line in f:
            vocab_set.add(line.strip())
    print('INFO: Read Predicate Vocab Successful, {} predicates in total'.format(len(vocab_set)))
    return vocab_set

def read_predicates_map(filename):
    mention2predicate={}
    with open(filename,'r',encoding='utf-8') as f:
        for line in f:
            ss=line.strip().split('\t')
            if len(ss) == 2:
                mention2predicate[ss[0]]=ss[1]
                mention2predicate[ss[0].lower()]=ss[1]
    print('INFO: Read Predicate Mapping (from mentions) Successful,'
          ' {} predicates in total'.format(len(mention2predicate)))
    return mention2predicate


def convert_func(inputs,predicate_set,mention2predicate):
    if len(inputs) != 5:
        return None,None,None

    #extract info from inputs
    output_predicate=inputs[1].split('=')
    output_predicate=output_predicate[1].strip().replace("'","").replace('"',"").replace(',',"")
    if output_predicate in mention2predicate:
        output_predicate=mention2predicate[output_predicate]
    output_predicate=output_predicate.replace(' ','_')

    input_predicate_list=inputs[2].split('=')
    #print(input_predicate_list[1])
    input_predicate_list=json.loads(input_predicate_list[1].strip().replace("'",'"'))
    for i,predicate in enumerate(input_predicate_list):
        if predicate in mention2predicate:
            input_predicate_list[i]=mention2predicate[predicate]
        input_predicate_list[i] = input_predicate_list[i].replace(' ','_')

    unrecognizeds=[]
    for predicate in ([output_predicate]+input_predicate_list):
        if not predicate in predicate_set:
            unrecognizeds.append(predicate)
    if len(unrecognizeds) > 0:
        print("ERROR: unrecognized predicates: {}".format(unrecognizeds))
        #print('\n'.join(inputs))
        return None,None,None


    formula=inputs[3].split(':')
    formula=formula[1].strip().replace("params","dbList").replace("dblist","dbList")
    func_formula=formula
    for i,predicate in enumerate(input_predicate_list):
        formula=formula.replace('dbList[{}]'.format(i),predicate)
        func_formula=func_formula.replace('dbList[{}]'.format(i),'self.parameters[{}].out_node.value'.format(i))

    #building output function
    func_name=''.join([x[0].upper()+x[1:] for x in input_predicate_list]+
                      ['2',output_predicate[0].upper(),output_predicate[1:]])
    #print(func_name)

    outputs=[]
    #class Func_Mass2Mole(Func):
    outputs.append('class Func_{}(Func):'.format(func_name))
    outputs.append("")
    #    name = "{Mass2Mole}"
    outputs.append('    name = "{}"'.format(func_name))
    #    description = "mole=mass/molar_mass"
    outputs.append('    description = "{}"'.format(formula))
    #    output_type="mole"
    outputs.append('    output_type = "{}"'.format(output_predicate))
    #    input_sat_maps = [["target", "molar_mass"],["target","mass"]]
    input_sat_maps=[]
    for predicate in input_predicate_list:
        input_sat_maps.append(['target',predicate])
    outputs.append('    input_sat_maps = {}'.format(json.dumps(input_sat_maps)))
    outputs.append("")
    #    def __init__(self,inputs,outputs=None):
    outputs.append('    def __init__(self,inputs,outputs=None):')
    #        super(Func_Mass2Mole,self).__init__(inputs,outputs)
    outputs.append('        super(Func_{},self).__init__(inputs,outputs)'.format(func_name))
    outputs.append("")
    #    def run_func(self):
    outputs.append('    def run_func(self):')
    #        if not self.sat_running():
    outputs.append('        if not self.sat_running():')
    #            return False
    outputs.append('            return False')
    #calculate the value
    #molarMass = self.parameters[0].out_node
    #mass = self.parameters[1].out_node
    #mole_value = mass.value / molarMass.value
    outputs.append('        value={}'.format(func_formula))
    #        self.outputs[0].out_node=PU(value=mole_value,unit='mole')
    outputs.append('        self.outputs[0].out_node=PU(value=value,unit=None)')
    #        return True
    outputs.append('        return True')

    return outputs,func_name,output_predicate





# test
'''
if __name__=='__main__':
    
    lines=[]
    lines.append("fx = Formula()")
    lines.append("fx.OutputName = 'molarmass'")
    lines.append("fx.InputNames = ['pressure','density','temperature']")
    lines.append("fx.Function = lambda dbList:dbList[1]*dbList[2]*0.082/dbList[0]")
    lines.append("rs.append(fx)")

    outputs=convert_func(inputs=lines)

    for line in outputs:
        print(line)
'''

predicate_set=read_predicates_set(sys.argv[1])
predicate_map=read_predicates_map(sys.argv[2])
success_count=0
func_list=[]
out_predicate_set=set()
with open(sys.argv[3],'r',encoding='utf-8') as f:
    with open(sys.argv[4],'w',encoding='utf-8') as fout:
        with open(sys.argv[5], 'w', encoding='utf-8') as fdebug:
            fout.write("import math\n")
            fout.write("from ..func_utils import Func\n")
            fout.write("from domain.chemistry_utils import PU,CE,ChemicalSubstance\n")
            fout.write("from parse.chemistry_parse import ParseSubstance\n")

            buffer = []
            flag = False
            for line in f:
                line = line.strip()
                if line == "fx = Formula()":
                    flag = True
                if flag:
                    buffer.append(line)
                    if line == "rs.append(fx)":
                        outputs, func_name, out_predicate = convert_func(inputs=buffer,
                                                                         predicate_set=predicate_set,
                                                                         mention2predicate=predicate_map)
                        if outputs is not None:
                            for out_line in outputs:
                                fout.write(out_line + '\n')
                            fout.write('\n')
                            success_count += 1
                            func_list.append('Func_{}'.format(func_name))
                            out_predicate_set.add(out_predicate)
                        else:
                            fdebug.write('\n'.join(buffer)+'\n')
                            fdebug.write('\n')
                        buffer = []
                        flag = False



print('Convert success {} functions, cover {} predicates'.format(success_count,len(out_predicate_set)))

with open(sys.argv[6],'w',encoding='utf-8') as fout:
    for line in func_list:
        fout.write(line+',\n')




