import math
from ..func_utils import Func
from domain.chemistry_utils import PU,CE,ChemicalSubstance
from parse.chemistry_parse import ParseSubstance
class Func_Ph2Kw(Func):

    name = "Ph2Kw"
    description = "10 ** (-ph * 2)"
    output_type = "kw"
    input_sat_maps = [["target", "ph"]]

    def __init__(self,inputs,outputs=None):
        super(Func_Ph2Kw,self).__init__(inputs,outputs)

    def run_func(self):
        if not self.sat_running():
            return False
        value=10 ** (-self.parameters[0].out_node.value * 2)
        self.outputs[0].out_node=PU(value=value,unit=None)
        return True

class Func_Number2Mole(Func):

    name = "Number2Mole"
    description = "number / 6.022e23"
    output_type = "mole"
    input_sat_maps = [["target", "number"]]

    def __init__(self,inputs,outputs=None):
        super(Func_Number2Mole,self).__init__(inputs,outputs)

    def run_func(self):
        if not self.sat_running():
            return False
        value=self.parameters[0].out_node.value / 6.022e23
        self.outputs[0].out_node=PU(value=value,unit=None)
        return True

class Func_Mole2Number(Func):

    name = "Mole2Number"
    description = "mole * 6.022e23"
    output_type = "number"
    input_sat_maps = [["target", "mole"]]

    def __init__(self,inputs,outputs=None):
        super(Func_Mole2Number,self).__init__(inputs,outputs)

    def run_func(self):
        if not self.sat_running():
            return False
        value=self.parameters[0].out_node.value * 6.022e23
        self.outputs[0].out_node=PU(value=value,unit=None)
        return True

class Func_MassMolar_mass2Mole(Func):

    name = "MassMolar_mass2Mole"
    description = "mass / molar_mass"
    output_type = "mole"
    input_sat_maps = [["target", "mass"], ["target", "molar_mass"]]

    def __init__(self,inputs,outputs=None):
        super(Func_MassMolar_mass2Mole,self).__init__(inputs,outputs)

    def run_func(self):
        if not self.sat_running():
            return False
        value=self.parameters[0].out_node.value / self.parameters[1].out_node.value
        self.outputs[0].out_node=PU(value=value,unit=None)
        return True

class Func_MoleMolar_mass2Mass(Func):

    name = "MoleMolar_mass2Mass"
    description = "mole * molar_mass"
    output_type = "mass"
    input_sat_maps = [["target", "mole"], ["target", "molar_mass"]]

    def __init__(self,inputs,outputs=None):
        super(Func_MoleMolar_mass2Mass,self).__init__(inputs,outputs)

    def run_func(self):
        if not self.sat_running():
            return False
        value=self.parameters[0].out_node.value * self.parameters[1].out_node.value
        self.outputs[0].out_node=PU(value=value,unit=None)
        return True

class Func_VolumeMolarity2Mole(Func):

    name = "VolumeMolarity2Mole"
    description = "volume * 1.0 * molarity"
    output_type = "mole"
    input_sat_maps = [["target", "volume"], ["target", "molarity"]]

    def __init__(self,inputs,outputs=None):
        super(Func_VolumeMolarity2Mole,self).__init__(inputs,outputs)

    def run_func(self):
        if not self.sat_running():
            return False
        value=self.parameters[0].out_node.value * 1.0 * self.parameters[1].out_node.value
        self.outputs[0].out_node=PU(value=value,unit=None)
        return True

class Func_VolumeMoleTemperature2Pressure(Func):

    name = "VolumeMoleTemperature2Pressure"
    description = "mole * temperature * 0.082 / volume"
    output_type = "pressure"
    input_sat_maps = [["target", "volume"], ["target", "mole"], ["target", "temperature"]]

    def __init__(self,inputs,outputs=None):
        super(Func_VolumeMoleTemperature2Pressure,self).__init__(inputs,outputs)

    def run_func(self):
        if not self.sat_running():
            return False
        value=self.parameters[1].out_node.value * self.parameters[2].out_node.value * 0.082 / self.parameters[0].out_node.value
        self.outputs[0].out_node=PU(value=value,unit=None)
        return True

