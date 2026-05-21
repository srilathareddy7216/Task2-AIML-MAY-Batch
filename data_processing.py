import pandas as pd
import numpy as np

# Load the dataset
df = pd.read_csv("student_scores.csv")

print("\n------------------------------")
print("🔹 Original Data Loaded")
print("------------------------------")
print(df.head())

# 1. Identify & handle missing values
print("\n🔹 Missing Values Before Handling:")
print(df.isnull().sum())

# Replace "twenty" etc. in age with NaN, then convert
df["age"] = pd.to_numeric(df["age"], errors="coerce")

# Convert numeric columns with errors to NaN
numeric_columns = ["math_score", "science_score", "attendance"]
for col in numeric_columns:
    df[col] = pd.to_numeric(df[col], errors="coerce")

# Fill missing numeric values with the column mean
df[numeric_columns] = df[numeric_columns].fillna(df[numeric_columns].mean())

print("\n🔹 Missing Values After Handling:")
print(df.isnull().sum())

# 2. Convert incorrect data formats
# Gender formatting (capitalize males/females)
df["gender"] = df["gender"].str.capitalize()

# Strip spaces in names/columns
df["name"] = df["name"].str.strip()

# 3. Convert exam_date to datetime
df["exam_date"] = pd.to_datetime(df["exam_date"], errors="coerce", dayfirst=True)

print("\n🔹 Exam Date Converted to Datetime:")
print(df["exam_date"].head())

# 4. Detect & handle outliers in math_score, science_score

def remove_outliers(col):
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3 - Q1
    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR
    return df[(df[col] >= lower) & (df[col] <= upper)]

print("\n🔹 Removing outliers in math_score...")
df = remove_outliers("math_score")

print("🔹 Removing outliers in science_score...")
df = remove_outliers("science_score")

# 5. Find & remove duplicate rows
duplicates = df.duplicated().sum()
print(f"\n🔹 Duplicate Rows Found: {duplicates}")

df = df.drop_duplicates()

print("\n🔹 Duplicate Rows Removed Successfully.")

# Final Cleaned Dataset
print("\n------------------------------")
print("🔹 Cleaned Data (First 10 Rows)")
print("------------------------------")
print(df.head(10))

# Save cleaned file
df.to_csv("student_scores_cleaned.csv", index=False)
print("\n Cleaned dataset saved as student_scores_cleaned.csv")