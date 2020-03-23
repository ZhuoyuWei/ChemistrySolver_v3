'''

Molarity(x,y) ^ Mole(x,z) => Volume(x,a)
a=f_volume(Molarity(x,y),Mole(x,z))


If we know the following ideal gas equation:
    PV=nRT
How to solve different

'''
import math
from .func_utils import Func
from domain.chemistry_utils import PU,CE,ChemicalSubstance,AvogadroConstant,R_in_PV_equal_nRT,R_in_PV_equal_nRT_latm,ATM
from parse.chemistry_parse import ParseSubstance


#DICT_MolarMassElement={"K":39.0983,"Cl":35.453,"P":30.9738,"O":15.999,"C":12.010,"H":1.007,"N":14.0067,"He":4.002,"F":18.998,"Al":26.981,"Na":22.989,"Mg":24.304,"S":32.059,"Br":79.901}
DICT_MolarMassElement={"H":1.0079,"He":4.0026,"Li":6.941,"Be":9.0122,"B":10.811,"C":12.0107,"N":14.0067,"O":15.9994,"F":18.9984,"Ne":20.1797,"Na":22.9897,"Mg":24.305,"Al":26.9815,"Si":28.0855,"P":30.9738,"S":32.065,"Cl":35.453,"K":39.0983,"Ar":39.948,"Ca":40.078,"Sc":44.9559,"Ti":47.867,"V":50.9415,"Cr":51.9961,"Mn":54.938,"Fe":55.845,"Ni":58.6934,"Co":58.9332,"Cu":63.546,"Zn":65.39,"Ga":69.723,"Ge":72.64,"As":74.9216,"Se":78.96,"Br":79.904,"Kr":83.8,"Rb":85.4678,"Sr":87.62,"Y":88.9059,"Zr":91.224,"Nb":92.9064,"Mo":95.94,"Tc":98,"Ru":101.07,"Rh":102.9055,"Pd":106.42,"Ag":107.8682,"Cd":112.411,"In":114.818,"Sn":118.71,"Sb":121.76,"I":126.9045,"Te":127.6,"Xe":131.293,"Cs":132.9055,"Ba":137.327,"La":138.9055,"Ce":140.116,"Pr":140.9077,"Nd":144.24,"Pm":145,"Sm":150.36,"Eu":151.964,"Gd":157.25,"Tb":158.9253,"Dy":162.5,"Ho":164.9303,"Er":167.259,"Tm":168.9342,"Yb":173.04,"Lu":174.967,"Hf":178.49,"Ta":180.9479,"W":183.84,"Re":186.207,"Os":190.23,"Ir":192.217,"Pt":195.078,"Au":196.9665,"Hg":200.59,"Tl":204.3833,"Pb":207.2,"Bi":208.9804,"Po":209,"At":210,"Rn":222,"Fr":223,"Ra":226,"Ac":227,"Pa":231.0359,"Th":232.0381,"Np":237,"U":238.0289,"Am":243,"Pu":244,"Cm":247,"Bk":247,"Cf":251,"Es":252,"Fm":257,"Md":258,"No":259,"Rf":261,"Lr":262,"Db":262,"Bh":264,"Sg":266,"Mt":268,"Rg":272,"Hs":277,"Hydrogen":1.0079,"Helium":4.0026,"Lithium":6.941,"Beryllium":9.0122,"Boron":10.811,"Carbon":12.0107,"Nitrogen":14.0067,"Oxygen":15.9994,"Fluorine":18.9984,"Neon":20.1797,"Sodium":22.9897,"Magnesium":24.305,"Aluminum":26.9815,"Silicon":28.0855,"Phosphorus":30.9738,"Sulfur":32.065,"Chlorine":35.453,"Potassium":39.0983,"Argon":39.948,"Calcium":40.078,"Scandium":44.9559,"Titanium":47.867,"Vanadium":50.9415,"Chromium":51.9961,"Manganese":54.938,"Iron":55.845,"Nickel":58.6934,"Cobalt":58.9332,"Copper":63.546,"Zinc":65.39,"Gallium":69.723,"Germanium":72.64,"Arsenic":74.9216,"Selenium":78.96,"Bromine":79.904,"Krypton":83.8,"Rubidium":85.4678,"Strontium":87.62,"Yttrium":88.9059,"Zirconium":91.224,"Niobium":92.9064,"Molybdenum":95.94,"Technetium":98,"Ruthenium":101.07,"Rhodium":102.9055,"Palladium":106.42,"Silver":107.8682,"Cadmium":112.411,"Indium":114.818,"Tin":118.71,"Antimony":121.76,"Iodine":126.9045,"Tellurium":127.6,"Xenon":131.293,"Cesium":132.9055,"Barium":137.327,"Lanthanum":138.9055,"Cerium":140.116,"Praseodymium":140.9077,"Neodymium":144.24,"Promethium":145,"Samarium":150.36,"Europium":151.964,"Gadolinium":157.25,"Terbium":158.9253,"Dysprosium":162.5,"Holmium":164.9303,"Erbium":167.259,"Thulium":168.9342,"Ytterbium":173.04,"Lutetium":174.967,"Hafnium":178.49,"Tantalum":180.9479,"Tungsten":183.84,"Rhenium":186.207,"Osmium":190.23,"Iridium":192.217,"Platinum":195.078,"Gold":196.9665,"Mercury":200.59,"Thallium":204.3833,"Lead":207.2,"Bismuth":208.9804,"Polonium":209,"Astatine":210,"Radon":222,"Francium":223,"Radium":226,"Actinium":227,"Protactinium":231.0359,"Thorium":232.0381,"Neptunium":237,"Uranium":238.0289,"Americium":243,"Plutonium":244,"Curium":247,"Berkelium":247,"Californium":251,"Einsteinium":252,"Fermium":257,"Mendelevium":258,"Nobelium":259,"Rutherfordium":261,"Lawrencium":262,"Dubnium":262,"Bohrium":264,"Seaborgium":266,"Meitnerium":268,"Roentgenium":272,"Hassium":277}
class Func_Name2CE(Func):
    '''
    just as an example, CE is a text
    '''

    name = "Name2CE"
    description = "Convert a substance name to its chemical equation (CE)"
    output_type="Chemistry_Substance"
    output_unit = None
    input_sat_maps = [["target", "name", None]]
    NAME2CE=None

    def _read_Name2CE_from_Resource(self):
        if Func_Name2CE.NAME2CE is None:
            Func_Name2CE.NAME2CE={}
            with open('domain/resources/Substance2Formula.tsv','r',encoding='utf-8') as f:
                for line in f:
                    ss=line.strip().split('\t')
                    if len(ss) == 2:
                        Func_Name2CE.NAME2CE[ss[0]]=ss[1]


    def __init__(self,inputs,outputs=None):
        super(Func_Name2CE,self).__init__(inputs,outputs)
        self._read_Name2CE_from_Resource()


    def run_func(self):
        if not self.sat_running():
            return False
        ce_str=Func_Name2CE.NAME2CE.get(self.parameters[0].out_node,None)
        print('in ce parser, ce_str={},name={}'.format(ce_str,self.parameters[0].out_node))
        if ce_str == None:
            ce_str=self.parameters[0].out_node
        chemistry_substance=ParseSubstance(ce_str)
        print('chemistry_substance = {}'.format(chemistry_substance))
        self.outputs[0].out_node=chemistry_substance
        return (chemistry_substance is not None)

