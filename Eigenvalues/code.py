import numpy as np

print("=== EIGENVECTORS & EIGENVALUES ===")

# Matrix
A = np.array([[2, 0],
              [0, 3]])

print("Matrix A:\n", A)


print("\n=== FIND EIGENVALUES & EIGENVECTORS ===")

values, vectors = np.linalg.eig(A)

print("Eigenvalues:", values)
print("Eigenvectors:\n", vectors)


print("\n=== VERIFY Av = λv ===")

# Take first eigenvector
v = vectors[:, 0]
lambda_val = values[0]

left = A @ v
right = lambda_val * v

print("A @ v:", left)
print("λ * v:", right)


print("\n=== MULTIPLE EIGENVECTORS (SCALING) ===")

# Same direction, different scale
v2 = 3 * v
print("Original v:", v)
print("Scaled v (3*v):", v2)

print("Check A @ (3v):", A @ v2)
print("Check λ * (3v):", lambda_val * v2)


print("\n=== SPECIAL CASE (λ = 0) ===")

# Matrix with zero eigenvalue
B = np.array([[1, 2],
              [2, 4]])

values_B, vectors_B = np.linalg.eig(B)

print("Matrix B:\n", B)
print("Eigenvalues:", values_B)

# Check collapse
for i in range(len(values_B)):
    if np.isclose(values_B[i], 0):
        print("Eigenvalue 0 found → data collapses in that direction")


print("\n=== DETERMINANT RELATION ===")

det_A = np.linalg.det(A)
product_lambda = np.prod(values)

print("Determinant:", det_A)
print("Product of Eigenvalues:", product_lambda)


print("\n=== ML INSIGHT ===")

print("Large eigenvalue → important direction")
print("Small eigenvalue → less important")


print("\n=== FINAL UNDERSTANDING ===")

print("Eigenvector = stable direction")
print("Eigenvalue = scaling factor")
print("Av = λv → direction same, magnitude changes")