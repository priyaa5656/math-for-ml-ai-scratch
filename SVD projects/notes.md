# 🧠 Linear Algebra Notes – SVD Image Compression

---

## 📌 Why I Built This Project

I built this project to understand how **Linear Algebra is used in real-world applications**.

👉 Instead of just learning theory, I wanted to:
- Apply math in code  
- See actual output  
- Understand how data is reduced  

---

## 🎯 Key Concept: Singular Value Decomposition (SVD)

SVD is a method to break a matrix into 3 parts:

A = U Σ Vᵀ

- U → structure (how data is arranged)  
- Σ → importance (which parts matter most)  
- Vᵀ → details (input patterns)  

---

## 🧠 Intuition (Simple Understanding)

👉 Think of an image:

- Some parts are **very important (edges, shapes)**  
- Some parts are **less important (tiny details, noise)**  

💡 SVD helps us:
- Keep important parts  
- Remove less useful data  

---

## ⚙️ What I Did in This Project

### 1️⃣ Converted Image to Matrix
- Image = grid of numbers (pixels)

---

### 2️⃣ Applied SVD
- Broke image into U, S, Vᵀ

---

### 3️⃣ Reduced Data
- Selected only top k values  
- Removed less important information  

---

### 4️⃣ Reconstructed Image
- Built image again using reduced data  

---

## 📊 Observations

- Small k → blurry image  
- Medium k → decent quality  
- Large k → almost original  

👉 Tradeoff:
- Lower size vs better quality  

---

## 🧠 What I Learned

- Linear Algebra is used in real applications  
- SVD is a powerful compression tool  
- Data can be reduced without losing much quality  
- Images are just matrices  

---

## ❗ Challenges Faced

- Understanding SVD concept  
- Handling color images (RGB channels)  
- Fixing errors while running code  

---

## 💡 Key Insight

> We don’t need all data to represent something — only the most important parts.

---

## 🚀 Future Improvements

- Add GUI (user selects k value)  
- Compare file sizes before/after  
- Apply on videos  

---

## 🧠 In One Line

> Linear Algebra can compress real-world data by keeping only important information.