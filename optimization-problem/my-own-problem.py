import cvxpy as cp

#Energy Consumption from various resources  - optimal cost calculation

#variable declaration
#total energy from fossil fuel in percentage
fossilFuel = cp.Variable()
#total energy from renewable energy resources in percentage
renewableEnergy = cp.Variable()
#total energy from nulcear energy source in percentage
nuclearEnergy = cp.Variable()
#total energy from hydro energy source in percentage
hydroEnergy = cp.Variable()

#total energey consumption
totalEnergyConsumption = 10000
#cost of individual energy consumption per KW in Euros
costFossilFuelPerKW = 200
costRenewableEnergyPerKW = 30
costNuclearEnergyPerKW = 50
costHydroEnergyPerKW = 100

#total cost of fossil fuel
tCostFossilFuel = ((fossilFuel * totalEnergyConsumption)/100) * costFossilFuelPerKW

#total cost of renewable energy
tCostRenewableEnergy = ((renewableEnergy * totalEnergyConsumption)/100) * costRenewableEnergyPerKW

#total cost of nuclear energy
tCostNuclearEnergy = ((nuclearEnergy * totalEnergyConsumption)/100) * costNuclearEnergyPerKW

#total cost of  hydro energy
tCostHydroEnergy = ((hydroEnergy * totalEnergyConsumption)/100) * costHydroEnergyPerKW


exp = (tCostFossilFuel + tCostRenewableEnergy + tCostNuclearEnergy + tCostHydroEnergy)

netUsage = cp.Minimize(exp)
constraints = [fossilFuel+renewableEnergy+nuclearEnergy+hydroEnergy == 100,10<=renewableEnergy,renewableEnergy<=20,
               30<=nuclearEnergy,20<=hydroEnergy, 5<=fossilFuel,fossilFuel<=10]

probSolve = cp.Problem(netUsage,constraints )
probSolve.solve()

print("status:", probSolve.status)
print("Minimised Cost: ", probSolve.value)
print("Percentage of Total Energy from the Fossil Fuels:  ", fossilFuel.value)
print("Percentage of  Total Energy from the Renewable Energy Sources: ", renewableEnergy.value)
print("Percentage of Total Energy from the Nuclear Energy Sources: ", nuclearEnergy.value)
print("Percentage of  Total Energy from the Hydro Energy Sources: ", hydroEnergy.value)

#total renewable energy value
totalRenewableEnergyValue  = (renewableEnergy.value * totalEnergyConsumption)/100
totalFossilEnergyValue  = (fossilFuel.value * totalEnergyConsumption)/100
totalNuclearEnergyValue  = (nuclearEnergy.value * totalEnergyConsumption)/100
totalHydroEnergyValue  = (hydroEnergy.value * totalEnergyConsumption)/100

#print the total consumtion in kw
print("Total Energy Consumption of Renewable energy in KW : ",totalRenewableEnergyValue)
print("Total Energy Consumption of Fossil fuel in KW : ",totalFossilEnergyValue)
print("Total Energy Consumption of Nuclear energy in KW : ",totalNuclearEnergyValue)
print("Total Energy Consumption of Hydro energy in KW : ",totalHydroEnergyValue)


