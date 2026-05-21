import pandas as pd
import numpy as np

# Load CSV file
df = pd.read_csv("student_scores.csv")

# Convert math_score column to numeric (handles '999', blanks, text, etc.)
df["math_score"] = pd.to_numeric(df["math_score"], errors="coerce")

# Remove rows where math_score is NaN
math_scores = df["math_score"].dropna().to_numpy()

print("Math Score Array:")
print(math_scores)

# ---- NUMPY OPERATIONS ----

# Mean
mean_score = np.mean(math_scores)
# Median
median_score = np.median(math_scores)
# Max
max_score = np.max(math_scores)
# Min
min_score = np.min(math_scores)

print("\n--- Statistics ---")
print("Mean:", mean_score)
print("Median:", median_score)
print("Max:", max_score)
print("Min:", min_score)

# ---- NORMALIZATION ----

# Min–Max normalization
norm_minmax = (math_scores - min_score) / (max_score - min_score)

# Z-score normalization
norm_zscore = (math_scores - mean_score) / np.std(math_scores)

print("\n--- Min-Max Normalized Scores ---")
print(norm_minmax)

print("\n--- Z-Score Normalized Scores ---")
print(norm_zscore)