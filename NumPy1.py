import numpy as np

# Generate 1000 random sales values
sales = np.random.normal(
    loc=5000,
    scale=1000,
    size=1000
)

print("Mean:", np.mean(sales))
print("Median:", np.median(sales))
print("Standard Deviation:", np.std(sales))
print("Maximum:", np.max(sales))
print("Minimum:", np.min(sales))

# Find sales above 6000
high_sales = sales[sales > 6000]

print("High Sales Count:", len(high_sales))
print("High Sales Values:", high_sales)