class Func_Formula2CE(Func):
    '''
    just as an example, CE is a text
    '''

    name = "Formula2CE"
    description = "Convert a substance (chemical) formula to its chemical equation/formula (CE/CF)"
    output_type="Chemistry_Substance"
    output_unit=None
    input_sat_maps = [["target", "formula",None]]
    NAME2CE=None



    def __init__(self,inputs,outputs=None):
        super(Func_Formula2CE,self).__init__(inputs,outputs)



    def run_func(self):
        if not self.sat_running():
            return False
        ce_str=self.parameters[0].out_node
        #print('in ce parser, ce_str={},name={}'.format(ce_str,self.parameters[0].out_node))
        chemistry_substance=ParseSubstance(ce_str)
        #print('chemistry_substance = {}'.format(chemistry_substance))
        self.outputs[0].out_node=chemistry_substance
        return (chemistry_substance is not None)

class Func_Mole2Atom(Func):

    name = "Mole2Atom"
    description = "Calculate the number of Atom from the Mole"
    output_type="atom"
    output_unit=None
    input_sat_maps = [["target", "mole", "mole"]]

    def __init__(self,inputs,outputs=None):
        super(Func_Mole2Atom,self).__init__()
        self.inputs = inputs
        self.outputs = outputs

    def run_func(self):
        if not self._sat_running():
            return False
        value=self.parameters[0].out_node.value*AvogadroConstant
        self.outputs[0].out_node=PU(value=value,unit=self.__class__.output_unit)
        return True



class Func_CE2MolarMass(Func):
    '''
    just as an example, CE is a text
    '''

    name = "Name2MolarMass"
    description = "from the CE of a substance to its MolarMass"
    output_type="molar_mass"
    output_unit='g/mol'
    input_sat_maps = [["target", "Chemistry_Substance",None]]


    def __init__(self,inputs,outputs=None):
        super(Func_CE2MolarMass,self).__init__(inputs,outputs)


    def run_func(self):
        if not self.sat_running():
            return False
        chemistry_substance=self.parameters[0].out_node
        print('cs in molarmass')
        sum=0
        for element_pair in chemistry_substance.elements:
            element=element_pair['element']
            element_count=element_pair['count']
            print(element_pair)
            sum+=DICT_MolarMassElement.get(element,0)*element_count
        if sum == 0:
            return False
        else:
            self.outputs[0].out_node=PU(value=sum,unit=self.__class__.output_unit)
            return True

