import pandas as pd

# Data Cleaning: the process of fixing/removing
# incomplete, incorrect, or irrelevant data.
# ~75% of work done with Pandas is data cleaning

df = pd.read_csv("data.csv")

# 1. Drop irrelevant columns
# df = df.drop(columns=["Legendary", "No"])

# 2. Handle missing data

# Drop rows where Type2 is missing
df2 = df.dropna(subset=["Type2"])
print("\nRows with non-null Type2:\n", df2.to_string())

# Replace missing Type2 values with 'None'
df3 = df.fillna({"Type2": "None"})
print("\nMissing Type2 replaced with 'None':\n", df3.to_string())

# Fill all missing numeric values with 0 (if any)
df_filled = df.fillna(0)
print("\nAll missing numeric values filled with 0:\n", df_filled.to_string())

# 3. Fix inconsistent values

# Normalize Type1 values
df["Type1"] = df["Type1"].replace({
    "Grass": "GRASS",
    "Fire": "FIRE",
    "Water": "WATER"
})
print("\nNormalized Type1 values:\n", df.to_string())

# 4. Standardize text

# Convert all names to lowercase
df["Name"] = df["Name"].str.lower()
print("\nStandardized lowercase names:\n", df)

# Strip leading/trailing whitespace from all string columns
df = df.apply(lambda col: col.str.strip() if col.dtype == "object" else col)
print("\nWhitespace removed from string columns:\n", df.to_string())

# 5. Fix data types

# Convert Legendary column to boolean
df["Legendary"] = df["Legendary"].astype(bool)
print("\nLegendary column as boolean:\n", df.to_string())

# Convert 'Height' and 'Weight' to float (if needed)
df["Height"] = df["Height"].astype(float)
df["Weight"] = df["Weight"].astype(float)

# 6. Remove duplicate values

df = df.drop_duplicates()
print("\nData after removing duplicates:\n", df.to_string())

# 7. Reset index after cleaning
df = df.reset_index(drop=True)
print("\nFinal cleaned DataFrame with reset index:\n", df.to_string())