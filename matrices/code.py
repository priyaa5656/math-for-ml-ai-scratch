import numpy as np

print("=== MATRIX BASICS ===")

A = np.array([[1, 2],
              [3, 4]])

print("Matrix A:\n", A)
print("Shape:", A.shape)  # (2,2)


print("\n=== TYPES OF MATRICES ===")

# Zero Matrix
Z = np.zeros((2, 2))
print("Zero Matrix:\n", Z)

# Ones Matrix
O = np.ones((2, 2))
print("Ones Matrix:\n", O)

# Identity Matrix
I = np.eye(2)
print("Identity Matrix:\n", I)

# Diagonal Matrix
D = np.diag([2, 3])
print("Diagonal Matrix:\n", D)

# Triangular Matrices
A_tri = np.array([[1,2,3],
                  [4,5,6],
                  [7,8,9]])

print("Upper Triangular:\n", np.triu(A_tri))
print("Lower Triangular:\n", np.tril(A_tri))


print("\n=== CONCATENATION ===")

A = np.array([[1,2],
              [3,4]])

B = np.array([[5,6],
              [7,8]])

# Horizontal
print("Horizontal Stack:\n", np.hstack((A, B)))

# Vertical
print("Vertical Stack:\n", np.vstack((A, B)))


print("\n=== BASIC OPERATIONS ===")

# Addition
print("Addition:\n", A + B)

# Subtraction
print("Subtraction:\n", A - B)


print("\n=== MATRIX MULTIPLICATION ===")

C = np.array([[2,0],
              [1,2]])

print("A @ C:\n", A @ C)

# Order check
print("C @ A:\n", C @ A)  # different result


print("\n=== TRANSPOSE ===")

print("Transpose:\n", A.T)


print("\n=== DETERMINANT ===")

det = np.linalg.det(A)
print("Determinant:", det)


print("\n=== RANK ===")

rank = np.linalg.matrix_rank(A)
print("Rank:", rank)


print("\n=== TRACE ===")

trace = np.trace(A)
print("Trace:", trace)


print("\n=== INVERSE ===")

if det != 0:
    inv = np.linalg.inv(A)
    print("Inverse:\n", inv)
    print("Check A @ A⁻¹:\n", A @ inv)
else:
    print("Matrix not invertible (det = 0)")


print("\n=== ML EXAMPLE ===")

# Input (vector)
X = np.array([[2],
              [3]])

# Weights (matrix)
W = np.array([[0.5, 0.2]])

# Bias
b = 1

output = W @ X + b
print("Prediction:", output)


print("\n=== FINAL UNDERSTANDING ===")

print("Matrix = data + transformation system")
print("Flow: Vector → Matrix → Transformation → Output")
print("ML: Input → Weights → Prediction")