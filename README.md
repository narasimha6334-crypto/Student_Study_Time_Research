Student Study Time Research

Project Overview

This project investigates whether weekly study time is associated with students' final mathematics grades using statistical analysis in Python.

Research Question

Is weekly study time associated with students' final mathematics grade?

Dataset

The dataset is the UCI Student Performance Mathematics dataset.

- Sample size: 395 student records
- Predictor: "studytime" — weekly study-time category
- Outcome: "G3" — final mathematics grade, measured on a scale of 0–20

Methods

1. Kruskal–Wallis H test: Compares final mathematics grades across study-time categories.
2. Spearman rank correlation: Measures the direction and strength of the ordinal association between study time and final mathematics grade.
3. Effect size: Epsilon-squared is reported for the Kruskal–Wallis test.
4. Visualization: A box plot compares final mathematics grades across study-time categories.

The significance level is 0.05.

Results

Measure| Result
Number of records| 395
Kruskal–Wallis H statistic| 7.5789
Kruskal–Wallis p-value| 0.0556
Epsilon-squared| 0.0117
Spearman correlation| 0.1052
Spearman p-value| 0.0367

Conclusion

The Kruskal–Wallis test did not find statistically significant differences in final mathematics grades across study-time categories at the 0.05 significance level.

Spearman correlation showed a statistically significant but very weak positive association between weekly study time and final mathematics grade. This association does not establish causation.

Project Structure

- "pre-registration/" — Analysis preregistration
- "raw/" — Original dataset files
- "src/analysis.py" — Statistical analysis code
- "reports/" — Generated box plot

Requirements

Python 3, pandas, SciPy, and Matplotlib.

How to Run

From the project root directory, run:

python src/analysis.py

The script reads the dataset from "raw/student-mat.csv" and saves the box plot in "reports/".

Reproducibility

The analysis uses the specified dataset, documented hypotheses, and statistical methods. The preregistration records the planned analysis.s