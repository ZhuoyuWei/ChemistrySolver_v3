'''
This file descripts
'''

import re

AvogadroConstant=6.02214076e23
R_in_PV_equal_nRT=8.31441
R_in_PV_equal_nRT_latm=0.0820574587
ATM=101.325

class PU:

    mention2unit=None

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
            print('in PU')

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
            text=text.replace('× 10^','e')
            tokens=text.split()
            word2digit={"one":1,"two":2,"three":3,"four":4,"five":5,
                        "six":6,"seven":7,"eight":8,"nine":9,"zero":0,
                        "each":1}
            try:
                value=tokens[0]
                if value.endswith('.') or value.endswith(',') or value.endswith('?'):
                    value=value[:-1]
                if ',' in value:
                    value=value.replace(',','')
                if value.endswith('%'):
                    value=float(value[:-1])*0.01
                else:
                    try:
                        if value.lower() in word2digit:
                            value=word2digit[value.lower()]
                        else:
                            value = float(value)
                    except:
                        rr = re.findall("[-+]?[.]?[\d]+(?:,\d\d\d)*[\.]?\d*(?:[eE][-+]?\d+)?", value)
                        #print("{}\t{}\t{}".format(text,value,rr))
                        #
                        value=float(rr[-1])
                unit = ' '.join(tokens[1:])
                if unit.endswith('.') or unit.endswith(',') or unit.endswith('?'):
                    unit=unit[:-1]
                unit=cls.get_unit_from_mention(unit)
                #print("[[debug in parsing]]: value=[{}], unit=[{}]".format(value,unit))
                return PU(value, unit)
            except:
                #print(tokens)
                #import time
                #time.sleep(1)
                return None


        return None
    @classmethod
    def read_mention2unit_from_tsv(cls):
        cls.mention2unit={}
        with open('domain/resources/units.tsv','r',encoding='utf-8') as f:
            for line in f:
                ss=line.strip().split('\t')
                if len(ss) == 2:
                    cls.mention2unit[ss[0]]=ss[1].replace(' ','_')

    @classmethod
    def get_unit_from_mention(cls,mention):
        if cls.mention2unit is None:
            cls.read_mention2unit_from_tsv()
        if mention in cls.mention2unit:
            return cls.mention2unit[mention]
        elif mention.lower() in cls.mention2unit:
            return cls.mention2unit[mention.lower()]
        else:
            return mention


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
    def to_str(self):
        return self.__str__()

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

class UnitConvertor:

    unit_maps=None

    @classmethod
    def build_unit_maps(cls):

        cls.unit_maps={
            'g':{'kg':cls.div_1000},
            'kg':{'g':cls.mul_1000},
            'j': {'kj': cls.div_1000},
            'kj': {'j': cls.mul_1000},
            'm':{'mm':cls.mul_1000,
                 'cm':cls.mul_100,
                 'dm': cls.mul_10,
                 'mol/kg':cls.equal},
            'mm':{'m':cls.div_1000,
                 'dm':cls.div_100,
                 'cm': cls.div_10},
            'cm': {'m': cls.div_100,
                   'dm': cls.div_10,
                   'mm': cls.mul_10},
            'dm': {'m': cls.div_10,
                   'cm': cls.mul_10,
                   'mm': cls.mul_100},
            'ml':{'l':cls.div_1000,
                  'm^3': cls.div_1000000},
            'l':{'ml':cls.mul_1000,
                 'm^3':cls.div_1000},
            'm^3': {'l': cls.mul_1000,
                  'ml': cls.mul_1000000},
            "k": {"°c":cls.k2c},
            "°c": {"k":cls.c2k},
            'g/l': {'kg/l': cls.div_1000,
                    'g/m^3': cls.mul_1000,
                    'g/cm^3': cls.div_1000},
            'kg/l': {'g/l': cls.mul_1000,
                     'g/m^3': cls.mul_1000000,
                     'g/cm^3': cls.equal},
            'g/m^3': {'kg/l': cls.div_1000000,
                      'g/l': cls.div_1000,
                      'g/cm^3': cls.div_1000000},
            'g/cm^3': {'kg/l': cls.equal,
                      'g/l': cls.mul_1000,
                      'g/m^3': cls.mul_1000000},
            'mol/kg': {'m': cls.equal},
            'pa':{'kpa':cls.div_1000,
                  'atm':cls.pa2atm},
            'kpa':{'pa':cls.mul_1000,
                   'atm':cls.kpa2atm},
            'atm':{'pa':cls.atm2pa,
                   'kpa':cls.atm2kpa},

        }

    @classmethod
    def div_1000000(cls,num):
        return num/1000000

    @classmethod
    def div_1000(cls,num):
        return num/1000

    @classmethod
    def div_100(cls,num):
        return num/100

    @classmethod
    def div_10(cls,num):
        return num/10

    @classmethod
    def mul_1000000(cls,num):
        return num*1000000

    @classmethod
    def mul_1000(cls,num):
        return num*1000

    @classmethod
    def mul_100(cls,num):
        return num*100

    @classmethod
    def mul_10(cls,num):
        return num*10

    @classmethod
    def k2c(cls,num):
        return num-273.15

    @classmethod
    def c2k(cls,num):
        return num+273.15

    @classmethod
    def equal(cls,num):
        return num

    @classmethod
    def pa2atm(cls,num):
        return num/1000/ATM
    @classmethod
    def kpa2atm(cls,num):
        return num/ATM

    @classmethod
    def atm2pa(cls,num):
        return num*1000*ATM
    @classmethod
    def atm2kpa(cls,num):
        return num*ATM


    @classmethod
    def converting(cls,s_pu,t_unit):
        if cls.unit_maps is None:
            cls.build_unit_maps()
        try:
            t_pu=PU(value=None,unit=t_unit)
            t_pu.value=cls.unit_maps[s_pu.unit][t_unit](s_pu.value)
        except:
            t_pu=s_pu
        return t_pu

