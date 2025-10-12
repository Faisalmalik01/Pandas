import pandas as pd

# Aggregate functions: Reduce a set of values into a single summary value.
# Used to summarize and analyze data, often with groupby().

df = pd.read_csv("data.csv")

# --- Aggregation on entire DataFrame ---
print("\nMean of all numeric columns:\n", df.mean(numeric_only=True))
print("\nSum of all numeric columns:\n", df.sum(numeric_only=True))
print("\nMinimum values:\n", df.min(numeric_only=True))
print("\nMaximum values:\n", df.max(numeric_only=True))
print("\nCount of non-null entries per column:\n", df.count())

# --- Aggregation on single column ---
print("\nHeight column statistics:")
print("Mean:", df["Height"].mean())
print("Sum:", df["Height"].sum())
print("Min:", df["Height"].min())
print("Max:", df["Height"].max())
print("Non-null count in Type2:", df["Type2"].count())

# --- Grouped Aggregation ---
group = df.groupby("Type1")

print("\nMean Height by Type1:\n", group["Height"].mean())
print("\nSum of Height by Type1:\n", group["Height"].sum())
print("\nMinimum Height by Type1:\n", group["Height"].min())
print("\nCount of Height entries by Type1:\n", group["Height"].count())

# --- Additional Aggregation Techniques ---

# Aggregating multiple columns
print("\nMean of Height and Weight by Type1:\n", group[["Height", "Weight"]].mean())

# Applying multiple functions using .agg()
print("\nMultiple stats on Height:\n", group["Height"].agg(["mean", "min", "max", "count"]))

# Custom aggregation: range of Height
print("\nHeight range by Type1:\n", group["Height"].agg(lambda x: x.max() - x.min()))

# Aggregating multiple columns with multiple functions
print("\nHeight and Weight stats by Type1:\n", group[["Height", "Weight"]].agg(["mean", "sum", "max"]))

# Sorting aggregated results
print("\nSorted average Height by Type1:\n", group["Height"].mean().sort_values(ascending=False))

# Resetting index after aggregation
height_summary = group["Height"].mean().reset_index()
print("\nHeight summary with reset index:\n", height_summary)