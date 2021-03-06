fx = Formula()
fx.OutputName = "mass_percent"
fx.InputNames = ["InNodes", "OutNodes", "graph"]
fx.Function = Formula.mass_percentTwoNodes
rs.append(fx)

fx = Formula()
fx.OutputName = "mole_percent"
fx.InputNames = ["InNodes", "OutNodes", "graph"]
fx.Function = Formula.mole_percentTwoNodes
rs.append(fx)

fx = Formula()
fx.OutputName = 'molarity_percent'
fx.InputNames = ['InNodes', 'OutNodes', 'graph']
fx.Function = Formula.MolarityFractionTwoNodes
rs.append(fx)

fx = Formula()
fx.OutputName = "equilibrium_constant_k"
fx.InputNames = ["equation", "graph"]
fx.Function = Formula.EquationKWithMolarity
rs.append(fx)

fx = Formula()
fx.OutputName = "equilibrium_constant_k"
fx.InputNames = ["equation", "graph", "volume"]
fx.Function = Formula.EquationK
rs.append(fx)

fx = Formula()
fx.OutputName = "actual_yield"
fx.InputNames = ["equation", "graph", "theoretical_yield", "percent_yield"]
fx.Function = lambda dbList: dbList[2] * dbList[3]
rs.append(fx)

fx = Formula()
fx.OutputName = "theoretical_yield"
fx.InputNames = ["equation", "graph", "actual_yield", "percent_yield"]
fx.Function = lambda dbList: dbList[2] * 1.0 / dbList[3]
rs.append(fx)

fx = Formula()
fx.OutputName = "percent_yield"
fx.InputNames = ["equation", "graph", "theoretical_yield", "actual_yield"]
fx.Function = lambda dbList: dbList[2] * 1.0 / dbList[3]
rs.append(fx)

fx = Formula()
fx.OutputName = "avogadroconstant"
fx.InputNames = ["equation", "graph"]
fx.Function = lambda *dbList: 6.023e23
rs.append(fx)

fx = Formula()
fx.OutputName = "coefficient"
fx.InputNames = ["equation", "graph", "molecule"]
fx.Function = lambda dbList: Formula.GetCoefficient(dbList[0], dbList[2])
rs.append(fx)

fx = Formula()
fx.OutputName = "freezing_point_temperature"
fx.InputNames = ["equation", "graph"]
fx.Function = lambda dbList: 273.15
rs.append(fx)

fx = Formula()
fx.OutputName = 'kw'
fx.InputNames = ['ph']
fx.Function = lambda dbList: 10 ** (-dbList[0] * 2)
rs.append(fx)

fx = Formula()
fx.OutputName = 'standard_enthalpy'
fx.InputNames = ['equation', 'graph']
fx.Function = Formula.StandardEnthalpy
rs.append(fx)

fx = Formula()
fx.OutputName = 'standard_atmospheric_pressure'
fx.InputNames = ['molecule']
fx.Function = lambda dbList: 1.0
rs.append(fx)

fx = Formula()
fx.OutputName = "mole"
fx.InputNames = ["number"]
fx.Function = lambda params: params[0] / 6.022e23
rs.append(fx)

fx = Formula()
fx.OutputName = "number"
fx.InputNames = ["mole"]
fx.Function = lambda params: params[0] * 6.022e23
rs.append(fx)

fx = Formula()
fx.OutputName = "mole"
fx.InputNames = ["mass", "molar_mass"]
fx.Function = lambda params: params[0] / params[1]
rs.append(fx)

fx = Formula()
fx.OutputName = "mass"
fx.InputNames = ["mole", "molar_mass"]
fx.Function = lambda params: params[0] * params[1]
rs.append(fx)

fx = Formula()
fx.OutputName = "mole"
fx.InputNames = ["volume", "molarity"]
fx.Function = lambda params: params[0] * 1.0 * params[1]
rs.append(fx)

fx = Formula()
fx.OutputName = "pressure"
fx.InputNames = ["volume", "mole", "temperature"]
fx.Function = lambda params: params[1] * params[2] * 0.082 / params[0]
rs.append(fx)

fx = Formula()
fx.OutputName = "mole"
fx.InputNames = ["volume", "temperature", "pressure"]
fx.Function = lambda dbList: dbList[2] * dbList[0] / (dbList[1] * 0.082)
rs.append(fx)
# pM = tho * R * T

fx = Formula()
fx.OutputName = 'density'
fx.InputNames = ['pressure', 'molar_mass', 'temperature']
fx.Function = lambda dbList: dbList[0] * dbList[1] / (dbList[2] * 0.082)
rs.append(fx)

