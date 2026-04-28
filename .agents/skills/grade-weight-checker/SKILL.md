---
name: grade-weight-checker
description: Calculates and audits weighted course grades from a CSV file. Use when the user asks to calculate a final weighted grade, check whether assignment weights add up correctly, or identify problems such as missing scores, invalid scores, or scores above the maximum.
---

# Grade Weight Checker Skill

## Purpose

This skill helps inspect a course grade CSV file, calculate the weighted final grade, and identify common data problems.

The Python script is required because grade calculation needs exact numeric work. The model can explain the result, but the script should handle the calculation and validation.

## When to use this skill

Use this skill when the user provides a weighted course grade table and wants to:

- calculate a final weighted grade
- check whether weights add up to 100%
- find invalid or suspicious scores
- produce a short grade report

## When not to use this skill

Do not use this skill to:

- predict future grades without enough data
- decide an official letter grade without a grading scale
- guess whether a professor will curve grades
- interpret school policy that the user did not provide

## Expected input

The expected input is a CSV file with these columns:

category,item,score,max_score,weight

Example:

category,item,score,max_score,weight
Exam,Midterm Exam,85,100,25
Project,Final Project,92,100,35
Quiz,Quiz Average,18,20,20
Participation,Class Participation,9,10,20

## Step-by-step instructions

1. Confirm that the user provided a CSV file or CSV-style grade data.
2. Check that the expected columns are present.
3. Run the Python script in the scripts folder.
4. Use the script output as the source of truth for calculations.
5. Summarize the final weighted grade and any warnings.

## Expected output format

The response should include:

- Final weighted grade
- Total weight
- Warnings, if any
- Short explanation

## Limitations

This skill only calculates grades from the provided data. It does not know grading curves, late penalties, extra credit rules, or official course policies unless the user provides them.
