import pandas as pd

data = {
    "Employee": ["John", "David", "John", "Mary", "David", "Mary"],
    "Department": ["IT", "Sales", "IT", "HR", "Sales", "HR"],
    "Sales": [5000, 8000, 7000, 4000, 9000, 6000]
}

df = pd.DataFrame(data)

# Group by department
department_sales = df.groupby("Department")["Sales"].sum()

print("Department Sales:")
print(department_sales)

# Employee performance
employee_sales = df.groupby("Employee")["Sales"].sum()

print("\nEmployee Performance:")
print(employee_sales)

# Find top-performing employee
print("\nTop Employee:")
print(employee_sales.idxmax())