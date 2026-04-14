import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 4, 1, 8, 7]

plt.plot(x, y)
plt.scatter(x, y)

plt.xlabel("X axis")
plt.ylabel("Y axis")
plt.title("Basic Matplotlib Graph")

plt.grid()  # 🔥 add this (better visibility)

plt.show()

