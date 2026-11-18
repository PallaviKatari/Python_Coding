import matplotlib.pyplot as plt
import numpy as np

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]

sales = [12000, 15000, 18000, 14000, 22000, 25000]
expenses = [8000, 9000, 11000, 10000, 14000, 16000]

profit = np.array(sales) - np.array(expenses)

fig, axes = plt.subplots(2, 2, figsize=(12, 8))

# Line chart
axes[0, 0].plot(months, sales, marker="o")
axes[0, 0].set_title("Monthly Sales")

# Bar chart
axes[0, 1].bar(months, expenses)
axes[0, 1].set_title("Monthly Expenses")

# Pie chart
axes[1, 0].pie(profit, labels=months, autopct="%1.1f%%")
axes[1, 0].set_title("Profit Distribution")

# Histogram
axes[1, 1].hist(sales, bins=5)
axes[1, 1].set_title("Sales Distribution")

plt.tight_layout()
plt.show()