fx = Formula()
fx.OutputName = 'molar_mass'
fx.InputNames = ['pressure', 'density', 'temperature']
fx.Function = lambda dbList: dbList[1] * dbList[2] * 0.082 / dbList[0]
rs.append(fx)

fx = Formula()
fx.OutputName = 'molar_mass'
fx.InputNames = ['mole', 'mass']
fx.Function = lambda dbList: dbList[1] / dbList[0]
rs.append(fx)

fx = Formula()
fx.OutputName = "temperature"
fx.InputNames = ["mole", "volume", "pressure"]
fx.Function = lambda dbList: dbList[2] * dbList[1] / (dbList[0] * 0.082)
rs.append(fx)

fx = Formula()
fx.OutputName = "volume"
fx.InputNames = ["mole", "temperature", "pressure"]
fx.Function = lambda dbList: dbList[0] * 0.082 * dbList[1] / dbList[2]
rs.append(fx)

fx = Formula()
fx.OutputName = "molarity"
fx.InputNames = ["mole", "volume"]
fx.Function = lambda dbList: dbList[0] / dbList[1]
rs.append(fx)

fx = Formula()
fx.OutputName = 'mole'
fx.InputNames = ['molarity', 'volume']
fx.Function = lambda dbList: dbList[0] * dbList[1]
rs.append(fx)

fx = Formula()
fx.OutputName = 'volume'
fx.InputNames = ['mole', 'molarity']
fx.Function = lambda dbList: dbList[0] / dbList[1]
rs.append(fx)

fx = Formula()
fx.OutputName = "acid concentration"
fx.InputNames = ["ph"]
fx.Function = lambda dbList: 10 ** (-dbList[0])
rs.append(fx)

fx = Formula()
fx.OutputName = "ph"
fx.InputNames = ["acid concentration"]
fx.Function = lambda dbList: -math.log10(dbList[0])
rs.append(fx)

fx = Formula()
fx.OutputName = 'alkali concentration'
fx.InputNames = ['poh']
fx.Function = lambda dbList: 10 ** (-dbList[0])
rs.append(fx)

fx = Formula()
fx.OutputName = "poh"
fx.InputNames = ["ph"]
fx.Function = lambda dbList: 14 - dbList[0]
rs.append(fx)

fx = Formula()
fx.OutputName = "ph"
fx.InputNames = ["poh"]
fx.Function = lambda dblist: 14 - dblist[0]
rs.append(fx)

fx = Formula()
fx.OutputName = "pka"
fx.InputNames = ["ka"]
fx.Function = lambda dbList: -math.log10(dbList[0])
rs.append(fx)

fx = Formula()
fx.OutputName = "molarity"
fx.InputNames = ["w/v", "molar_mass"]
fx.Function = lambda dbList: dbList[0] * 100 / dbList[1] / 0.1
rs.append(fx)

fx = Formula()
fx.OutputName = "atom mole in molecule"
fx.InputNames = ["atom", "molecule", "mole"]
fx.Function = Formula.CalcAtomMole
rs.append(fx)

fx = Formula()
fx.OutputName = "atom mass in molecule"
fx.InputNames = ["atom", "molecule", "mole"]
fx.Function = Formula.CalcAtomMass
rs.append(fx)

fx = Formula()
fx.OutputName = "atom number in molecule"
fx.InputNames = ["atom", "molecule", "mole"]
fx.Function = Formula.CalcAtomNumber
rs.append(fx)

fx = Formula()
fx.OutputName = "atom number in molecule"
fx.InputNames = ["atom", "molecule"]
fx.Function = Formula.CalcAtomNumberSimple
rs.append(fx)

fx = Formula()
fx.OutputName = "atom oxidation number"
fx.InputNames = ["atom", "molecule"]
fx.Function = Formula.CalcAtomOxidationNumber
rs.append(fx)

fx = Formula()
fx.OutputName = "density",
fx.InputNames = ["mass", "volume"]
fx.Function = lambda dbList: dbList[0] * 1.0 / dbList[1]
rs.append(fx)

fx = Formula()
fx.OutputName = "mass",
fx.InputNames = ["density", "volume"]
fx.Function = lambda dbList: dbList[0] * dbList[1]
rs.append(fx)

fx = Formula()
fx.OutputName = "volume",
fx.InputNames = ["mass", "density"]
fx.Function = lambda dbList: dbList[0] * 1.0 / dbList[1]
rs.append(fx)

# E = m * C * dT, kg,kj, K,

fx = Formula()
fx.OutputName = "energy"
fx.InputNames = ["mass", "shc", "dt"]
fx.Function = lambda dbList: dbList[0] * dbList[1] * dbList[2]
rs.append(fx)

