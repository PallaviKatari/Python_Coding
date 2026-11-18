import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    "Sales": [100, 200, 300, 400, 500],
    "Marketing": [20, 40, 60, 80, 100],
    "Profit": [10, 30, 50, 70, 90],
    "Customers": [5, 10, 15, 20, 25]
}

df = pd.DataFrame(data)

correlation = df.corr()

sns.heatmap(
    correlation,
    annot=True,
    cmap="coolwarm"
)

plt.title("Business Data Correlation")
plt.show()