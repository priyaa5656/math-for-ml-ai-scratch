import numpy as np
from PIL import Image
import os

print("=== COLOR SVD IMAGE COMPRESSION ===")

# load image (NO grayscale)
img = Image.open("image.jpg").convert("RGB")
A = np.array(img)

print("Image shape:", A.shape)

os.makedirs("output", exist_ok=True)

k_values = [10, 30, 50]

# function
def compress_channel(channel, k):
    U, S, Vt = np.linalg.svd(channel, full_matrices=False)
    return np.clip(U[:, :k] @ np.diag(S[:k]) @ Vt[:k, :], 0, 255)

# split channels
R = A[:, :, 0]
G = A[:, :, 1]
B = A[:, :, 2]

for k in k_values:
    print(f"Processing k = {k}")

    R_c = compress_channel(R, k)
    G_c = compress_channel(G, k)
    B_c = compress_channel(B, k)

    # merge
    compressed = np.stack((R_c, G_c, B_c), axis=2).astype(np.uint8)

    Image.fromarray(compressed).save(f"output/color_k{k}.jpg")

print("✅ DONE! Check output folder")