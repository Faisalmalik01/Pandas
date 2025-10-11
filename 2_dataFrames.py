import pandas as pd

# What is a DataFrame?
# A Pandas DataFrame is a 2D-labeled data structure with rows and columns.
# It's similar to an Excel spreadsheet or SQL table.

# Creating a basic DataFrame with default integer index
employee_data = {
    "Name": ["Spongebob", "Patrick", "Squidward"],
    "Age": [42, 42, 42]
}

df_default = pd.DataFrame(employee_data)
print("Default DataFrame:\n", df_default)

# Creating a DataFrame with custom row labels (index)
df_custom = pd.DataFrame(employee_data, index=["Employee 1", "Employee 2", "Employee 3"])
print("\nCustom Indexed DataFrame:\n", df_custom)

# Accessing rows using label and position
print("\nAccessing Employee 2 by label:\n", df_custom.loc["Employee 2"])
print("\nAccessing first row by position:\n", df_custom.iloc[0])

# Adding a new column to the DataFrame
df_custom["Job"] = ["Cook", "N/A", "Cashier"]
print("\nDataFrame after adding 'Job' column:\n", df_custom)

# Adding a single new row
new_employee = pd.DataFrame([{"Name": "Sandy", "Age": 28, "Job": "Engineer"}],
                            index=["Employee 4"])
df_custom = pd.concat([df_custom, new_employee])
print("\nDataFrame after adding Employee 4:\n", df_custom)

# Adding multiple new rows
additional_employees = pd.DataFrame([
    {"Name": "Sandy2", "Age": 28, "Job": "Engineer"},
    {"Name": "Eugine", "Age": 60, "Job": "Manager"}
], index=["Employee 5", "Employee 6"])

df_custom = pd.concat([df_custom, additional_employees])
print("\nDataFrame after adding Employees 5 and 6:\n", df_custom)