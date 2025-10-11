import pandas as pd

# What is a Series?
# A Pandas Series is a one-dimensional labeled array capable of holding any data type.
# Think of it like a single column in a spreadsheet.

# Creating basic Series with default integer index
numeric_data = [100, 102, 104]
string_data = ["A", "B", "C"]
boolean_data = [True, False, True]

numeric_series = pd.Series(numeric_data)
string_series = pd.Series(string_data)
boolean_series = pd.Series(boolean_data)

print("Numeric Series:\n", numeric_series)
print("\nString Series:\n", string_series)
print("\nBoolean Series:\n", boolean_series)

# Creating Series with custom index labels
room_numbers = [10, 20, 30]
apartment_ids = [101, 202, 303]

room_series = pd.Series(room_numbers, index=["a", "b", "c"])
apartment_series = pd.Series(apartment_ids, index=["apartment #1", "apartment #2", "apartment #3"])

print("\nRoom Series with custom index:\n", room_series)
print("\nApartment Series with custom index:\n", apartment_series)

# Accessing elements using label and position
print("\nAccessing room 'a':", room_series.loc["a"])
print("Accessing first element by position:", room_series.iloc[0])

# Updating a value using label
room_series.loc["c"] = 300
print("\nUpdated Room Series:\n", room_series)

# Filtering Series based on condition
expense_details = [100, 200, 300, 400, 500]
expense_series = pd.Series(expense_details, index=["a", "b", "c", "d", "e"])
print("\nExpenses less than or equal to 200:\n", expense_series[expense_series <= 200])

# Creating Series from dictionary
calorie_data = {"Day 1": 1750, "Day 2": 2100, "Day 3": 1700}
calorie_series = pd.Series(calorie_data)
print("\nCalorie Intake Series:\n", calorie_series)

# Accessing and updating values
print("\nCalories on Day 1:", calorie_series.loc["Day 1"])
calorie_series.loc["Day 2"] += 500
print("\nUpdated Calorie Series:\n", calorie_series)

# Filtering values greater than or equal to 2000
print("\nDays with calorie intake >= 2000:\n", calorie_series[calorie_series >= 2000])




