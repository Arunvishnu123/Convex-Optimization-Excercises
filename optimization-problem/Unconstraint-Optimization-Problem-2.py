import cvxpy as cp
from sympy import symbols,Matrix
from numpy.linalg import eig
import numpy as np

#SymPy is a Python library for symbolic mathematics. It aims to become a full-featured computer algebra system (CAS)
# while keeping the code as simple as possible in order to be comprehensible and easily extensible.
# SymPy is written entirely in Python.

#Before we can construct symbolic math expressions or symbolic math equations  with SymPy,
# first we need to create symbolic math variables, also called symbolic math symbols.
x1 = symbols('x1')
x2 = symbols('x2')
x3 = symbols('x3')

equation = x1**3 + (x2-x3)**2 + x3**3 + 2

# sympy library is used to find the derivative of the function
#calculate the derivative of function "equation" with respect to x1
derivative_x1 = equation.diff(x1)
print("Derivative of function wrt x1 :",derivative_x1)

#calculate the derivative of function "equation" with respect to x2
derivative_x2 = equation.diff(x2)
print("Derivative of function wrt x2 :",derivative_x2)

#calculate the derivative of functioin "equation" with respect to x3
derivative_x3 = equation.diff(x3)
print("Derivative of function wrt x3 :",derivative_x3)
matrix =  []
#hessain matrix
matrix = np.array([[derivative_x1.diff(x1),derivative_x1.diff(x2),derivative_x1.diff(x3)],
                           [derivative_x2.diff(x1),derivative_x2.diff(x2),derivative_x2.diff(x3)],
                           [derivative_x3.diff(x1),derivative_x3.diff(x2),derivative_x3.diff(x3)]])

print(matrix)

hessian_matrix = Matrix(matrix)
print("eigen value: ", hessian_matrix.eigenvals())
# here all the eign value are not positive this is not convex

print(hessian_matrix.det())



x1 = cp.Variable()
x2 = cp.Variable()
x3 = cp.Variable()

obj = cp.Minimize(x1**3 + (x2-x3)**2 + x3**3 + 2)
constraints  = [0<=x3]

prob =cp.Problem(obj,constraints)
prob.solve()

print("status: ", prob.status)
print("optimal value: ", prob.value)
print("optimal var x1: ", x1.value)
print("optimal var x2: ", x2.value)
print("optimal var x3: ", x3.value)

