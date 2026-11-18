import pandas as pd

data = {
    "Product": ["Laptop", "Mobile", "Tablet", "Laptop", "Mobile"],
    "Price": [60000, 25000, 30000, 65000, 28000],
    "Quantity": [2, 5, 3, 1, 4]
}

df = pd.DataFrame(data)

# Calculate revenue
df["Revenue"] = df["Price"] * df["Quantity"]

# Apply conditional classification
df["Category"] = df["Revenue"].apply(
    lambda x: "High Value" if x > 100000 else "Normal"
)

# Pivot table
pivot = pd.pivot_table(
    df,
    values="Revenue",
    index="Product",
    aggfunc="sum"
)

print(df)
print("\nPivot Table:")
print(pivot)