class Func_VolumeTemperaturePressure2Mole(Func):

    name = "VolumeTemperaturePressure2Mole"
    description = "pressure * volume / (temperature * 0.082)"
    output_type = "mole"
    input_sat_maps = [["target", "volume"], ["target", "temperature"], ["target", "pressure"]]

    def __init__(self,inputs,outputs=None):
        super(Func_VolumeTemperaturePressure2Mole,self).__init__(inputs,outputs)

    def run_func(self):
        if not self.sat_running():
            return False
        value=self.parameters[2].out_node.value * self.parameters[0].out_node.value / (self.parameters[1].out_node.value * 0.082)
        self.outputs[0].out_node=PU(value=value,unit=None)
        return True

class Func_PressureMolar_massTemperature2Density(Func):

    name = "PressureMolar_massTemperature2Density"
    description = "pressure * molar_mass / (temperature * 0.082)"
    output_type = "density"
    input_sat_maps = [["target", "pressure"], ["target", "molar_mass"], ["target", "temperature"]]

    def __init__(self,inputs,outputs=None):
        super(Func_PressureMolar_massTemperature2Density,self).__init__(inputs,outputs)

    def run_func(self):
        if not self.sat_running():
            return False
        value=self.parameters[0].out_node.value * self.parameters[1].out_node.value / (self.parameters[2].out_node.value * 0.082)
        self.outputs[0].out_node=PU(value=value,unit=None)
        return True

class Func_PressureDensityTemperature2Molar_mass(Func):

    name = "PressureDensityTemperature2Molar_mass"
    description = "density * temperature * 0.082 / pressure"
    output_type = "molar_mass"
    input_sat_maps = [["target", "pressure"], ["target", "density"], ["target", "temperature"]]

    def __init__(self,inputs,outputs=None):
        super(Func_PressureDensityTemperature2Molar_mass,self).__init__(inputs,outputs)

    def run_func(self):
        if not self.sat_running():
            return False
        value=self.parameters[1].out_node.value * self.parameters[2].out_node.value * 0.082 / self.parameters[0].out_node.value
        self.outputs[0].out_node=PU(value=value,unit=None)
        return True

class Func_MoleMass2Molar_mass(Func):

    name = "MoleMass2Molar_mass"
    description = "mass / mole"
    output_type = "molar_mass"
    input_sat_maps = [["target", "mole"], ["target", "mass"]]

    def __init__(self,inputs,outputs=None):
        super(Func_MoleMass2Molar_mass,self).__init__(inputs,outputs)

    def run_func(self):
        if not self.sat_running():
            return False
        value=self.parameters[1].out_node.value / self.parameters[0].out_node.value
        self.outputs[0].out_node=PU(value=value,unit=None)
        return True

class Func_MoleVolumePressure2Temperature(Func):

    name = "MoleVolumePressure2Temperature"
    description = "pressure * volume / (mole * 0.082)"
    output_type = "temperature"
    input_sat_maps = [["target", "mole"], ["target", "volume"], ["target", "pressure"]]

    def __init__(self,inputs,outputs=None):
        super(Func_MoleVolumePressure2Temperature,self).__init__(inputs,outputs)

    def run_func(self):
        if not self.sat_running():
            return False
        value=self.parameters[2].out_node.value * self.parameters[1].out_node.value / (self.parameters[0].out_node.value * 0.082)
        self.outputs[0].out_node=PU(value=value,unit=None)
        return True

class Func_MoleTemperaturePressure2Volume(Func):

    name = "MoleTemperaturePressure2Volume"
    description = "mole * 0.082 * temperature / pressure"
    output_type = "volume"
    input_sat_maps = [["target", "mole"], ["target", "temperature"], ["target", "pressure"]]

    def __init__(self,inputs,outputs=None):
        super(Func_MoleTemperaturePressure2Volume,self).__init__(inputs,outputs)

    def run_func(self):
        if not self.sat_running():
            return False
        value=self.parameters[0].out_node.value * 0.082 * self.parameters[1].out_node.value / self.parameters[2].out_node.value
        self.outputs[0].out_node=PU(value=value,unit=None)
        return True

