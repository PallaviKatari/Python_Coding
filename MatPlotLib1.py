import matplotlib.pyplot as plt
import numpy as np

plt.ion()

fig, ax = plt.subplots()

x = np.arange(10)
y = np.random.randint(10, 100, 10)

line, = ax.plot(x, y, marker="o")

ax.set_ylim(0, 120)
ax.set_title("Live Sales Monitoring")

for i in range(10):
    y = np.random.randint(10, 100, 10)

    line.set_ydata(y)

    plt.pause(1)

plt.ioff()
plt.show()