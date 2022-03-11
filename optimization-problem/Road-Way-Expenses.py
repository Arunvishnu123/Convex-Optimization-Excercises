
import cvxpy as cp

xRural = cp.Variable()
xUrban = cp.Variable()

bRural = 7000 * cp.log(1 + xRural)
bUrban = 5000 * cp.log(1 + xUrban)

equation  = bRural + bUrban - xRural -xUrban

netBenefitCalc = cp.Maximize(equation)

constraints = [xRural + xUrban == 200]

problSolution = cp.Problem(netBenefitCalc,constraints)
problSolution.solve()

print("status:", problSolution.status)
print("Optimal Solution", problSolution.value)
print("xRural : ", xRural.value)
print("xUrban : ", xUrban.value)

