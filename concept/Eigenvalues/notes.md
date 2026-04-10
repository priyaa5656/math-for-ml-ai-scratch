# 🧠 🧭 EIGENVECTORS & EIGENVALUES
Intuition (Think):  👉 You apply a transformation (matrix). Mostly, the direction of vectors changes. But There are some special vectors :The direction remains the same. Only the length changes.👉 that is:
Eigenvector = special direction
Eigenvalue (λ) = how much stretch/shrink occurred

## 🔢 Definition  :  
👉 Meaning:
Matrix A transforms vector v,
but direction remains same (only scaled by λ)
Av=λv   👉 A = matrix , 👉 v = eigenvector, 👉 λ = eigenvalue

👉 Conditions:
- v ≠ 0
- Not all vectors are eigenvectors

key insight:
👉 Eigenvectors are directions
👉 Eigenvalues are scaling factors

🎯 Simple Example
Matrix:  A = [[2, 0],
              [0, 3]]

👉 x-axis → 2x stretch, 👉 y-axis → 3x stretch ,  So:
[1,0] → eigenvector (λ = 2)
[0,1] → eigenvector (λ = 3)


🎯 example :- 
```python
A = np.array([[2, 0],
              [0, 3]])
values, vectors = np.linalg.eig(A)

print("Eigenvalues:", values)
print("Eigenvectors:\n", vectors)
```

🔍 Verify: Av = λv

```python
v = vectors[:,0]
lambda_val = values[0]

print(A @ v)               #A @ v = [2, 0]
print(lambda_val * v)      #λ * v = [2, 0]
```

🔍 Scaling

```python
v_scaled = 3 * v    # v=[1, 0] => 3v = [3, 0]

print("A @ (3v):", A @ v_scaled)               #A @ 3v = [6, 0]
print("λ * (3v):", lambda_val * v_scaled)      #λ * 3v = [6, 0]  i.e Av= λv
```

🧠 Important Understanding
👉 Every matrix can have:
multiple eigenvectors.
infinite multiples of the same direction

👉 ML Insight:
- Large λ → important direction
- Small λ → less important

👉 Special Case:
- λ = 0 → data collapse (information loss)

👉 Important Relation:
Product of eigenvalues = determinant of matrix