import pandas as pd

# Load cleaned dataset
df = pd.read_csv("student_scores_cleaned.csv")

# 1. Create new column: average_score
df["average_score"] = df[["math_score", "science_score"]].mean(axis=1)

print("\n New Column 'average_score' Added:")
print(df.head())

# 2. Top 5 students by average_scores
top5 = df.sort_values(by="average_score", ascending=False).head(5)

print("\n Top 5 Students Based on Average Score:")
print(top5[["name", "math_score", "science_score", "average_score"]])


# 3. Correlation between attendance and marks
correlation = df[["attendance", "math_score", "science_score", "average_score"]].corr()

print("\n Correlation Between Attendance and Marks:")
print(correlation)

# 4. Group students by gender
gender_group = df.groupby("gender").agg({
    "math_score": "mean",
    "science_score": "mean",
    "attendance": "mean",
    "average_score": "mean",
    "name": "count"
}).rename(columns={"name": "total_students"})

print("\n Grouped Data by Gender (Averages + Count):")
print(gender_group)