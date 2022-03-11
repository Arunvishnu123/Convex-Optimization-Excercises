import cvxpy as cp

# total quantity extracted from reservoir in litres
reservoirQuantity  = cp.Variable()

# total quantity extracted from stream in litres
streamQuantity = cp.Variable()

#total cost calculation formula
totalCost = cp.Minimize(((reservoirQuantity*100)/1000)+(50*streamQuantity/1000))

constraints = [reservoirQuantity + streamQuantity ==500000, streamQuantity <=100000,
               reservoirQuantity * 50 + streamQuantity*250 <= 50000000]

probSolve = cp.Problem(totalCost,constraints)
probSolve.solve()

print("status:", probSolve.status)
print("Minimised Cost: ", probSolve.value)
print("Water extracted from reservoir: ", reservoirQuantity .value)
print("Water extracted from stream: ", streamQuantity.value)