class Func_Mass2Mole(Func):
    '''
    just as an example, CE is a text
    '''

    name = "Mass2Mole"
    description = "mole=mass/molar_mass"
    output_type="mole"
    output_unit="mol"
    input_sat_maps = [["target", "molar_mass","g/mol"],["target","mass","g"]]


    def __init__(self,inputs,outputs=None):
        super(Func_Mass2Mole,self).__init__(inputs,outputs)


    def run_func(self):
        if not self.sat_running():
            return False
        molarMass=self.parameters[0].out_node
        mass=self.parameters[1].out_node
        mole_value=mass.value/molarMass.value
        self.outputs[0].out_node=PU(value=mole_value,unit=self.__class__.output_unit)
        return True


'''
The following functions are converted from old version
'''
class Func_Ph2Kw(Func):

    name = "Ph2Kw"
    description = "10 ** (-ph * 2)"
    output_type = "kw"
    output_unit = None
    input_sat_maps = [["target", "ph",None]]

    def __init__(self,inputs,outputs=None):
        super(Func_Ph2Kw,self).__init__(inputs,outputs)

    def run_func(self):
        if not self.sat_running():
            return False
        value=10 ** (-self.parameters[0].out_node.value * 2)
        self.outputs[0].out_node=PU(value=value,unit=self.__class__.output_unit)
        return True

class Func_Number2Mole(Func):

    name = "Number2Mole"
    description = "number / 6.022e23"
    output_type = "mole"
    output_unit = "mol"
    input_sat_maps = [["target", "number", None]]

    def __init__(self,inputs,outputs=None):
        super(Func_Number2Mole,self).__init__(inputs,outputs)

    def run_func(self):
        if not self.sat_running():
            return False
        value=self.parameters[0].out_node.value / AvogadroConstant
        self.outputs[0].out_node=PU(value=value,unit=self.__class__.output_unit)
        return True

class Func_Mole2Number(Func):

    name = "Mole2Number"
    description = "mole * 6.022e23"
    output_type = "number"
    output_unit = None
    input_sat_maps = [["target", "mole", "mol"]]

    def __init__(self,inputs,outputs=None):
        super(Func_Mole2Number,self).__init__(inputs,outputs)

    def run_func(self):
        if not self.sat_running():
            return False
        value=self.parameters[0].out_node.value * AvogadroConstant
        self.outputs[0].out_node=PU(value=value,unit=self.__class__.output_unit)
        return True

class Func_MassMolar_mass2Mole(Func):

    name = "MassMolar_mass2Mole"
    description = "mass / molar_mass"
    output_type = "mole"
    output_unit = "mol"
    input_sat_maps = [["target", "mass","g"], ["target", "molar_mass","g/mol"]]

    def __init__(self,inputs,outputs=None):
        super(Func_MassMolar_mass2Mole,self).__init__(inputs,outputs)

    def run_func(self):
        if not self.sat_running():
            return False
        value=self.parameters[0].out_node.value / self.parameters[1].out_node.value
        self.outputs[0].out_node=PU(value=value,unit=self.__class__.output_unit)
        return True

class Func_MoleMolar_mass2Mass(Func):

    name = "MoleMolar_mass2Mass"
    description = "mole * molar_mass"
    output_type = "mass"
    output_unit = "g"
    input_sat_maps = [["target", "mole", "mol"], ["target", "molar_mass", "g/mol"]]

    def __init__(self,inputs,outputs=None):
        super(Func_MoleMolar_mass2Mass,self).__init__(inputs,outputs)

    def run_func(self):
        if not self.sat_running():
            return False
        print("DEBUG: parameters: {}".format(self.parameters))
        value=self.parameters[0].out_node.value * self.parameters[1].out_node.value
        self.outputs[0].out_node=PU(value=value,unit=self.__class__.output_unit)
        return True

class Func_VolumeMolarity2Mole(Func):

    name = "VolumeMolarity2Mole"
    description = "volume * 1.0 * molarity"
    output_type = "mole"
    output_type = "mol"
    input_sat_maps = [["target", "volume", "l"], ["target", "molarity", "mol/l"]]

    def __init__(self,inputs,outputs=None):
        super(Func_VolumeMolarity2Mole,self).__init__(inputs,outputs)

    def run_func(self):
        if not self.sat_running():
            return False
        value=self.parameters[0].out_node.value * 1.0 * self.parameters[1].out_node.value
        self.outputs[0].out_node=PU(value=value,unit=self.__class__.output_unit)
        return True

