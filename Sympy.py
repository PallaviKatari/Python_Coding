import sympy as sp

x = sp.Symbol("x")

expression = x**3 + 5*x**2 + 10*x + 5

# Differentiation
derivative = sp.diff(expression, x)

# Integration
integration = sp.integrate(expression, x)

# Solve equation
solutions = sp.solve(expression, x)

print("Expression:", expression)
print("Derivative:", derivative)
print("Integration:", integration)
print("Solutions:", solutions)