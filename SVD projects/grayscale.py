import numpy as np
from PIL import Image
import os

print("=== SVD IMAGE COMPRESSION ===")

# ==============================
# 1️⃣ LOAD IMAGE
# ==============================
img = Image.open("image.jpg").convert("L")  # grayscale
A = np.array(img)

print("Image shape:", A.shape)

# create output folder
os.makedirs("output", exist_ok=True)

# ==============================
# 2️⃣ APPLY SVD
# ==============================
U, S, Vt = np.linalg.svd(A)

print("SVD done!")


# ==============================
# 3️⃣ COMPRESS WITH DIFFERENT k
# ==============================
k_values = [10, 30, 50, 100]

for k in k_values:
    print(f"\nProcessing k = {k}")

    # low-rank approximation
    U_k = U[:, :k]
    S_k = np.diag(S[:k])
    Vt_k = Vt[:k, :]

    A_compressed = U_k @ S_k @ Vt_k

    # clip values (important for image)
    A_compressed = np.clip(A_compressed, 0, 255)

    # convert to image
    img_compressed = Image.fromarray(A_compressed.astype(np.uint8))

    # save
    filename = f"output/compressed_k{k}.jpg"
    img_compressed.save(filename)

    print(f"Saved: {filename}")


print("\n✅ DONE! Check output folder")