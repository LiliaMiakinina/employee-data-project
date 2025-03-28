import csv
import sys

def filter_by_month(database_file, month):
    try:
        with open(database_file, mode="r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            print(f"\nEmployees hired in {month} month:\n")

            found = False
            for row in reader:
                hiring_month = int(row["hiring_date"].split("-")[1])
                if hiring_month == int(month):
                    print(f"{row['name']} | Hiring date: {row['hiring_date']} | Department: {row['department']}")
                    found = True

            if not found:
                print("No employees were hired in this month.")

    except FileNotFoundError:
        print("Database file not found!")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python report.py database.csv <month_number>")
    else:
        filter_by_month(sys.argv[1], sys.argv[2])