class Func_VolumeMoleTemperature2Pressure(Func):

    name = "VolumeMoleTemperature2Pressure"
    description = "mole * temperature * R_in_PV_equal_nRT / volume"
    output_type = "pressure"
    output_unit = "pa"
    input_sat_maps = [["target", "volume","m^3"], ["target", "mole", "mol"], ["target", "temperature","k"]]

    def __init__(self,inputs,outputs=None):
        super(Func_VolumeMoleTemperature2Pressure,self).__init__(inputs,outputs)

    def run_func(self):
        if not self.sat_running():
            return False
        value=self.parameters[1].out_node.value * self.parameters[2].out_node.value * R_in_PV_equal_nRT / self.parameters[0].out_node.value
        self.outputs[0].out_node=PU(value=value,unit=self.__class__.output_unit)
        return True

class Func_VolumeTemperaturePressure2Mole(Func):

    name = "VolumeTemperaturePressure2Mole"
    description = "pressure * volume / (temperature * R_in_PV_equal_nRT)"
    output_type = "mole"
    output_unit = "mol"
    input_sat_maps = [["target", "volume", "m^3"], ["target", "temperature", "k"], ["target", "pressure", "pa"]]

    def __init__(self,inputs,outputs=None):
        super(Func_VolumeTemperaturePressure2Mole,self).__init__(inputs,outputs)

    def run_func(self):
        if not self.sat_running():
            return False
        value=self.parameters[2].out_node.value * self.parameters[0].out_node.value / (self.parameters[1].out_node.value * R_in_PV_equal_nRT)
        self.outputs[0].out_node=PU(value=value,unit=self.__class__.output_unit)
        return True

class Func_PressureMolar_massTemperature2Density(Func):

    name = "PressureMolar_massTemperature2Density"
    description = "1000 * pressure * molar_mass  / (temperature * R_in_PV_equal_nRT )"
    output_type = "density"
    output_type = "g/l"
    input_sat_maps = [["target", "pressure", "pa"], ["target", "molar_mass", "g/mol"], ["target", "temperature", "k"]]

    def __init__(self,inputs,outputs=None):
        super(Func_PressureMolar_massTemperature2Density,self).__init__(inputs,outputs)

    def run_func(self):
        if not self.sat_running():
            return False
        value=1000 * self.parameters[0].out_node.value * self.parameters[1].out_node.value\
              / (self.parameters[2].out_node.value * R_in_PV_equal_nRT)
        self.outputs[0].out_node=PU(value=value,unit=self.__class__.output_unit)
        return True

class Func_PressureDensityTemperature2Molar_mass(Func):

    name = "PressureDensityTemperature2Molar_mass"
    description = "density/1000 * temperature * R_in_PV_equal_nRT / pressure"
    output_type = "molar_mass"
    output_type = "g/mol"
    input_sat_maps = [["target", "pressure","pa"], ["target", "density", "g/l"], ["target", "temperature", "k"]]

    def __init__(self,inputs,outputs=None):
        super(Func_PressureDensityTemperature2Molar_mass,self).__init__(inputs,outputs)

    def run_func(self):
        if not self.sat_running():
            return False
        value=self.parameters[1].out_node.value/1000 * self.parameters[2].out_node.value * R_in_PV_equal_nRT/ self.parameters[0].out_node.value
        self.outputs[0].out_node=PU(value=value,unit=self.__class__.output_unit)
        return True

class Func_MoleMass2Molar_mass(Func):

    name = "MoleMass2Molar_mass"
    description = "mass / mole"
    output_type = "molar_mass"
    output_unit="g/mol"
    input_sat_maps = [["target", "mole","mol"], ["target", "mass","g"]]

    def __init__(self,inputs,outputs=None):
        super(Func_MoleMass2Molar_mass,self).__init__(inputs,outputs)

    def run_func(self):
        if not self.sat_running():
            return False
        value=self.parameters[1].out_node.value / self.parameters[0].out_node.value
        self.outputs[0].out_node=PU(value=value,unit=self.__class__.output_unit)
        return True

class Func_MoleVolumePressure2Temperature(Func):

    name = "MoleVolumePressure2Temperature"
    description = "pressure * volume / (mole * R_in_PV_equal_nRT)"
    output_type = "temperature"
    output_type = "k"
    input_sat_maps = [["target", "mole", "mol"], ["target", "volume", "m^3"], ["target", "pressure", "pa"]]

    def __init__(self,inputs,outputs=None):
        super(Func_MoleVolumePressure2Temperature,self).__init__(inputs,outputs)

    def run_func(self):
        if not self.sat_running():
            return False
        value=self.parameters[2].out_node.value * self.parameters[1].out_node.value / (self.parameters[0].out_node.value * R_in_PV_equal_nRT)
        self.outputs[0].out_node=PU(value=value,unit=self.__class__.output_unit)
        return True

