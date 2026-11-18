"""Exercise 9.0 — Surviving what you did not expect

Useful for the final exam: two campaigns in the exam dataset have zero conversions.

WHAT THE PROGRAM MUST DO
    Ask the user for a number, divide something by it, and keep running whatever the
    user types. Never crash.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. Which two different failures can happen here, and should they produce the same
       message to the user? Decide before coding.

WHAT THE AI CANNOT KNOW
    Your answer to question 4, and how many attempts you allow before giving up.

    An assistant will often propose catching every error at once. Find out why catching
    each failure separately is better, and write the reason in a comment.

CHECK IT YOURSELF
    Run it with: a normal number, then zero, then the word "abc", then an empty line.
    Four runs, four behaviours, all described in a comment. If any of them stopped your
    program, it is not finished.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In:
# 2. Process:
# 3. Out:
# 4. The two failures, and whether they deserve the same message:


# Your code below

# 1. What goes in?
# The user enters a number.

# 2. What happens to it?
# Python converts the input into a number and divides 100 by it.

# 3. What comes out?
# The result of the division or an error message.

# 4. The two failures, and whether they deserve the same message:
# The first failure is entering text instead of a number.
# The second failure is entering zero.
# They should have different messages because the problems are different.

# Catching each error separately is better because we can
# give the user a clear message for each problem.

# The program allows 3 attempts.

# Check:
# 1. Entering 10 gives the result 10.0.
# 2. Entering 0 displays a division by zero message.
# 3. Entering abc displays an invalid number message.
# 4. Pressing Enter without typing displays an empty input message.


for i in range(3):
    try:
        number = input("Enter a number: ")

        if number == "":
            raise ValueError

        number = float(number)

        result = 100 / number

        print("Result:", result)
        break

    except ZeroDivisionError:
        print("You cannot divide by zero.")

    except ValueError:
        print("Please enter a valid number.")

else:
    print("You have used all your attempts.")
