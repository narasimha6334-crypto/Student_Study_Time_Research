from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import kruskal, spearmanr

# Project folders
PROJECT_DIR = Path(__file__).resolve().parent.parent
DATA_FILE = PROJECT_DIR / "raw" / "student-mat.csv"
REPORTS_DIR = PROJECT_DIR / "reports"
REPORTS_DIR.mkdir(parents=True, exist_ok=True)

# Load the dataset
df = pd.read_csv(DATA_FILE, sep=";")

# Validate required columns
required_columns = ["studytime", "G3"]
if not all(col in df.columns for col in required_columns):
    raise ValueError(
        f"Dataset must contain these columns: {required_columns}"
    )

# Select required variables and remove missing values
data = df[required_columns].dropna().copy()

# Remove invalid values
data = data[
    data["studytime"].isin([1, 2, 3, 4])
    & data["G3"].between(0, 20)
]

if data.empty or data["studytime"].nunique() < 2:
    raise ValueError("Insufficient valid data for statistical analysis.")

print("Dataset loaded successfully!")
print("Number of eligible records:", len(data))
print("Study-time categories:", sorted(data["studytime"].unique()))

# Kruskal-Wallis H test
groups = [
    group["G3"].to_numpy()
    for _, group in data.groupby("studytime", sort=True)
]

stat, p_value = kruskal(*groups)
k = len(groups)
n = len(data)

# Epsilon-squared effect size
epsilon_squared = max(0, (stat - k + 1) / (n - k))

print("\nKruskal-Wallis H Test")
print(f"H-statistic: {stat:.4f}")
print(f"p-value: {p_value:.4f}")
print(f"Epsilon-squared: {epsilon_squared:.4f}")

if p_value < 0.05:
    print("Result: Significant differences between study-time groups.")
else:
    print("Result: No statistically significant differences "
          "between study-time groups.")

# Spearman rank correlation
correlation, corr_p = spearmanr(
    data["studytime"],
    data["G3"]
)

print("\nSpearman Rank Correlation")
print(f"Correlation: {correlation:.4f}")
print(f"p-value: {corr_p:.4f}")

if corr_p < 0.05:
    print("Result: Statistically significant association.")
else:
    print("Result: No statistically significant association.")

# Save box plot in reports/
plt.figure(figsize=(8, 5))
data.boxplot(column="G3", by="studytime")

plt.title("Final Mathematics Grade by Study Time")
plt.suptitle("")
plt.xlabel("Weekly Study-Time Category")
plt.ylabel("Final Mathematics Grade (G3)")
plt.tight_layout()

plot_path = REPORTS_DIR / "study_time_G3_boxplot.png"
plt.savefig(plot_path, dpi=300, bbox_inches="tight")
plt.close()

print(f"\nBox plot saved to: {plot_path}")