# 🧭 MATRICES
👉 Matrix = a structure that represents data AND transformations.
👉 Vector = single data
👉 Matrix = multiple data + transformation machine

Think:
Vector = one student data
Matrix = full class data

🔢 Definition:  A matrix is a 2D array of numbers arranged in rows and columns.

Example:
A = [[1, 2],
     [3, 4]]   👉 Shape = (rows, columns) = (2, 2)

## example :
```python 
A = np.array([[1, 2],
              [3, 4]])

print(A)
print(A.shape)   # (2,2)
```

## 📏 Important Terms
Term	   | Meaning
Row     |	Horizontal
Column  |	Vertical
Shape   | (rows, columns)
Element |	Single value

## 🧪 Type of Matrix:
### ➤ 1. ZERO MATRIX
🧠 Intuition 👉 Matrix all values = 0
👉 “No information / empty data”

📊 Example
[[0, 0],
 [0, 0]]

```python
Z = np.zeros((2,2))
print(Z)
```
### ➤ 2.MATRIX OF ONES
🧠 Intuition  👉 all values = 1  👉 “Uniform data”

📊 Example
[[1, 1],
 [1, 1]]

```python
O = np.ones((2,2))
print(O)
```

### ➤ 3.IDENTITY MATRIX (I) 🔥
🧠 Intuition 👉 “Do nothing matrix”

📊 Example
[[1, 0],
 [0, 1]]
👉 A @ I = A

```python
I = np.eye(2)
print(I)
```

### ➤ 4. DIAGONAL MATRIX
🧠 Intuition 👉 only diagonal has values , all other values 0

📊 Example
[[2, 0],
 [0, 3]]
👉 Independent scaling

```python
D = np.diag([2, 3])
print(D)
```

### ➤ 5. TRIANGULAR MATRICES
#### 🔺 (A) Upper Triangular
🧠 Intuition 👉 Diagonal bottom all values are zero

[[1, 2, 3],
 [0, 4, 5],
 [0, 0, 6]]

```python
A = np.array([[1,2,3],
              [4,5,6],
              [7,8,9]])

upper = np.triu(A)
print(upper)
```

#### 🔻 (B) Lower Triangular
🧠 Intuition 👉 Diagonal top zero

[[1, 0, 0],
 [4, 5, 0],
 [7, 8, 9]]
```python
lower = np.tril(A)
print(lower)
```

### ➤ 6. CONCATENATE MATRICES
🧠 Intuition 👉 Matrices adding  (side by side ya top bottom)

📊 Example
#### ➤ Horizontal (side by side)

A = np.array([[1,2],
              [3,4]])

B = np.array([[5,6],
              [7,8]])

```python
print(np.hstack((A,B)))
```

#### ➤ Vertical (upar niche)
```python
print(np.vstack((A,B)))
```


## 🧪 BASIC OPERATIONS
### ➤ 1. Addition -👉 add Same size of 2 tables  
A = marks of class 1
B = marks of class 2
👉 Add = total marks
🔢 Rule 👉 Shape will be SAME.  (m × n) + (m × n)
📊 Example
A = [[1, 2],
     [3, 4]] 
B = [[5, 6],
     [7, 8]]

👉 Add:
(A + B) = [[1+5, 2+6],
            [3+7, 4+8]]

(A + B)= [[6, 8],
          [10,12]]


Example :
```python
A = np.array([[1,2],
              [3,4]])

B = np.array([[5,6],
              [7,8]])

print(A + B)
```

### 🧠 2. MATRIX SUBTRACTION
🧠 Intuition- 👉 Difference between two datasets

🔢 Rule 👉 Same shape required
📊 Example
A - B = [[1-5, 2-6],
         [3-7, 4-8]]

= [[-4, -4],
   [-4, -4]]

Example :
```python
A = np.array([[1,2],
              [3,4]])

B = np.array([[5,6],
              [7,8]])

print(A - B)
```

### 🧠 3. MATRIX MULTIPLICATION 🔥 (MOST IMPORTANT)
🧠 Intuition (VERY IMPORTANT) 👉 Matrix multiplication = transformation apply 

Think:  X = input data  , W = model   , 👉 W @ X = prediction
🔢 Rule;;    (m × n) @ (n × p) → (m × p)  👉 Inner dimension SAME hona chahiye
```markdown
👉 Order matters:  A @ B ≠ B @ A

📊 Example (Step-by-Step)
A = [[1, 2],
     [3, 4]]

B = [[2, 0],
     [1, 2]]

A @ B = [[(1×2 + 2×1) , (1×0 + 2×2)],
         [(3×2 + 4×1), (3×0 + 4×2) ]]

A @ B = [[4, 4],
         [10, 8]]

Example :
```python
A = np.array([[1,2],
              [3,4]])

B = np.array([[2,0],
              [1,2]])

print(A @ B)
```


### ➤ 4. Transpose (Aᵀ)
🧠 Intuition 👉 Rows ↔ Columns swap
🔢 Definition If: A = (m × n) Then: Aᵀ = (n × m)
📊 Example
A = [[1, 2],
     [3, 4]]

Aᵀ = [[1, 3],
      [2, 4]]

Example: 
```python
A = np.array([[1,2],
              [3,4]])

print(A.T)
```

### ➤ 5. DETERMINANT (det(A)) 🔥
🧠 Real Intuition 👉 “how much Matrix change space?”
👉 det > 1 → expansion  
👉 det < 1 → shrink  
👉 det = 0 → collapse (information loss)

🎯 Example
A = [[2, 0],
     [0, 3]]

det(A) = (2×3) - (0×0) = 6 👉 Area is 6 times 

❗ Important
det = 0 → space collapse 😨

```python
np.linalg.det(A)
```
### ➤ 6. RANK
🧠 Intuition 👉 how much independent information we have
🔢 Definition: Number of linearly independent rows/columns

📊 Example
A = [[1,2],
     [2,4]]

Rank = 1 (dependent rows)

```python
np.linalg.matrix_rank(A)
```

### ➤ 7.TRACE
🧠 Intuition 👉 Diagonal elements ka sum

🔢 Definition
Trace(A) = a₁₁ + a₂₂ + a₃₃ + ...
📊 Example
A = [[1,2],
     [3,4]]

Trace = 1 + 4 = 5

```python 
np.trace(A)
```

### ➤ 8. INVERSE MATRIX (A⁻¹) 🔥
🧠 Intuition 👉 Reverse transformation
think ;; A = forward action , A⁻¹ = undo
🔢 Rule:;   A⁻¹ @ A = I
👉 Not all matrices have inverse  
👉 Only square matrices with det ≠ 0
📊 Example
A = [[1,2],
     [3,4]]

A⁻¹ exists only if det(A) ≠ 0

```python
np.linalg.inv(A)
```
⚠️ Important
👉 det(A) = 0 → inverse NOT possible

## 🧠 Final Understanding

Matrix = data + transformation system

Flow:
Vector → Matrix → Transformation → Output

In ML:
Input → Weights → Prediction


