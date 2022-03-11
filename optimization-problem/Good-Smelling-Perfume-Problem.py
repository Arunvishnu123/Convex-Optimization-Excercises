import cvxpy as cp

# variable declaration for blend
blendOne = cp.Variable()
blendTwo = cp.Variable()
blendThree = cp.Variable()
blendFour = cp.Variable()

# equation for the total cost
totalCost = blendOne * 55 + blendTwo * 65 + blendThree * 35 + blendFour * 85

calculateTotalCost = cp.Minimize(totalCost)


# total percentage of beragamont Orange content in the blend
beragamotOrange =  0.35 * blendOne + 0.60 * blendTwo + 0.35 * blendThree + 0.40 * blendFour

# total percentage of thymus content in the blend
thymusContent = 0.15 * blendOne + 0.05 * blendTwo + 0.20 * blendThree + 0.10 * blendFour

# total percentage of rose centent in the blend
roseContent =  0.30 * blendOne + 0.20 * blendTwo + 0.40 * blendThree + 0.20 * blendFour

# total percentage of lilly in the blend
lillyContent =0.20 * blendOne + 0.15 * blendTwo + 0.05 * blendThree + 0.30 * blendFour
# constraints
constraints = [0.05 <= blendTwo, blendTwo <= 0.2,
               0.3 <= blendThree,
               0.1 <= blendOne, blendOne <= 0.25,
               beragamotOrange <= 0.5,
               0.08 <= thymusContent, thymusContent <= 0.13,
               roseContent <= 0.35,
               0.19 <= lillyContent,blendOne+blendTwo+blendThree+blendFour ==1
             ]

probSolve = cp.Problem(calculateTotalCost, constraints)
probSolve.solve()

print("status:", probSolve.status)
print("optimal cost", probSolve.value)
print("Percentage of blend One: ", blendOne.value)
print("Percentage of blend Two: ", blendTwo.value)
print("Percentage of blend Three: ", blendThree.value)
print("Percentage of blend Four: ", blendFour.value)
