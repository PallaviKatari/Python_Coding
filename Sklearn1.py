import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

customers = np.array([
    [20, 2000],
    [25, 2500],
    [30, 3000],
    [45, 8000],
    [50, 9000],
    [55, 10000],
    [60, 15000],
    [65, 16000]
])

model = KMeans(
    n_clusters=3,
    random_state=42,
    n_init=10
)

clusters = model.fit_predict(customers)

plt.scatter(
    customers[:, 0],
    customers[:, 1],
    c=clusters
)

plt.xlabel("Age")
plt.ylabel("Annual Spending")
plt.title("Customer Segmentation")

plt.show()

print("Cluster Assignments:", clusters)