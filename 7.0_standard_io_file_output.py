"""Exercise 7.0 — Collecting data and saving it

WHAT THE PROGRAM MUST DO
    Ask the user for the information needed to record one entry, then save it to a CSV
    file. Running the program twice must produce two entries, not overwrite the first.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?  (name your file, and list your columns)
    4. Which columns did you choose, and what would you actually do with this file once
       it has two hundred rows in it?

WHAT THE AI CANNOT KNOW
    Your columns. They must be the ones you would really need to collect for a purpose
    you can state. See 7.0_student_data.csv for the shape of a header line, not for
    the columns to use.

    Two behaviours are yours to decide, and an assistant will guess them wrong:
    what happens the very first time, when the file does not exist yet and needs its
    header line, and what happens when a value the user typed is not acceptable.

CHECK IT YOURSELF
    Run your program three times with different values. Then open the file and count
    the lines. You should have three entries and exactly one header line. If you have
    three header lines, or one entry, your program is wrong.

DELIVERABLE
    This file, plus the CSV your program produced.
"""

# 1. In: The date, subject, topic, minutes studied and confidence level.
# 2. Process: The program collects the information and saves it in a CSV file.
# 3. Out: study_sessions.csv with date, subject, topic, minutes and confidence.
# 4. I chose these columns to track my studying. With 200 rows, I could compare subjects and see how much time I spend studying each subject.


# Your code below
import csv
import os

file_name = "study_sessions.csv"

date = input("Enter the date: ")
subject = input("Enter the subject: ")
topic = input("Enter the topic studied: ")

minutes = int(input("Enter the number of minutes studied: "))

while minutes <= 0:
    print("Minutes must be greater than 0.")
    minutes = int(input("Enter the number of minutes studied: "))

confidence = int(input("Enter your confidence level (1 to 5): "))

while confidence < 1 or confidence > 5:
    print("Confidence must be between 1 and 5.")
    confidence = int(input("Enter your confidence level (1 to 5): "))

# Check if the file already exists
file_exists = os.path.exists(file_name)

# Open the file in append mode
with open(file_name, "a", newline="") as file:
    writer = csv.writer(file)

    # Write the header only if the file is new
    if not file_exists:
        writer.writerow(["date", "subject", "topic", "minutes", "confidence"])

    # Save the study session
    writer.writerow([date, subject, topic, minutes, confidence])

print("Study session saved successfully!")

