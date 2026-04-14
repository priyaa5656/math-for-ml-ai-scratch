import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.decomposition import PCA

# load dataset
data = load_iris()
X = data.data
y = data.target

# apply PCA
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X)

print("Original shape:", X.shape)
print("Reduced shape:", X_pca.shape)

# plot
plt.figure()

for i in range(3):
    plt.scatter(X_pca[y == i, 0],
                X_pca[y == i, 1],
                label=data.target_names[i])

plt.xlabel("PC1")
plt.ylabel("PC2")
plt.legend()
plt.title("PCA Visualization")

plt.savefig("output.png")  # 🔥 important
plt.show()