class Func_MoleVolume2Molarity(Func):

    name = "MoleVolume2Molarity"
    description = "mole / volume"
    output_type = "molarity"
    input_sat_maps = [["target", "mole"], ["target", "volume"]]

    def __init__(self,inputs,outputs=None):
        super(Func_MoleVolume2Molarity,self).__init__(inputs,outputs)

    def run_func(self):
        if not self.sat_running():
            return False
        value=self.parameters[0].out_node.value / self.parameters[1].out_node.value
        self.outputs[0].out_node=PU(value=value,unit=None)
        return True

class Func_MolarityVolume2Mole(Func):

    name = "MolarityVolume2Mole"
    description = "molarity * volume"
    output_type = "mole"
    input_sat_maps = [["target", "molarity"], ["target", "volume"]]

    def __init__(self,inputs,outputs=None):
        super(Func_MolarityVolume2Mole,self).__init__(inputs,outputs)

    def run_func(self):
        if not self.sat_running():
            return False
        value=self.parameters[0].out_node.value * self.parameters[1].out_node.value
        self.outputs[0].out_node=PU(value=value,unit=None)
        return True

class Func_MoleMolarity2Volume(Func):

    name = "MoleMolarity2Volume"
    description = "mole / molarity"
    output_type = "volume"
    input_sat_maps = [["target", "mole"], ["target", "molarity"]]

    def __init__(self,inputs,outputs=None):
        super(Func_MoleMolarity2Volume,self).__init__(inputs,outputs)

    def run_func(self):
        if not self.sat_running():
            return False
        value=self.parameters[0].out_node.value / self.parameters[1].out_node.value
        self.outputs[0].out_node=PU(value=value,unit=None)
        return True

class Func_Ph2Acid_concentration(Func):

    name = "Ph2Acid_concentration"
    description = "10 ** (-ph)"
    output_type = "acid_concentration"
    input_sat_maps = [["target", "ph"]]

    def __init__(self,inputs,outputs=None):
        super(Func_Ph2Acid_concentration,self).__init__(inputs,outputs)

    def run_func(self):
        if not self.sat_running():
            return False
        value=10 ** (-self.parameters[0].out_node.value)
        self.outputs[0].out_node=PU(value=value,unit=None)
        return True

class Func_Acid_concentration2Ph(Func):

    name = "Acid_concentration2Ph"
    description = "-math.log10(acid_concentration)"
    output_type = "ph"
    input_sat_maps = [["target", "acid_concentration"]]

    def __init__(self,inputs,outputs=None):
        super(Func_Acid_concentration2Ph,self).__init__(inputs,outputs)

    def run_func(self):
        if not self.sat_running():
            return False
        value=-math.log10(self.parameters[0].out_node.value)
        self.outputs[0].out_node=PU(value=value,unit=None)
        return True

class Func_Ph2Poh(Func):

    name = "Ph2Poh"
    description = "14 - ph"
    output_type = "poh"
    input_sat_maps = [["target", "ph"]]

    def __init__(self,inputs,outputs=None):
        super(Func_Ph2Poh,self).__init__(inputs,outputs)

    def run_func(self):
        if not self.sat_running():
            return False
        value=14 - self.parameters[0].out_node.value
        self.outputs[0].out_node=PU(value=value,unit=None)
        return True

class Func_Poh2Ph(Func):

    name = "Poh2Ph"
    description = "14 - poh"
    output_type = "ph"
    input_sat_maps = [["target", "poh"]]

    def __init__(self,inputs,outputs=None):
        super(Func_Poh2Ph,self).__init__(inputs,outputs)

    def run_func(self):
        if not self.sat_running():
            return False
        value=14 - self.parameters[0].out_node.value
        self.outputs[0].out_node=PU(value=value,unit=None)
        return True

