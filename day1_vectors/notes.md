# Linear Algebra
Linear algebra is the study of vectors and matrices used to represent and transform data.
Data = Vector
Model = Matrix
Prediction = Transformation

### Example 
```python 
v = np.array([2, 3])  # vector (data)

A = np.array([[2, 0],
              [0, 1]])       # matrix (transformation)

result = A @ v        # operation
print(result)
```

## 🧭 1. VECTORS
A vector is an ordered list of numbers. 👉 Think: movement from one point to another
Vector = direction + magnitude


### 🔢 Mathematical Definition
👉 Vector = ordered list of numbers
Example: 
v = [2, 3]
2 → x direction
3 → y direction

### 📍 Visual Thinking
Vector = arrow from origin (0,0) to point (2,3)
👉 Start: (0,0)
👉 End: (2,3)

```python
v = np.array([2, 3])
print(v)
```
👉 This is EXACT same vector 

### 🧪 Basic Operations
#### ➤ 1. Addition
```python 
v1 = np.array([1, 2])
v2 = np.array([3, 4])
print(v1 + v2)   # [4, 6]
```

#### ➤ 2. Scalar Multiplication
To multiply a vector by a scalar (a single number), we multiply each component by that scalar.
```python
v = np.array([2, 3])
print(2 * v)   # [4, 6]
```
👉 Meaning: same direction, bigger size. here 2 is a scalar.

#### ➤ 3. Length (Magnitude)
```python
np.linalg.norm(v)
```
👉 Distance from origin


##### 🚀 Mini Task (DO THIS)
```python
v1 = np.array([1, 2, 3])
v2 = np.array([4, 5, 6])
# 1. Add
# 2. Multiply by 3v1 or 3v2
```
output
v1+v2= ([5, 7, 9])
3*V1=   ([3, 6,9])  and 3*V2=   ([12, 15, 18])


#### ➤ 4. Dot product
The dot product of two vectors is a scalar value.
Formula:   a · b = a₁b₁ + a₂b₂ + ... + aₙbₙ
example 
a = [1, 2, 3]  
b = [4, 5, 6]

a · b = (1×4) + (2×5) + (3×6)  
= 4 + 10 + 18  
= 32

```python
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

dot = np.dot(a, b)
print(dot)        #32 
```   
👉 Measures similarity:
Large → same direction
Zero → perpendicular
Negative → opposite

#### ➤ 5.  Cross Product
```python
a = np.array([1, 0, 0])
b = np.array([0, 1, 0])
print(np.cross(a, b))  # [0, 0, 1]
```
👉 Perpendicular vector

#### ➤ 6.  Unit Vector (VERY IMPORTANT)
```python
v = np.array([3, 4])
unit_v = v / np.linalg.norm(v)
print(unit_v)
```
👉 Direction only (magnitude = 1)

#### ➤ 7.  Angle Between Vectors (🔥 ML important)
```python
a = np.array([1, 2])
b = np.array([2, 3])
angle = np.dot(a, b) / (np.linalg.norm(a)*np.linalg.norm(b))
print(angle)
```
👉 Used in cosine similarity

## 2. 🧭 LINEAR COMBINATION
Mixing vectors with weights. A linear combination of vectors:
a₁v₁ + a₂v₂ + ... + aₙvₙ   Where:   v = vectors,   a = scalars (weights)

Example1: 
You have 2 directions:
Right → [1, 0]
Up → [0, 1]
Now you say: 👉 “2 steps right + 3 steps up”
That is:  2 * [1,0] + 3 * [0,1] = [2,3]
👉 This = linear combination 

Example2: 
```python 
v1 = np.array([1, 0])
v2 = np.array([0, 1])
a=2 ,b=3 
result = 2*v1 + 3*v2
print(result)        #[2, 3]
```

Example3: 
```python
x = np.array([2, 3, 4])     # input
w = np.array([0.5, 0.2, 0.1])  # weights
output = np.dot(w, x)
print(output)         #2.0
```


## 3. 🧭 SPAN & BASIS
👉 Span = all possible vectors you can create using linear combinations
Span of vectors = set of all linear combinations

🎯 Example 
You have:
v₁ = [1, 0] (right)
v₂ = [0, 1] (up)
👉 By combining them:  a*v₁ + b*v₂
You can reach ANY point in 2D plane
👉 So: Span(v₁, v₂) = entire 2D space

👉 Basis = minimum vectors needed to create the whole space

```python
v1 = np.array([1, 0])
v2 = np.array([0, 1])

# Random combination
a, b = 2, 3
span = a*v1 + b*v2
print(span) 
``` 
output  [2, 3]  👉 Change a, b → get different points → that’s span

🧠 Key Understanding
Vectors	Span
Independent vectors → full space
Dependent vectors → limited space


## 4. 🧭 LINEAR TRANSFORMATION
A linear transformation changes a vector using a matrix. It can scale, rotate, or stretch the vector.
👉 Linear Transformation = function that moves vectors 
 T(v) = A @ v ,            where:  A = transformation matrix    v = input vector  ,output = transformed vector

####  Properties 👉it must follow then → linear transformation ✅
1. Additivity-- T(v₁ + v₂) = T(v₁) + T(v₂)
2. Scaling-- T(c·v) = c·T(v)

```python
# Transformation matrix
A = np.array([[2, 0],
              [0, 1]])

# Input vector
v = np.array([1, 2])

# Apply transformation
result = A @ v

print(result)   
```
output:  [2, 2]



🧠 Final Understanding
Linear Algebra = transforming vectors
Flow:
Vector → Linear Combination → Span → Transformation → ML Model