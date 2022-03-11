import cvxpy as cp

x1 = cp.Variable()
x2 = cp.Variable()

obj = cp.Minimize((x1-2)**2 + 3*x2 - (1/100000)*cp.log(-(-x1-x2+4)))

prob = cp.Problem(obj)
prob.solve()

print("status:", prob.status)
print("optimal value", prob.value)
print("optimal var of x1 : ", x1.value)
print("optimal var of x2 : ",  x2.value)