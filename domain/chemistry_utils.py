'''
This file descripts
'''

import re

class PU:
    def __init__(self,value=None,unit=None):
        self.value=value
        self.unit=unit

    def __str__(self):
        return '{} {}'.format(self.value,self.unit)

    def __repr__(self):
        return '{} {}'.format(self.value,self.unit)

    @classmethod
    def _merge_num(cls,s):
        tokens = s.strip().split()
        str_buf = ""
        new_tokens = []
        for token in tokens:
            flag = True
            for c in token:
                if c not in "0123456789.":
                    flag = False
                    break
            if flag:
                str_buf += token
            else:
                if str_buf != "":
                    new_tokens.append(str_buf)
                str_buf = ""
                new_tokens.append(token)
        if str_buf != "":
            new_tokens.append(str_buf)
        return ' '.join(new_tokens)

    @classmethod
    def parse_from_text(cls,text):
        #\\pu{}
        if text.startswith(r'\\pu') or text.startswith(r'\\\\pu'):

            pu_pattern = re.compile(r"pu \{(.*?)\}")
            pu_match = pu_pattern.search(text)

            if pu_match:
                value_str=pu_match.group(1)
                #print('before {}'.format(value_str))
                value_str=cls._merge_num(value_str).strip()
                #print('{}'.format(value_str))
                unit_regex = re.compile(r"([0-9e+\-.]+) ([a-zA-Z]+)$")
                unit_match = unit_regex.search(value_str)

                if unit_match:
                    print(value_str)
                    try:
                        value=float(unit_match.group(1))
                        unit=unit_match.group(2)
                        return PU(value,unit)
                    except:
                        return None
        #raw text
        else:
            '''
            answer=text.split()
            unit_index = len(answer)
            answer_unit = None
            answer_value = 0
            while unit_index > 0:
                answer_value = ''.join(answer[:unit_index])
                flag = True
                try:
                    answer_value = float(answer_value)
                except:
                    flag = False
                if flag:
                    answer_unit = ' '.join(answer[unit_index:])
                    break
                unit_index -= 1
            '''
            tokens=text.split()
            try:
                value = float(tokens[0])
                unit = ' '.join(tokens[1:])
                return PU(value, unit)
            except:
                return None


        return None

class CE:
    def __init__(self,ce_str,type='substance'):
        self.ce_str=ce_str
        self.type=type





class ChemicalSubstance:
    def __init__(self,elements):
        self.elements=elements
        self._text=None

    def __str__(self):
        if self._text:
            return self._text
        text=''
        if self.elements:
            buffer = []
            for element in self.elements:
                if element['count'] ==1:
                    element_text=element['element']
                else:
                    element_text='{}{}'.format(element['element'], element['count'])
                buffer.append(element_text)
            text= ''.join(buffer)
        self._text=text
        return text

    @classmethod
    def is_same_substance(cls,substance_A, substance_B):
        res = False

        if substance_A is None or substance_B is None or substance_A.elements is None or substance_B.elements is None:
            return res

        if len(substance_A.elements) == len(substance_B.elements) and len(substance_A.elements) > 0:
            sorted_element_from_substance_A= sorted(substance_A.elements, key = lambda x: x['element'])
            sorted_element_from_substance_B = sorted(substance_B.elements, key = lambda x: x['element'])

            theSame = True
            for idx in range(len(sorted_element_from_substance_A)):
                element_FromA = sorted_element_from_substance_A[idx]
                element_FromB = sorted_element_from_substance_B[idx]

                if element_FromA['element'].lower() != element_FromB['element'].lower():
                    theSame = False
                elif element_FromA['count'] != element_FromB['count']:
                    theSame = False

                if theSame is False:
                    break

            res = theSame
        else:
            res = False

        return res



class ChemicalMixture:
    def __init__(self,substances):
        self.substances=substances
        self._text=None

    def __str__(self):
        if self._text:
            return self._text
        text=''
        if self.substances:
            buffer=[]
            for substance in self.substances:
                if substance['count']==1:
                    substance_str=str(substance['matter'])
                else:
                    substance_str='{}{}'.format(substance['count'],str(substance['matter']))
                buffer.append(substance_str)

            text='+'.join(buffer)
        self._text=text
        return text

    def whether_contain_a_substance(self,substance):
        for substance_in in self.substances:
            if ChemicalSubstance.is_same_substance(substance,substance_in):
                return True
        return False


class ChemicalEquation:
    def __init__(self,left_substances,right_substances):
        self.left_substances=left_substances
        self.right_substances=right_substances
        self._text=None

    def __str__(self):
        if self._text:
            return self._text
        buffer=[str(self.left_substances),str(self.right_substances)]
        text='='.join(buffer)
        self._text=text
        return text

    '''
    def search_a_substance_from_equation(self, givenMatter):
        foundMatterFromEquation = None

        searchCandidates = []
        searchCandidates.extend([matter for matter in self.left_matters.matters if ChemicalMatter.IsSameMatter(matter['matter'], givenMatter)])
        searchCandidates.extend([matter for matter in self.right_matters.matters if ChemicalMatter.IsSameMatter(matter['matter'], givenMatter)])

        if (searchCandidates is not None and len(searchCandidates) == 1):
            foundMatterFromEquation = searchCandidates[0]
        elif searchCandidates is None or len(searchCandidates) == 1:
            print('Not found in Equation')
        else:
            print('Disambiguation Equation')

        return foundMatterFromEquation
    '''


