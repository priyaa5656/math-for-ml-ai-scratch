import numpy as np

print("=== Linear Algebra: Core Example ===")

# Vector (data)
v = np.array([2, 3])

# Matrix (transformation)
A = np.array([[2, 0],
              [0, 1]])

# Transformation
result = A @ v
print("Transformation Result:", result)  # [4, 3]


print("\n=== VECTORS ===")

v = np.array([2, 3])
print("Vector:", v)

# Addition
v1 = np.array([1, 2])
v2 = np.array([3, 4])
print("Addition:", v1 + v2)  # [4, 6]

# Scalar Multiplication
print("Scalar Multiplication:", 2 * v)  # [4, 6]

# Magnitude
print("Magnitude:", np.linalg.norm(v))

# Dot Product
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print("Dot Product:", np.dot(a, b))  # 32

# Cross Product
a = np.array([1, 0, 0])
b = np.array([0, 1, 0])
print("Cross Product:", np.cross(a, b))  # [0, 0, 1]

# Unit Vector
v = np.array([3, 4])
unit_v = v / np.linalg.norm(v)
print("Unit Vector:", unit_v)

# Angle (Cosine Similarity)
a = np.array([1, 2])
b = np.array([2, 3])
angle = np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))
print("Cosine Similarity:", angle)


print("\n=== LINEAR COMBINATION ===")

v1 = np.array([1, 0])
v2 = np.array([0, 1])

result = 2 * v1 + 3 * v2
print("Linear Combination:", result)  # [2, 3]

# ML Example (Neuron)
x = np.array([2, 3, 4])
w = np.array([0.5, 0.2, 0.1])
output = np.dot(w, x)
print("Neuron Output:", output)


print("\n=== SPAN & BASIS ===")

v1 = np.array([1, 0])
v2 = np.array([0, 1])

a, b = 2, 3
span = a * v1 + b * v2
print("Span Example:", span)

# Dependent vectors example
v1 = np.array([1, 2])
v2 = np.array([2, 4])  # dependent
print("Dependent Example:", 3 * v1, "==", v2 * 1.5)


print("\n=== LINEAR TRANSFORMATION ===")

A = np.array([[2, 0],
              [0, 1]])

v = np.array([1, 2])

result = A @ v
print("Transformed Vector:", result)  # [2, 2]


print("\n=== FINAL UNDERSTANDING ===")

print("Linear Algebra = transforming vectors")
print("Flow: Vector → Linear Combination → Span → Transformation → ML Model")