fx = Formula()
fx.OutputName = "mass"
fx.InputNames = ["energy", "shc", "dt"]
fx.Function = lambda dbList: dbList[0] / dbList[1] / dbList[2]
rs.append(fx)

fx = Formula()
fx.OutputName = "shc"
fx.InputNames = ["energy", "mass", "dt"]
fx.Function = lambda dbList: dbList[0] / dbList[1] / dbList[2]
rs.append(fx)

fx = Formula()
fx.OutputName = "dt"
fx.InputNames = ["energy", "mass", "shc"]
fx.Function = lambda dbList: dbList[0] / dbList[1] / dbList[2]
rs.append(fx)

# molality and molarity
fx = Formula()
fx.OutputName = "molality"
fx.InputNames = ["molarity", "molar_mass"]
fx.Function = lambda dbList: dbList[0] * 1000 / (1000 - dbList[0] * dbList[1])
rs.append(fx)

fx = Formula()
fx.OutputName = "molarity"
fx.InputNames = ["molality", "molar_mass"]
fx.Function = lambda dbList: dbList[0] * 1000 / (1000 + dbList[0] * dbList[1])
rs.append(fx)

# mass concentration
fx = Formula()
fx.OutputName = "massconcentration"
fx.InputNames = ["mass", "volume"]
fx.Function = lambda dbList: dbList[0] / dbList[1]
rs.append(fx)

# osmolarity
fx = Formula()
fx.OutputName = "osmolarity"
fx.InputNames = ["molarity", "temperature"]
fx.Function = lambda dbList: dbList[0] * dbList[1] * 8.31 / 101.325
rs.append(fx)

# actual_yield
fx = Formula()
fx.OutputName = "actual_yield"
fx.InputNames = ["theoretical_yield", "percent_yield"]
fx.Function = lambda dbList: dbList[0] * dbList[1]
rs.append(fx)

fx = Formula()
fx.OutputName = "theoretical_yield"
fx.InputNames = ["actual_yield", "percent_yield"]
fx.Function = lambda dbList: dbList[0] * 1.0 / dbList[1]
rs.append(fx)

fx = Formula()
fx.OutputName = "percent_yield"
fx.InputNames = ["theoretical_yield", "actual_yield"]
fx.Function = lambda dbList: dbList[1] * 1.0 / dbList[0]
rs.append(fx)

fx = Formula()
fx.OutputName = "avogadroconstant"
fx.InputNames = ["molecule"]
fx.Function = lambda *dbList: 6.023e23
rs.append(fx)

fx = Formula()
fx.OutputName = "boiling_point_temperature2"
fx.InputNames = ["boiling_point_temperature1", "hvap", "vapor_pressure1", "vapor_pressure2"]
fx.Function = lambda dbList: 1.0 / (1.0 / dbList[0] - 8.314 / dbList[1] * math.log(dbList[3] / dbList[2]))
rs.append(fx)

fx = Formula()
fx.OutputName = "vapor_pressure2"
fx.InputNames = ["boiling_point_temperature1", "hvap", "vapor_pressure1", "boiling_point_temperature2"]
fx.Function = lambda dbList: dbList[2] * math.e ** (-dbList[1] / 8.314 * (1.0 / dbList[3] - 1.0 / dbList[0]))
rs.append(fx)

fx = Formula()
fx.OutputName = "hvap"
fx.InputNames = ["vapor_pressure1", "vapor_pressure2", "boiling_point_temperature1", "boiling_point_temperature2"]
fx.Function = lambda dbList: math.log(dbList[1] / dbList[0]) * (-8.314) / (1 / dbList[3] - 1 / dbList[2])
rs.append(fx)

fx = Formula()
fx.OutputName = "degree_of_dissociation"
fx.InputNames = ["ka"]
fx.Function = lambda dbList: 2 / (-1 + math.sqrt(1 + 4 / dbList[0]))
rs.append(fx)

fx = Formula()
fx.OutputName = "freezing_point_temperature"
fx.InputNames = []
fx.Function = lambda *dbList: 273.15
rs.append(fx)

fx = Formula()
fx.OutputName = "ka"
fx.InputNames = ["molarity_h", "molarity_a", "molarity_ha"]
fx.Function = lambda dbList: dbList[0] * dbList[1] / dbList[2]
rs.append(fx)

fx = Formula()
fx.OutputName = "kb"
fx.InputNames = ["molarity_oh", "molarity_a", "molarity_aoh"]
fx.Function = lambda dbList: dbList[0] * dbList[1] / dbList[2]
rs.append(fx)

