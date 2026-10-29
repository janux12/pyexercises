"""Exercise 5.1 — Doing the same thing to every item

WHAT THE PROGRAM MUST DO
    Take the list you built in exercise 4.0 and, for every item, display a line that
    combines the item, its position, and something computed about it.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What did you compute for each item, and what does the reader learn from that line?

WHAT THE AI CANNOT KNOW
    Your list from 4.0, and what is worth computing about its items. Length of the name,
    share of a total, position in a ranking, whether the item passes a threshold you set.
    Open your 4.0 file, copy the list across, and say in a comment what you decided.

CHECK IT YOURSELF
    Count the lines your program Printed. There must be exactly as many as items in your
    list. If there is one more or one less, you have an off-by-one, and it is worth
    understanding now rather than in the exam.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In:A list of numbers from exercise 4.0.
# 2. Process:The program displays each number, its position, and its double.
# 3. Out:One line for each number in the list.
# 4. What I compute for each item, and why it is worth showing:I calculate double each number to see its value multiplied by 2.


# Your code below

list_of_numbers = [10, 9, 1, 7, 8, 6, 2, 3, 4, 5]

for i in range(len(list_of_numbers)):
    print(list_of_numbers[i], "position", i + 1, "double", list_of_numbers[i] * 2)

# Check: The program printed 10 lines for 10 numbers.
# Check: The first number is 10, its position is 1, and its double is 20.
# Check: The second number is 9, its position is 2, and its double is 18.
# Check: The third number is 1, its position is 3, and its double is 2.