from scipy.optimize import minimize

# Cost function
def cost(x):
    return (x[0] - 5) ** 2 + (x[1] - 10) ** 2

initial_guess = [0, 0]

result = minimize(cost, initial_guess)

print("Optimal Values:", result.x)
print("Minimum Cost:", result.fun)