class Func_MoleTemperaturePressure2Volume(Func):

    name = "MoleTemperaturePressure2Volume"
    description = "mole * R_in_PV_equal_nRT * temperature / pressure"
    output_type = "volume"
    output_unit = "m^3"
    input_sat_maps = [["target", "mole", "mol"], ["target", "temperature", "k"], ["target", "pressure", "pa"]]

    def __init__(self,inputs,outputs=None):
        super(Func_MoleTemperaturePressure2Volume,self).__init__(inputs,outputs)

    def run_func(self):
        if not self.sat_running():
            return False
        value=self.parameters[0].out_node.value * R_in_PV_equal_nRT * self.parameters[1].out_node.value / self.parameters[2].out_node.value
        self.outputs[0].out_node=PU(value=value,unit=self.__class__.output_unit)
        return True

class Func_MoleVolume2Molarity(Func):

    name = "MoleVolume2Molarity"
    description = "mole / volume"
    output_type = "molarity"
    output_unit = "mol/l"
    input_sat_maps = [["target", "mole","mol"], ["target", "volume", "l"]]

    def __init__(self,inputs,outputs=None):
        super(Func_MoleVolume2Molarity,self).__init__(inputs,outputs)

    def run_func(self):
        if not self.sat_running():
            return False
        value=self.parameters[0].out_node.value / self.parameters[1].out_node.value
        self.outputs[0].out_node=PU(value=value,unit=self.__class__.output_unit)
        return True

class Func_MolarityVolume2Mole(Func):

    name = "MolarityVolume2Mole"
    description = "molarity * volume"
    output_type = "mole"
    output_unit="mol"
    input_sat_maps = [["target", "molarity","mol/l"], ["target", "volume","l"]]

    def __init__(self,inputs,outputs=None):
        super(Func_MolarityVolume2Mole,self).__init__(inputs,outputs)

    def run_func(self):
        if not self.sat_running():
            return False
        value=self.parameters[0].out_node.value * self.parameters[1].out_node.value
        self.outputs[0].out_node=PU(value=value,unit=self.__class__.output_unit)
        return True

class Func_MoleMolarity2Volume(Func):

    name = "MoleMolarity2Volume"
    description = "mole / molarity"
    output_type = "volume"
    output_unit = "l"
    input_sat_maps = [["target", "mole", "mol"], ["target", "molarity", "mol/l"]]

    def __init__(self,inputs,outputs=None):
        super(Func_MoleMolarity2Volume,self).__init__(inputs,outputs)

    def run_func(self):
        if not self.sat_running():
            return False
        print('Debug in Func_MoleMolarity2Volume: {}/{}'.format(self.parameters[0].out_node.value,
                                                                self.parameters[1].out_node.value))
        value=self.parameters[0].out_node.value / self.parameters[1].out_node.value
        self.outputs[0].out_node=PU(value=value,unit=self.__class__.output_unit)
        return True

class Func_Ph2Acid_concentration(Func):

    name = "Ph2Acid_concentration"
    description = "10 ** (-ph)"
    output_type = "acid_concentration"
    output_unit = "mol/l"
    input_sat_maps = [["target", "ph", None]]

    def __init__(self,inputs,outputs=None):
        super(Func_Ph2Acid_concentration,self).__init__(inputs,outputs)

    def run_func(self):
        if not self.sat_running():
            return False
        value=10 ** (-self.parameters[0].out_node.value)
        self.outputs[0].out_node=PU(value=value,unit=self.__class__.output_unit)
        return True

class Func_Acid_concentration2Ph(Func):

    name = "Acid_concentration2Ph"
    description = "-math.log10(acid_concentration)"
    output_type = "ph"
    output_unit=None
    input_sat_maps = [["target", "acid_concentration","mol/l"]]

    def __init__(self,inputs,outputs=None):
        super(Func_Acid_concentration2Ph,self).__init__(inputs,outputs)

    def run_func(self):
        if not self.sat_running():
            return False
        value=-math.log10(self.parameters[0].out_node.value)
        self.outputs[0].out_node=PU(value=value,unit=self.__class__.output_unit)
        return True

class Func_Ph2Poh(Func):

    name = "Ph2Poh"
    description = "14 - ph"
    output_type = "poh"
    output_type = None
    input_sat_maps = [["target", "ph",None]]

    def __init__(self,inputs,outputs=None):
        super(Func_Ph2Poh,self).__init__(inputs,outputs)

    def run_func(self):
        if not self.sat_running():
            return False
        value=14 - self.parameters[0].out_node.value
        self.outputs[0].out_node=PU(value=value,unit=self.__class__.output_unit)
        return True

