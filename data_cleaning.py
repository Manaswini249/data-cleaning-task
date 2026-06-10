import pandas as pd

df = pd.read_csv("raw_data.csv")

print("Original Dataset")
print(df)

# Remove duplicates
df = df.drop_duplicates()

# Fill missing names
df["Name"] = df["Name"].fillna("Unknown")

# Fill missing age
avg_age = df["Age"].mean()
df["Age"] = df["Age"].fillna(avg_age)

# Standardize dates
df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
df["Date"] = df["Date"].dt.strftime("%Y-%m-%d")

# Validate structure
required_columns = ["ID","Name","Age","Email","Date"]

for col in required_columns:
    if col not in df.columns:
        print("Missing:", col)

df.to_csv("cleaned.csv", index=False)

print("\nCleaned Dataset")
print(df)

print("\nTask Completed Successfully")
