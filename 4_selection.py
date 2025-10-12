import pandas as pd

# What is Selection in Pandas?
# Selection refers to accessing specific rows, columns, or subsets of a DataFrame.

# Load data from CSV
df = pd.read_csv("data.csv")

# --- COLUMN SELECTION ---

# Selecting a single column
print("Name column:\n", df["Name"])
print("\nFull Name column:\n", df["Name"].to_string())
print("\nFull Height column:\n", df["Height"].to_string())
print("\nFull Weight column:\n", df["Weight"].to_string())

# Selecting multiple columns
selected_columns = df[["Name", "Height", "Weight"]]
print("\nSelected columns:\n", selected_columns)
print("\nFull selected columns:\n", selected_columns.to_string())

# --- ROW SELECTION ---

# Selecting a row by position
print("\nRow at index 0:\n", df.loc[0])

# Setting 'Name' as index for label-based selection
df_indexed = pd.read_csv("data.csv", index_col="Name")
print("\nDataFrame with 'Name' as index:\n", df_indexed)

# Selecting a row by label
print("\nData for Pikachu:\n", df_indexed.loc["Pikachu"])

# Selecting specific columns for a row
print("\nHeight and Weight of Charizard:\n", df_indexed.loc["Charizard", ["Height", "Weight"]])

# Selecting a range of rows by label
print("\nHeight and Weight from Charizard to Blastoise:\n", df_indexed.loc["Charizard":"Blastoise", ["Height", "Weight"]])

# --- INDEX-BASED SELECTION ---

# Selecting rows by position range
print("\nRows 0 to 10:\n", df_indexed.iloc[0:11])

# Selecting every second row in range
print("\nEvery second row from 0 to 10:\n", df_indexed.iloc[0:11:2])

# Selecting specific rows and columns by position
print("\nSubset of rows and columns:\n", df_indexed.iloc[0:11:2, 0:3])

# --- INTERACTIVE EXERCISE ---

pokemon = input("\nEnter a Pokémon name: ")

try:
    print("\nData for Pokémon:", pokemon)
    print(df_indexed.loc[pokemon])
except KeyError:
    print(f"{pokemon} not found")