class Func_Ka2Pka(Func):

    name = "Ka2Pka"
    description = "-math.log10(ka)"
    output_type = "pka"
    input_sat_maps = [["target", "ka"]]

    def __init__(self,inputs,outputs=None):
        super(Func_Ka2Pka,self).__init__(inputs,outputs)

    def run_func(self):
        if not self.sat_running():
            return False
        value=-math.log10(self.parameters[0].out_node.value)
        self.outputs[0].out_node=PU(value=value,unit=None)
        return True

class Func_Mass_concentrationMolar_mass2Molarity(Func):

    name = "Mass_concentrationMolar_mass2Molarity"
    description = "mass_concentration * 100 / molar_mass / 0.1"
    output_type = "molarity"
    input_sat_maps = [["target", "mass_concentration"], ["target", "molar_mass"]]

    def __init__(self,inputs,outputs=None):
        super(Func_Mass_concentrationMolar_mass2Molarity,self).__init__(inputs,outputs)

    def run_func(self):
        if not self.sat_running():
            return False
        value=self.parameters[0].out_node.value * 100 / self.parameters[1].out_node.value / 0.1
        self.outputs[0].out_node=PU(value=value,unit=None)
        return True

class Func_MassVolume2Density(Func):

    name = "MassVolume2Density"
    description = "mass * 1.0 / volume"
    output_type = "density"
    input_sat_maps = [["target", "mass"], ["target", "volume"]]

    def __init__(self,inputs,outputs=None):
        super(Func_MassVolume2Density,self).__init__(inputs,outputs)

    def run_func(self):
        if not self.sat_running():
            return False
        value=self.parameters[0].out_node.value * 1.0 / self.parameters[1].out_node.value
        self.outputs[0].out_node=PU(value=value,unit=None)
        return True

class Func_DensityVolume2Mass(Func):

    name = "DensityVolume2Mass"
    description = "density * volume"
    output_type = "mass"
    input_sat_maps = [["target", "density"], ["target", "volume"]]

    def __init__(self,inputs,outputs=None):
        super(Func_DensityVolume2Mass,self).__init__(inputs,outputs)

    def run_func(self):
        if not self.sat_running():
            return False
        value=self.parameters[0].out_node.value * self.parameters[1].out_node.value
        self.outputs[0].out_node=PU(value=value,unit=None)
        return True

class Func_MassDensity2Volume(Func):

    name = "MassDensity2Volume"
    description = "mass * 1.0 / density"
    output_type = "volume"
    input_sat_maps = [["target", "mass"], ["target", "density"]]

    def __init__(self,inputs,outputs=None):
        super(Func_MassDensity2Volume,self).__init__(inputs,outputs)

    def run_func(self):
        if not self.sat_running():
            return False
        value=self.parameters[0].out_node.value * 1.0 / self.parameters[1].out_node.value
        self.outputs[0].out_node=PU(value=value,unit=None)
        return True

class Func_MolarityMolar_mass2Molality(Func):

    name = "MolarityMolar_mass2Molality"
    description = "molarity * 1000 / (1000 - molarity * molar_mass)"
    output_type = "molality"
    input_sat_maps = [["target", "molarity"], ["target", "molar_mass"]]

    def __init__(self,inputs,outputs=None):
        super(Func_MolarityMolar_mass2Molality,self).__init__(inputs,outputs)

    def run_func(self):
        if not self.sat_running():
            return False
        value=self.parameters[0].out_node.value * 1000 / (1000 - self.parameters[0].out_node.value * self.parameters[1].out_node.value)
        self.outputs[0].out_node=PU(value=value,unit=None)
        return True

