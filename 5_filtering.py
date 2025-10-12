import pandas as pd

# Filtering: Filtering allows you to extract rows from a DataFrame that meet specific conditions.

# Load the dataset
df = pd.read_csv("data.csv")

# Filter Pokémon with height greater than or equal to 2
tall_pokemon = df[df["Height"] >= 2]
print("\nTall Pokémon (Height >= 2):\n",tall_pokemon)

# Filter Pokémon with weight greater than or equal to 100
heavy_pokemon = df[df["Weight"] >= 100]
print(heavy_pokemon)

# legendary_pokemon = df[df["Legendary"] == 1]
legendary_pokemon = df[df["Legendary"] == True]
print(legendary_pokemon)


water_pokemon = df[(df["Type1"] == "Water") | (df["Type2"] == "Water")]
print(water_pokemon)

# Filter Pokémon that are Fire/Flying type combo
ff_pokemon = df[(df["Type1"] == "Fire") & (df["Type2"] == "Flying")]
print(ff_pokemon)