class Func_Poh2Ph(Func):

    name = "Poh2Ph"
    description = "14 - poh"
    output_type = "ph"
    output_unit = None
    input_sat_maps = [["target", "poh",None]]

    def __init__(self,inputs,outputs=None):
        super(Func_Poh2Ph,self).__init__(inputs,outputs)

    def run_func(self):
        if not self.sat_running():
            return False
        value=14 - self.parameters[0].out_node.value
        self.outputs[0].out_node=PU(value=value,unit=self.__class__.output_unit)
        return True

class Func_Ka2Pka(Func):

    name = "Ka2Pka"
    description = "-math.log10(ka)"
    output_type = "pka"
    output_unit = None
    input_sat_maps = [["target", "ka",None]]

    def __init__(self,inputs,outputs=None):
        super(Func_Ka2Pka,self).__init__(inputs,outputs)

    def run_func(self):
        if not self.sat_running():
            return False
        value=-math.log10(self.parameters[0].out_node.value)
        self.outputs[0].out_node=PU(value=value,unit=self.__class__.output_unit)
        return True

class Func_Mass_concentrationMolar_mass2Molarity(Func):

    name = "Mass_concentrationMolar_mass2Molarity"
    description = "mass_concentration * 100 / molar_mass / 0.1"
    output_type = "molarity"
    output_unit = "mol/l"
    input_sat_maps = [["target", "mass_concentration","g/l"], ["target", "molar_mass","g/mol"]]

    def __init__(self,inputs,outputs=None):
        super(Func_Mass_concentrationMolar_mass2Molarity,self).__init__(inputs,outputs)

    def run_func(self):
        if not self.sat_running():
            return False
        value=self.parameters[0].out_node.value * 100 / self.parameters[1].out_node.value / 0.1
        self.outputs[0].out_node=PU(value=value,unit=self.__class__.output_unit)
        return True

class Func_MassVolume2Density(Func):

    name = "MassVolume2Density"
    description = "mass * 1.0 / volume"
    output_type = "density"
    output_unit = "g/l"
    input_sat_maps = [["target", "mass", "g"], ["target", "volume", "l"]]

    def __init__(self,inputs,outputs=None):
        super(Func_MassVolume2Density,self).__init__(inputs,outputs)

    def run_func(self):
        if not self.sat_running():
            return False
        value=self.parameters[0].out_node.value * 1.0 / self.parameters[1].out_node.value
        self.outputs[0].out_node=PU(value=value,unit=self.__class__.output_unit)
        return True

class Func_DensityVolume2Mass(Func):

    name = "DensityVolume2Mass"
    description = "density * volume"
    output_type = "mass"
    output_unit = "g"
    input_sat_maps = [["target", "density", "g/l"], ["target", "volume", "l"]]

    def __init__(self,inputs,outputs=None):
        super(Func_DensityVolume2Mass,self).__init__(inputs,outputs)

    def run_func(self):
        if not self.sat_running():
            return False
        value=self.parameters[0].out_node.value * self.parameters[1].out_node.value
        self.outputs[0].out_node=PU(value=value,unit=self.__class__.output_unit)
        return True

class Func_MassDensity2Volume(Func):

    name = "MassDensity2Volume"
    description = "mass * 1.0 / density"
    output_type = "volume"
    output_unit = "l"
    input_sat_maps = [["target", "mass","g"], ["target", "density", "g/l"]]

    def __init__(self,inputs,outputs=None):
        super(Func_MassDensity2Volume,self).__init__(inputs,outputs)

    def run_func(self):
        if not self.sat_running():
            return False
        value=self.parameters[0].out_node.value * 1.0 / self.parameters[1].out_node.value
        self.outputs[0].out_node=PU(value=value,unit=self.__class__.output_unit)
        return True

class Func_MolarityMolar_mass2Molality(Func):

    name = "MolarityMolar_mass2Molality"
    description = "molarity * 1000 / (1000 - molarity * molar_mass)"
    output_type = "molality"
    output_unit = "mol/kg"
    input_sat_maps = [["target", "molarity","mol/l"], ["target", "molar_mass","g/mol"]]

    def __init__(self,inputs,outputs=None):
        super(Func_MolarityMolar_mass2Molality,self).__init__(inputs,outputs)

    def run_func(self):
        if not self.sat_running():
            return False
        value=self.parameters[0].out_node.value * 1000 / (1000 - self.parameters[0].out_node.value * self.parameters[1].out_node.value)
        self.outputs[0].out_node=PU(value=value,unit=self.__class__.output_unit)
        return True

class Func_MolalityMolar_mass2Molarity(Func):

    name = "MolalityMolar_mass2Molarity"
    description = "molality * 1000 / (1000 + molality * molar_mass)"
    output_type = "molarity",
    output_unit = "mol/l"
    input_sat_maps = [["target", "molality", "mol/kg"], ["target", "molar_mass", "g"]]

    def __init__(self,inputs,outputs=None):
        super(Func_MolalityMolar_mass2Molarity,self).__init__(inputs,outputs)

    def run_func(self):
        if not self.sat_running():
            return False
        value=self.parameters[0].out_node.value * 1000 / (1000 + self.parameters[0].out_node.value * self.parameters[1].out_node.value)
        self.outputs[0].out_node=PU(value=value,unit=self.__class__.output_unit)
        return True

