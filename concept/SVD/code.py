import numpy as np

print("=== SVD STEP BY STEP ===\n")

# ==============================
# 1️⃣ ORIGINAL MATRIX
# ==============================
A = np.array([[3, 1],
              [1, 3]])

print("Original Matrix A:\n", A)


# ==============================
# 2️⃣ SVD DECOMPOSITION
# ==============================
U, S, Vt = np.linalg.svd(A)

print("\nU (Output Directions):\n", U)
print("\nSingular Values:\n", S)
print("\nV^T (Input Directions):\n", Vt)


# ==============================
# 3️⃣ CREATE SIGMA MATRIX
# ==============================
Sigma = np.zeros_like(A, dtype=float)
np.fill_diagonal(Sigma, S)

print("\nSigma Matrix:\n", Sigma)


# ==============================
# 4️⃣ VERIFY RECONSTRUCTION
# ==============================
A_reconstructed = U @ Sigma @ Vt

print("\nReconstructed Matrix:\n", A_reconstructed)


# ==============================
# 5️⃣ CHECK ERROR (IMPORTANT)
# ==============================
error = np.linalg.norm(A - A_reconstructed)

print("\nReconstruction Error:", error)


# ==============================
# 6️⃣ UNDERSTANDING RANK
# ==============================
rank = np.sum(S > 1e-10)

print("\nRank of Matrix:", rank)


# ==============================
# 7️⃣ LOW-RANK APPROXIMATION 🔥
# ==============================
k = 1  # reduce complexity

U_k = U[:, :k]
S_k = np.diag(S[:k])
Vt_k = Vt[:k, :]

A_approx = U_k @ S_k @ Vt_k

print(f"\nLow-Rank Approximation (k={k}):\n", A_approx)


# ==============================
# 🧠 FINAL UNDERSTANDING
# ==============================
print("\n=== FINAL ===")
print("SVD = A → U Σ V^T")
print("Transformation = Rotate → Scale → Rotate")

