# Analysis Preregistration

## Research Question

Is weekly study time associated with students' final mathematics grade?

## Hypotheses

Primary Analysis: Kruskal–Wallis H Test

Null hypothesis (H₀): The distributions of final mathematics grades (G3) are the same across the four weekly study-time categories.

Alternative hypothesis (H₁): At least one weekly study-time category differs in its distribution of final mathematics grades.

Secondary Analysis: Spearman Rank Correlation

Null hypothesis (H₀): There is no monotonic association between weekly study time and final mathematics grade.

Alternative hypothesis (H₁): There is a monotonic association between weekly study time and final mathematics grade.

## Population, Sample, and Exclusions

Target population: Students represented in the UCI Student Performance Mathematics dataset.

Unit of analysis: Individual student.

Sample: All student records in the dataset with valid values for "studytime" and "G3".

Inclusion rules: Students with valid values for "studytime" and "G3" will be included in the analysis.

Exclusion rules: Records with missing or invalid values for "studytime" or "G3" will be excluded.

Stopping rule: The complete eligible dataset will be used for the analysis.

## Variables and Measures

Outcome variable: "G3", the final mathematics grade, measured on a scale from 0 to 20.

Predictor variable: "studytime", an ordinal variable representing the student's weekly study-time category.

Control variables: No control variables will be used in the primary analysis.

Transformations: The "studytime" variable will be treated as an ordinal variable, and "G3" will be treated as a numerical variable. No transformation will be applied to "G3".

Missing-data handling: Records with missing values in "studytime" or "G3" will be excluded. No missing values will be imputed.

## Analysis Plan

Primary analysis: A Kruskal–Wallis H test will be used to compare final mathematics grade distributions across the four study-time categories.

Secondary analysis: Spearman rank correlation will be used to assess the direction and strength of the monotonic association between weekly study time and final mathematics grade.

Significance level: The significance level will be set at α = 0.05.

Effect size: Epsilon-squared will be calculated and reported as an effect-size measure for the Kruskal–Wallis test, with the formula documented in the analysis code.

Uncertainty intervals: Where applicable, 95% confidence intervals will be reported for effect estimates. Any intervals not calculated will be documented as a limitation or deviation from the planned analysis.

Robustness check: Spearman rank correlation will provide a secondary assessment of the relationship between weekly study time and final mathematics grade.

Visualization: Box plots will be used to compare the distributions of final mathematics grades across the four study-time categories.

## Deviations and Amendments

This document records the planned analysis. Any changes made after the preregistration will be documented transparently, including the date of the change, the reason for the change, and its potential impact on the analysis and interpretation of the results. The original preregistration will be retained for transparency.