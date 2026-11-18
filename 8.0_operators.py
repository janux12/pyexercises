"""Exercise 8.0 — Operators (bonus, not graded)

WHAT THE PROGRAM MUST DO
    Take two values of your choice and display, as a readable table, the result of every
    comparison between them and of the logical combinations of those results.

ANSWER THESE FIRST, in comments
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. Which two values did you pick, and which comparison result surprised you?

WHAT THE AI CANNOT KNOW
    Your two values. Pick a pair where the answer is not obvious: two strings with
    different capitalisation, a number and the same number written as text, or zero and
    an empty string.

CHECK IT YOURSELF
    Predict each result before running. Count how many you got right.

DELIVERABLE
    This file, with your comments and your code.
"""

# Your code below
# 1. What goes in?
# Two strings: "Python" and "python"

# 2. What happens to it?
# Python compares the two strings using comparison operators
# and combines the results using logical operators.

# 3. What comes out?
# A table showing True or False for each comparison.

# 4. Which two values did you pick?
# I picked "Python" and "python".
# The surprising result is that "Python" is not equal to "python"
# because Python is case-sensitive.

value1 = "Python"
value2 = "python"

print("Comparison results")
print("------------------------------")

print("Equal:", value1 == value2)
print("Not equal:", value1 != value2)
print("Greater than:", value1 > value2)
print("Less than:", value1 < value2)
print("Greater or equal:", value1 >= value2)
print("Less or equal:", value1 <= value2)

print("------------------------------")
print("Logical combinations")

print("AND:", value1 == value2 and value1 != value2)
print("OR:", value1 == value2 or value1 != value2)
print("NOT:", not (value1 == value2))
