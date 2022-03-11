import cvxpy as cp

# Create two scalar optimization variables.
x1 = cp.Variable()
x2 = cp.Variable()

#form objective.
obj = cp.Minimize((x1-4)**2 + 7*(x2-4)**2 + 4*x2)

prob = cp.Problem(obj)
#solution.
prob.solve()
print("status: ", prob.status)
print("optimal value: ", prob.value)
print("optimal var x1: ", x1.value)
print("optimal var x2: ", x2.value)
