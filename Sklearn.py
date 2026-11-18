import numpy as np
from sklearn.linear_model import LinearRegression

# House sizes
X = np.array([
    [1000],
    [1500],
    [2000],
    [2500],
    [3000]
])

# House prices (in thousands)
y = np.array([200, 300, 400, 500, 600])

model = LinearRegression()

model.fit(X, y)

# Predict price for 2200 sq.ft.
prediction = model.predict([[2200]])

print("Predicted House Price:", prediction[0])

print("Model Coefficient:", model.coef_)
print("Model Intercept:", model.intercept_)