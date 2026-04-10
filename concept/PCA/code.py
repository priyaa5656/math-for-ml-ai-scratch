import numpy as np

print("=== PCA STEP BY STEP ===\n")

# ==============================
# 1️⃣ DATA
# ==============================
X = np.array([
    [2, 3],
    [3, 5],
    [4, 2],
    [5, 4]
])

print("Original Data:\n", X)


# ==============================
# 2️⃣ CENTER DATA
# ==============================
mean = np.mean(X, axis=0)
X_centered = X - mean

print("\nMean:", mean)
print("\nCentered Data:\n", X_centered)


# ==============================
# 3️⃣ COVARIANCE MATRIX
# ==============================
cov = np.cov(X_centered.T)

print("\nCovariance Matrix:\n", cov)


# ==============================
# 4️⃣ EIGEN DECOMPOSITION
# ==============================
values, vectors = np.linalg.eig(cov)

print("\nEigenvalues:\n", values)
print("\nEigenvectors:\n", vectors)


# ==============================
# 5️⃣ SORT (IMPORTANT)
# ==============================
idx = np.argsort(values)[::-1]

values = values[idx]
vectors = vectors[:, idx]

print("\nSorted Eigenvalues:\n", values)
print("\nSorted Eigenvectors:\n", vectors)


# ==============================
# 6️⃣ SELECT TOP K
# ==============================
k = 1  # reduce 2D → 1D

top_k_vectors = vectors[:, :k]

print(f"\nTop {k} Eigenvector(s):\n", top_k_vectors)


# ==============================
# 7️⃣ PROJECT DATA
# ==============================
X_reduced = X_centered @ top_k_vectors

print("\nReduced Data (Projection):\n", X_reduced)


# ==============================
# 🔥 EXTRA: RECONSTRUCT (optional)
# ==============================
X_approx = X_reduced @ top_k_vectors.T + mean

print("\nReconstructed Data (approx):\n", X_approx)


# ==============================
# 🧠 FINAL UNDERSTANDING
# ==============================
print("\n=== FINAL ===")
print("PCA = Data → Center → Cov → Eigen → Sort → Project")