#unsolved the unit
class Func_MolarityTemperature2Osmolarity(Func):

    name = "MolarityTemperature2Osmolarity"
    description = "molarity * temperature * R_in_PV_equal_nRT / 101.325"
    output_type = "osmolarity"
    output_unit= "osmol/l"
    input_sat_maps = [["target", "molarity", "mol/l"], ["target", "temperature","k"]]

    def __init__(self,inputs,outputs=None):
        super(Func_MolarityTemperature2Osmolarity,self).__init__(inputs,outputs)

    def run_func(self):
        if not self.sat_running():
            return False
        value=self.parameters[0].out_node.value * self.parameters[1].out_node.value * R_in_PV_equal_nRT / 101.325
        self.outputs[0].out_node=PU(value=value,unit=self.__class__.output_unit)
        return True

class Func_Theoretical_yieldPercent_yield2Actual_yield(Func):

    name = "Theoretical_yieldPercent_yield2Actual_yield"
    description = "theoretical_yield * percent_yield"
    output_type = "actual_yield"
    output_unit = None
    input_sat_maps = [["target", "theoretical_yield", None], ["target", "percent_yield", None]]

    def __init__(self,inputs,outputs=None):
        super(Func_Theoretical_yieldPercent_yield2Actual_yield,self).__init__(inputs,outputs)

    def run_func(self):
        if not self.sat_running():
            return False
        value=self.parameters[0].out_node.value * self.parameters[1].out_node.value
        self.outputs[0].out_node=PU(value=value,unit=self.__class__.output_unit)
        return True

class Func_Actual_yieldPercent_yield2Theoretical_yield(Func):

    name = "Actual_yieldPercent_yield2Theoretical_yield"
    description = "actual_yield * 1.0 / percent_yield"
    output_type = "theoretical_yield"
    output_unit = None
    input_sat_maps = [["target", "actual_yield", None], ["target", "percent_yield", None]]

    def __init__(self,inputs,outputs=None):
        super(Func_Actual_yieldPercent_yield2Theoretical_yield,self).__init__(inputs,outputs)

    def run_func(self):
        if not self.sat_running():
            return False
        value=self.parameters[0].out_node.value * 1.0 / self.parameters[1].out_node.value
        self.outputs[0].out_node=PU(value=value,unit=self.__class__.output_unit)
        return True

class Func_Theoretical_yieldActual_yield2Percent_yield(Func):

    name = "Theoretical_yieldActual_yield2Percent_yield"
    description = "actual_yield * 1.0 / theoretical_yield"
    output_type = "percent_yield"
    output_unit = None
    input_sat_maps = [["target", "theoretical_yield",None], ["target", "actual_yield",None]]

    def __init__(self,inputs,outputs=None):
        super(Func_Theoretical_yieldActual_yield2Percent_yield,self).__init__(inputs,outputs)

    def run_func(self):
        if not self.sat_running():
            return False
        value=self.parameters[1].out_node.value * 1.0 / self.parameters[0].out_node.value
        self.outputs[0].out_node=PU(value=value,unit=self.__class__.output_unit)
        return True

class Func_Ka2Degree_of_dissociation(Func):

    name = "Ka2Degree_of_dissociation"
    description = "2 / (-1 + math.sqrt(1 + 4 / ka))"
    output_type = "degree_of_dissociation"
    output_unit = None
    input_sat_maps = [["target", "ka",None]]

    def __init__(self,inputs,outputs=None):
        super(Func_Ka2Degree_of_dissociation,self).__init__(inputs,outputs)

    def run_func(self):
        if not self.sat_running():
            return False
        value=2 / (-1 + math.sqrt(1 + 4 / self.parameters[0].out_node.value))
        self.outputs[0].out_node=PU(value=value,unit=self.__class__.output_unit)
        return True

class Func_2Freezing_point_temperature(Func):

    name = "2Freezing_point_temperature"
    description = "273.15"
    output_type = "freezing_point_temperature"
    output_unit = "k"
    input_sat_maps = []

    def __init__(self,inputs,outputs=None):
        super(Func_2Freezing_point_temperature,self).__init__(inputs,outputs)

    def run_func(self):
        if not self.sat_running():
            return False
        value=273.15
        self.outputs[0].out_node=PU(value=value,unit=self.__class__.output_unit)
        return True

