#Write program to read subject and marks as input. Calculate total marks.
#Store all data in a csv file.



#1

# Program to read subject and marks, calculate total, and store in a CSV file

import csv

def store_marks():
    # Step 1: Ask how many subjects
    n = int(input("Enter number of subjects: "))

    subjects = []
    marks = []
    total = 0

    # Step 2: Read subject names and marks
    for i in range(n):
        subject = input(f"Enter subject {i+1} name: ")
        mark = int(input(f"Enter marks for {subject}: "))
        subjects.append(subject)
        marks.append(mark)
        total += mark

    # Step 3: Define filename
    filename = "marks.csv"

    try:
        # Step 4: Write data to CSV file
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)

            # Write header row
            writer.writerow(["Subject", "Marks"])

            # Write subject-wise marks
            for i in range(n):
                writer.writerow([subjects[i], marks[i]])

            # Write total marks
            writer.writerow(["Total", total])

        print(f"Marks saved successfully in '{filename}'")

    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
store_marks()
