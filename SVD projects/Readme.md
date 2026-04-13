# 🧠 SVD Image Compression
## 📌 What is this?
This project uses **Singular Value Decomposition (SVD)** to compress an image.
## 🧠 Concept
Any matrix A can be written as:  A = U Σ Vᵀ
- U → output directions  
- Σ → importance (singular values)  
- Vᵀ → input directions  
👉 We keep only top k singular values to compress the image.
---

## 🎯 Goal
- Reduce image size  
- Keep important information  
- Remove noise  

## ⚙️ How it works
1. Convert image to grayscale or colourfull 
2. Apply SVD  
3. Keep only top k singular values  
4. Reconstruct compressed image  

## 📊 Results

| k value| Quality         |
|--------|-----------------|
| 10     | Very blurr      |
| 30     | Medium          |
| 50     | Good            |
| 100    | Almost original |

---

## 🚀 How to Run
```bash
pip install numpy pillow
python colour.py  
python grayscaleoutput.py
```
---

## ❓ Why This Project?
The goal of this project is to **reduce image size while preserving important visual information**.
---
## 📸 Real-Life Motivation
In real-world scenarios:
- Images can be large in size (e.g., 5MB+)  
- We want: Faster sharing (e.g., WhatsApp)  , Less storage usage  
👉 Solution: **Image Compression**
---

## 🤖 What This Project Does
This project uses **Singular Value Decomposition (SVD)** to:
> Keep only the most important information in an image and remove unnecessary data.
---

## ⚙️ How It Works (Simple Explanation)
### 1️⃣ Image as Data
An image is treated as a **matrix of numbers**:
[255   200   100 ...]
[120   90     60 ...]
---

### 2️⃣ Apply SVD
SVD decomposes the image into three matrices:
- U → structure  
- S → importance (singular values)  
- Vᵀ → details  
👉 This helps identify what is important vs less important.
---

### 3️⃣ Keep Top k Values
We choose a value:   k=50
👉 Meaning:
- Keep only the **top 50 important components**  
- Remove less important data  
---

### 4️⃣ Reconstruct Image
Using the reduced data, we rebuild the image.
---

## 📊 Result
- Reduced image size 📉  
- Slight loss in quality 👌  
---

## 🧠 In One Line
> Remove unnecessary data from an image while keeping important features.
---

## 🎯 Applications
### 📸 Image Compression
- Used in apps like WhatsApp, Google Photos  

### 🎬 Video Compression
- Used in platforms like YouTube, Netflix  

### 🧠 Machine Learning
- Reduce data size  
- Faster training  