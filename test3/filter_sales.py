import pandas as pd

# Load CSV
df = pd.read_csv("Assignment python.csv")

# Use actual column names: 'price' and 'sq__ft'
df["PricePerFoot"] = df["price"] / df["sq__ft"]

# Calculate average price per foot
avg_price_per_foot = df["PricePerFoot"].mean()

# Filter rows
filtered = df[df["PricePerFoot"] < avg_price_per_foot]

# Save to new CSV
filtered.to_csv("below_average_price_per_foot.csv", index=False)

print("Filtered CSV created: below_average_price_per_foot.csv")
