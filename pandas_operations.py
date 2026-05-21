import pandas as pd

# Load the dataset
df = pd.read_csv("student_scores.csv")

# 1. Display first 5 rows
print("\n First 5 Rows:")
print(df.head())

# 2. Check data types
print("\n Data Types:")
print(df.dtypes)

# 3. Missing values in each column
print("\n Missing Values Per Column:")
print(df.isnull().sum())

# 4. Students with attendance < 70%
# Convert attendance to numeric (because some values appear mixed)
df["attendance"] = pd.to_numeric(df["attendance"], errors="coerce")

low_attendance = df[df["attendance"] < 70]

print("\n Students with attendance below 70%:")
print(low_attendance)