fx = Formula()
fx.OutputName = "osmolarity"
fx.InputNames = ["molarity", "molecule"]
fx.Function = lambda dbList: dbList[0] * Utils.Utils.CalcOSCoefficient(dbList[1])
rs.append(fx)

fx = Formula()
fx.OutputName = 'absorptivity'
fx.InputNames = ['molarity', 'depth', 'absorbance']
fx.Function = lambda dbList: dbList[2] / dbList[0] / dbList[1]
rs.append(fx)

fx = Formula()
fx.OutputName = 'transmittance'
fx.InputNames = ['absorbance']
fx.Function = lambda dbList: (10 ** (2 - dbList[0])) / 100
rs.append(fx)

fx = Formula()
fx.OutputName = 'absorbance'
fx.InputNames = ['molarity', 'depth', 'absorptivity']
fx.Function = lambda dbList: dbList[0] * dbList[1] * dbList[2]
rs.append(fx)

fx = Formula()
fx.OutputName = 'depth'
fx.InputNames = ['absorbance', 'molarity', 'absorptivity']
fx.Function = lambda dbList: dbList[0] / dbList[1] / dbList[2]
rs.append(fx)

fx = Formula()
fx.OutputName = 'diameter'
fx.InputNames = ['circumference']
fx.Function = lambda dbList: dbList[0] / math.pi
rs.append(fx)

fx = Formula()
fx.OutputName = 'dilution_factor'
fx.InputNames = ['initial_volume', 'final_volume']
fx.Function = lambda dbList: dbList[1] / dbList[0]
rs.append(fx)

fx = Formula()
fx.OutputName = 'electric_current'
fx.InputNames = ['resistance', 'voltage']
fx.Function = lambda dbList: dbList[1] / dbList[0]
rs.append(fx)

fx = Formula()
fx.OutputName = 'resistance'
fx.InputNames = ['electric_current', 'voltage']
fx.Function = lambda dbList: dbList[1] / dbList[0]
rs.append(fx)

fx = Formula()
fx.OutputName = 'voltage'
fx.InputNames = ['electric_current', 'resistance']
fx.Function = lambda dbList: dbList[0] * dbList[1]
rs.append(fx)

fx = Formula()
fx.OutputName = 'gauge_pressure'
fx.InputNames = ['density', 'height']
fx.Function = lambda dbList: dbList[0] * dbList[1] * 9.8 / 1e5
rs.append(fx)

fx = Formula()
fx.OutputName = 'pressure'
fx.InputNames = ['gauge_pressure']
fx.Function = lambda dbList: dbList[0] + 100
rs.append(fx)

fx = Formula()
fx.OutputName = 'half-life'
fx.InputNames = ['mass0', 'mass1', 'time']
fx.Function = lambda dbList: dbList[2] / (math.log(dbList[1] / dbList[0], 0.5))
rs.append(fx)

fx = Formula()
fx.OutputName = 'kinetic_energy'
fx.InputNames = ['mass', 'velocity']
fx.Function = lambda dbList: dbList[0] * (dbList[1] ** 2) * 0.5
rs.append(fx)

fx = Formula()
fx.OutputName = 'melted_time'
fx.InputNames = ['heat_of_fusion', 'mole', 'power']
fx.Function = lambda dbList: dbList[0] * dbList[1] / dbList[2]
rs.append(fx)

fx = Formula()
fx.OutputName = 'molar_heat'
fx.InputNames = ['shc', 'molar_mass']
fx.Function = lambda dbList: dbList[0] * dbList[1]
rs.append(fx)

fx = Formula()
fx.OutputName = 'percent_ionization'
fx.InputNames = ['ka', 'molarity']
fx.Function = lambda dbList: math.sqrt(dbList[0] * dbList[1]) / dbList[1]
rs.append(fx)

fx = Formula()
fx.OutputName = 'radius'
fx.InputNames = ['circumference']
fx.Function = lambda dbList: dbList[0] / (2 * math.pi)
rs.append(fx)

fx = Formula()
fx.OutputName = 'standard_atmospheric_pressure'
fx.InputNames = []
fx.Function = lambda dbList: 1.0
rs.append(fx)

fx = Formula()
fx.OutputName = 'w/w'
fx.InputNames = ['molality', 'molar_mass']
fx.Function = lambda dbList: dbList[0] * dbList[1] * 0.1
rs.append(fx)

fx = Formula()
fx.OutputName = 'molality'
fx.InputNames = ['w/w', 'molar_mass']
fx.Function = lambda dbList: dbList[0] / dbList[1] / 0.1
rs.append(fx)

fx = Formula()
fx.OutputName = 'ph'
fx.InputNames = ['molecule', 'molarity']
fx.Function = Formula.CalcPHFromSimpleSolution
rs.append(fx)