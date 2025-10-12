import pandas as pd

# Importing in Pandas?
# Pandas allows you to import data from various file formats like CSV, JSON, Excel, etc.
# CSV = Comma Separated Values (plain text format)
# JSON = JavaScript Object Notation (structured data format)

# Importing data from a CSV file
csv_df = pd.read_csv("data.csv")

# Importing data from a JSON file
json_df = pd.read_json("Pokémon.json")

# Displaying a truncated version of the CSV DataFrame
print("Truncated CSV Data:\n", csv_df)

# Displaying the full CSV DataFrame
print("\nFull CSV Data:\n", csv_df.to_string())

# Displaying the full JSON DataFrame
print("\nFull JSON Data:\n", json_df.to_string())