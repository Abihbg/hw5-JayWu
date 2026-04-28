import csv
import sys
from pathlib import Path


REQUIRED_COLUMNS = ["category", "item", "score", "max_score", "weight"]


def read_csv(file_path):
    rows = []

    with open(file_path, "r", encoding="utf-8-sig", newline="") as file:
        reader = csv.DictReader(file)

        if reader.fieldnames is None:
            raise ValueError("The CSV file is empty.")

        missing_columns = [col for col in REQUIRED_COLUMNS if col not in reader.fieldnames]
        if missing_columns:
            raise ValueError(f"Missing required columns: {', '.join(missing_columns)}")

        for row in reader:
            rows.append(row)

    return rows


def analyze_grades(rows):
    warnings = []
    results = []
    total_weight = 0.0
    weighted_grade = 0.0

    for line_number, row in enumerate(rows, start=2):
        category = row["category"].strip()
        item = row["item"].strip()

        try:
            score = float(row["score"])
            max_score = float(row["max_score"])
            weight = float(row["weight"])
        except ValueError:
            warnings.append(f"Line {line_number}: score, max_score, and weight must be numeric.")
            continue

        if max_score <= 0:
            warnings.append(f"Line {line_number}: max_score must be greater than zero.")
            continue

        if score < 0:
            warnings.append(f"Line {line_number}: score cannot be negative.")

        if score > max_score:
            warnings.append(f"Line {line_number}: score is higher than max_score.")

        if weight < 0:
            warnings.append(f"Line {line_number}: weight cannot be negative.")

        percentage = score / max_score * 100
        contribution = percentage * weight / 100

        total_weight += weight
        weighted_grade += contribution

        results.append({
            "category": category,
            "item": item,
            "percentage": percentage,
            "weight": weight,
            "contribution": contribution
        })

    if abs(total_weight - 100) > 0.01:
        warnings.append(f"Total weight is {total_weight:.2f}%, not 100%.")

    return weighted_grade, total_weight, results, warnings


def print_report(weighted_grade, total_weight, results, warnings):
    print("GRADE WEIGHT CHECK REPORT")
    print("=" * 30)
    print(f"Final weighted grade: {weighted_grade:.2f}%")
    print(f"Total weight: {total_weight:.2f}%")
    print()

    print("Breakdown:")
    for result in results:
        print(
            f"- {result['category']} / {result['item']}: "
            f"{result['percentage']:.2f}% x {result['weight']:.2f}% "
            f"= {result['contribution']:.2f}%"
        )

    print()

    if warnings:
        print("Warnings:")
        for warning in warnings:
            print(f"- {warning}")
    else:
        print("Warnings: None")


def main():
    if len(sys.argv) != 2:
        print("Usage: python grade_weight_checker.py <csv_file>")
        sys.exit(1)

    file_path = Path(sys.argv[1])

    if not file_path.exists():
        print(f"Error: File not found: {file_path}")
        sys.exit(1)

    try:
        rows = read_csv(file_path)
        weighted_grade, total_weight, results, warnings = analyze_grades(rows)
        print_report(weighted_grade, total_weight, results, warnings)
    except Exception as error:
        print(f"Error: {error}")
        sys.exit(1)


if __name__ == "__main__":
    main()
