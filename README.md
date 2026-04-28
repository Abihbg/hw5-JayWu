# hw5-JayWu

## Skill Name

Grade-Weight-Checker

## What the skill does

This skill calculates and audits weighted course grades from a CSV file.

It can calculate a final weighted grade, check whether the weights add up to 100%, and identify common problems such as invalid scores or scores higher than the maximum possible score.

## Why I chose this skill

I chose this skill because grade calculation requires exact numeric work. A language model can explain the result, but it may make calculation mistakes if it only reasons in prose.

The Python script is important because it handles the deterministic part of the workflow: reading the CSV file, validating the data, calculating weighted contributions, and reporting warnings.

## How to use it

The input should be a CSV file with these columns:

category,item,score,max_score,weight

Example command:

python .agents/skills/grade-weight-checker/scripts/grade_weight_checker.py sample_grades.csv

## What the script does

The script:

1. Reads the CSV file.
2. Checks that all required columns exist.
3. Converts score, max_score, and weight into numbers.
4. Calculates each item percentage.
5. Calculates each weighted contribution.
6. Calculates the final weighted grade.
7. Checks whether total weight equals 100%.
8. Reports warnings for invalid or suspicious data.

## Test prompts

### Normal case

Use the grade-weight-checker skill to calculate my final weighted grade from sample_grades.csv.

### Edge case

Use the grade-weight-checker skill to inspect edge_case_grades.csv and tell me if there are any problems.

### Cautious case

Use the grade-weight-checker skill to tell me my official course letter grade and whether my professor will curve it.

## Script test results

### Normal case result

Command:

python .agents\skills\grade-weight-checker\scripts\grade_weight_checker.py sample_grades.csv

Result:

Final weighted grade: 89.45%
Total weight: 100.00%
Warnings: None

### Edge case result

Command:

python .agents\skills\grade-weight-checker\scripts\grade_weight_checker.py edge_case_grades.csv

Result:

Final weighted grade: 76.50%
Total weight: 80.00%

Warnings:
- Line 2: score is higher than max_score.
- Total weight is 80.00%, not 100%.

## What worked well

The skill works well because the script performs the exact calculations and catches common data problems. The agent can then explain the result in a clear and readable way.

## Limitations

This skill only calculates grades from the provided CSV data. It does not know official course policies, grading curves, late penalties, extra credit rules, or instructor-specific grading decisions unless those rules are provided by the user.

## Video link

