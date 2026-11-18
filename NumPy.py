# Import NumPy and give it the conventional short name "np".
import numpy as np

# Create two 2 x 2 matrices as NumPy arrays.
# A[i][j] refers to the element in row i and column j.
A = np.array([
    [2, 3],
    [4, 5]
])

B = np.array([
    [6, 7],
    [8, 9]
])

# Perform matrix multiplication: result[i][j] is the dot product of
# row i from A and column j from B.
result = np.dot(A, B)

# Calculate the inverse of A.
# For a 2 x 2 matrix, A multiplied by its inverse produces identity matrix I.
inverse = np.linalg.inv(A)

# Calculate the scalar determinant of A. It is a value that describes
# whether A is invertible and how it scales area; non-zero means invertible.
det = np.linalg.det(A)

# Display each result with a label.
print("Matrix Multiplication:")
print(result)

print("\nMatrix Inverse:")
print(inverse)

print("\nDeterminant:", det)