class Func_MolalityMolar_mass2Molarity(Func):

    name = "MolalityMolar_mass2Molarity"
    description = "molality * 1000 / (1000 + molality * molar_mass)"
    output_type = "molarity"
    input_sat_maps = [["target", "molality"], ["target", "molar_mass"]]

    def __init__(self,inputs,outputs=None):
        super(Func_MolalityMolar_mass2Molarity,self).__init__(inputs,outputs)

    def run_func(self):
        if not self.sat_running():
            return False
        value=self.parameters[0].out_node.value * 1000 / (1000 + self.parameters[0].out_node.value * self.parameters[1].out_node.value)
        self.outputs[0].out_node=PU(value=value,unit=None)
        return True

class Func_MolarityTemperature2Osmolarity(Func):

    name = "MolarityTemperature2Osmolarity"
    description = "molarity * temperature * 8.31 / 101.325"
    output_type = "osmolarity"
    input_sat_maps = [["target", "molarity"], ["target", "temperature"]]

    def __init__(self,inputs,outputs=None):
        super(Func_MolarityTemperature2Osmolarity,self).__init__(inputs,outputs)

    def run_func(self):
        if not self.sat_running():
            return False
        value=self.parameters[0].out_node.value * self.parameters[1].out_node.value * 8.31 / 101.325
        self.outputs[0].out_node=PU(value=value,unit=None)
        return True

class Func_Theoretical_yieldPercent_yield2Actual_yield(Func):

    name = "Theoretical_yieldPercent_yield2Actual_yield"
    description = "theoretical_yield * percent_yield"
    output_type = "actual_yield"
    input_sat_maps = [["target", "theoretical_yield"], ["target", "percent_yield"]]

    def __init__(self,inputs,outputs=None):
        super(Func_Theoretical_yieldPercent_yield2Actual_yield,self).__init__(inputs,outputs)

    def run_func(self):
        if not self.sat_running():
            return False
        value=self.parameters[0].out_node.value * self.parameters[1].out_node.value
        self.outputs[0].out_node=PU(value=value,unit=None)
        return True

class Func_Actual_yieldPercent_yield2Theoretical_yield(Func):

    name = "Actual_yieldPercent_yield2Theoretical_yield"
    description = "actual_yield * 1.0 / percent_yield"
    output_type = "theoretical_yield"
    input_sat_maps = [["target", "actual_yield"], ["target", "percent_yield"]]

    def __init__(self,inputs,outputs=None):
        super(Func_Actual_yieldPercent_yield2Theoretical_yield,self).__init__(inputs,outputs)

    def run_func(self):
        if not self.sat_running():
            return False
        value=self.parameters[0].out_node.value * 1.0 / self.parameters[1].out_node.value
        self.outputs[0].out_node=PU(value=value,unit=None)
        return True

class Func_Theoretical_yieldActual_yield2Percent_yield(Func):

    name = "Theoretical_yieldActual_yield2Percent_yield"
    description = "actual_yield * 1.0 / theoretical_yield"
    output_type = "percent_yield"
    input_sat_maps = [["target", "theoretical_yield"], ["target", "actual_yield"]]

    def __init__(self,inputs,outputs=None):
        super(Func_Theoretical_yieldActual_yield2Percent_yield,self).__init__(inputs,outputs)

    def run_func(self):
        if not self.sat_running():
            return False
        value=self.parameters[1].out_node.value * 1.0 / self.parameters[0].out_node.value
        self.outputs[0].out_node=PU(value=value,unit=None)
        return True

class Func_Ka2Degree_of_dissociation(Func):

    name = "Ka2Degree_of_dissociation"
    description = "2 / (-1 + math.sqrt(1 + 4 / ka))"
    output_type = "degree_of_dissociation"
    input_sat_maps = [["target", "ka"]]

    def __init__(self,inputs,outputs=None):
        super(Func_Ka2Degree_of_dissociation,self).__init__(inputs,outputs)

    def run_func(self):
        if not self.sat_running():
            return False
        value=2 / (-1 + math.sqrt(1 + 4 / self.parameters[0].out_node.value))
        self.outputs[0].out_node=PU(value=value,unit=None)
        return True