class Func_Gauge_pressure2Pressure(Func):

    name = "Gauge_pressure2Pressure"
    description = "gauge_pressure + ATM"
    output_type = "pressure"
    output_unit = "kpa"
    input_sat_maps = [["target", "gauge_pressure","kpa"]]

    def __init__(self,inputs,outputs=None):
        super(Func_Gauge_pressure2Pressure,self).__init__(inputs,outputs)

    def run_func(self):
        if not self.sat_running():
            return False
        value=self.parameters[0].out_node.value + ATM
        self.outputs[0].out_node=PU(value=value,unit=self.__class__.output_unit)
        return True

class Func_MassVelocity2Kinetic_energy(Func):

    name = "MassVelocity2Kinetic_energy"
    description = "mass * (velocity ** 2) * 0.5"
    output_type = "kinetic_energy"
    output_unit = "j"
    input_sat_maps = [["target", "mass","kg"], ["target", "velocity","m/s"]]

    def __init__(self,inputs,outputs=None):
        super(Func_MassVelocity2Kinetic_energy,self).__init__(inputs,outputs)

    def run_func(self):
        if not self.sat_running():
            return False
        value=self.parameters[0].out_node.value * (self.parameters[1].out_node.value ** 2) * 0.5
        self.outputs[0].out_node=PU(value=value,unit=self.__class__.output_unit)
        return True

class Func_KaMolarity2Percent_ionization(Func):

    name = "KaMolarity2Percent_ionization"
    description = "math.sqrt(ka * molarity) / molarity"
    output_type = "percent_ionization"
    output_unit = None
    input_sat_maps = [["target", "ka", None], ["target", "molarity", "mol/l"]]

    def __init__(self,inputs,outputs=None):
        super(Func_KaMolarity2Percent_ionization,self).__init__(inputs,outputs)

    def run_func(self):
        if not self.sat_running():
            return False
        value=math.sqrt(self.parameters[0].out_node.value * self.parameters[1].out_node.value) / self.parameters[1].out_node.value
        self.outputs[0].out_node=PU(value=value,unit=self.__class__.output_unit)
        return True

class Func_2Standard_atmospheric_pressure(Func):

    name = "2Standard_atmospheric_pressure"
    description = "1.0"
    output_type = "standard_atmospheric_pressure"
    output_unit = "atm"
    input_sat_maps = []

    def __init__(self,inputs,outputs=None):
        super(Func_2Standard_atmospheric_pressure,self).__init__(inputs,outputs)

    def run_func(self):
        if not self.sat_running():
            return False
        value=1.0
        self.outputs[0].out_node=PU(value=value,unit=self.__class__.output_unit)
        return True

class Func_MolalityMolar_mass2Ww(Func):

    name = "MolalityMolar_mass2W/w"
    description = "molality * molar_mass * 1e-3"
    output_type = "w/w"
    output_unit = None
    input_sat_maps = [["target", "molality", "mol/kg"], ["target", "molar_mass", "g/mol"]]

    def __init__(self,inputs,outputs=None):
        super(Func_MolalityMolar_mass2Ww,self).__init__(inputs,outputs)

    def run_func(self):
        if not self.sat_running():
            return False
        value=self.parameters[0].out_node.value * self.parameters[1].out_node.value * 1e-3
        self.outputs[0].out_node=PU(value=value,unit=None)
        return True

class Func_WwMolar_mass2Molality(Func):

    name = "W/wMolar_mass2Molality"
    description = "w/w / molar_mass / 1e-3"
    output_type = "molality"
    output_unit = "mol/kg"
    input_sat_maps = [["target", "w/w", None], ["target", "molar_mass", "g/mol"]]

    def __init__(self,inputs,outputs=None):
        super(Func_WwMolar_mass2Molality,self).__init__(inputs,outputs)

    def run_func(self):
        if not self.sat_running():
            return False
        value=self.parameters[0].out_node.value / self.parameters[1].out_node.value / 1e-3
        self.outputs[0].out_node=PU(value=value,unit=self.__class__.output_unit)
        return True


'''
Adapt By Hand from 3/20/2020
'''

'''
fx = Formula()
fx.OutputName = "massfraction"
fx.InputNames = ["InNodes", "OutNodes", "graph"]
fx.Function = Formula.MassFractionTwoNodes
rs.append(fx)
'''

class Func_MassMass2Mass_percent(Func):

    name = "MassMass2Mass_percent"
    description = "mass of node_1 / mass of node_2"
    output_type = "mass_percent"
    output_unit = None
    input_sat_maps = [["node_1", "mass","g"], ["node_2", "mass","g"]]

    def __init__(self,inputs,outputs=None):
        super(Func_MassMass2Mass_percent,self).__init__(inputs,outputs)

    def run_func(self):
        if not self.sat_running():
            return False
        value=self.parameters[0].out_node.value / self.parameters[1].out_node.value
        self.outputs[0].out_node=PU(value=value,unit=self.__class__.output_unit)
        return True