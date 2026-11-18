import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

sns.histplot(
    data=tips,
    x="total_bill",
    hue="sex",
    kde=True
)

plt.title("Customer Bill Distribution")
plt.show()