class Func_2Freezing_point_temperature(Func):

    name = "2Freezing_point_temperature"
    description = "273.15"
    output_type = "freezing_point_temperature"
    input_sat_maps = []

    def __init__(self,inputs,outputs=None):
        super(Func_2Freezing_point_temperature,self).__init__(inputs,outputs)

    def run_func(self):
        if not self.sat_running():
            return False
        value=273.15
        self.outputs[0].out_node=PU(value=value,unit=None)
        return True

class Func_Gauge_pressure2Pressure(Func):

    name = "Gauge_pressure2Pressure"
    description = "gauge_pressure + 100"
    output_type = "pressure"
    input_sat_maps = [["target", "gauge_pressure"]]

    def __init__(self,inputs,outputs=None):
        super(Func_Gauge_pressure2Pressure,self).__init__(inputs,outputs)

    def run_func(self):
        if not self.sat_running():
            return False
        value=self.parameters[0].out_node.value + 100
        self.outputs[0].out_node=PU(value=value,unit=None)
        return True

class Func_MassVelocity2Kinetic_energy(Func):

    name = "MassVelocity2Kinetic_energy"
    description = "mass * (velocity ** 2) * 0.5"
    output_type = "kinetic_energy"
    input_sat_maps = [["target", "mass"], ["target", "velocity"]]

    def __init__(self,inputs,outputs=None):
        super(Func_MassVelocity2Kinetic_energy,self).__init__(inputs,outputs)

    def run_func(self):
        if not self.sat_running():
            return False
        value=self.parameters[0].out_node.value * (self.parameters[1].out_node.value ** 2) * 0.5
        self.outputs[0].out_node=PU(value=value,unit=None)
        return True

class Func_KaMolarity2Percent_ionization(Func):

    name = "KaMolarity2Percent_ionization"
    description = "math.sqrt(ka * molarity) / molarity"
    output_type = "percent_ionization"
    input_sat_maps = [["target", "ka"], ["target", "molarity"]]

    def __init__(self,inputs,outputs=None):
        super(Func_KaMolarity2Percent_ionization,self).__init__(inputs,outputs)

    def run_func(self):
        if not self.sat_running():
            return False
        value=math.sqrt(self.parameters[0].out_node.value * self.parameters[1].out_node.value) / self.parameters[1].out_node.value
        self.outputs[0].out_node=PU(value=value,unit=None)
        return True

class Func_2Standard_atmospheric_pressure(Func):

    name = "2Standard_atmospheric_pressure"
    description = "1.0"
    output_type = "standard_atmospheric_pressure"
    input_sat_maps = []

    def __init__(self,inputs,outputs=None):
        super(Func_2Standard_atmospheric_pressure,self).__init__(inputs,outputs)

    def run_func(self):
        if not self.sat_running():
            return False
        value=1.0
        self.outputs[0].out_node=PU(value=value,unit=None)
        return True

class Func_MolalityMolar_mass2W/w(Func):

    name = "MolalityMolar_mass2W/w"
    description = "molality * molar_mass * 0.1"
    output_type = "w/w"
    input_sat_maps = [["target", "molality"], ["target", "molar_mass"]]

    def __init__(self,inputs,outputs=None):
        super(Func_MolalityMolar_mass2W/w,self).__init__(inputs,outputs)

    def run_func(self):
        if not self.sat_running():
            return False
        value=self.parameters[0].out_node.value * self.parameters[1].out_node.value * 0.1
        self.outputs[0].out_node=PU(value=value,unit=None)
        return True

class Func_W/wMolar_mass2Molality(Func):

    name = "W/wMolar_mass2Molality"
    description = "w/w / molar_mass / 0.1"
    output_type = "molality"
    input_sat_maps = [["target", "w/w"], ["target", "molar_mass"]]

    def __init__(self,inputs,outputs=None):
        super(Func_W/wMolar_mass2Molality,self).__init__(inputs,outputs)

    def run_func(self):
        if not self.sat_running():
            return False
        value=self.parameters[0].out_node.value / self.parameters[1].out_node.value / 0.1
        self.outputs[0].out_node=PU(value=value,unit=None)
        return True

