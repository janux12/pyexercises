"""Exercise 5.2 — Repeating until something changes

WHAT THE PROGRAM MUST DO
    Keep asking the user something until a condition you define is met, then display a
    summary of what happened during the loop.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What is your stop condition, what is your maximum number of attempts, and what
       does your summary contain?

WHAT THE AI CANNOT KNOW
    Your stop condition and your safety limit. An assistant asked for a while loop will
    write one that can run for ever if the user never gives the expected answer. Decide
    how many attempts you allow, and what your program does when that limit is reached.

    Accepting "Yes", "yes" and " yes " as the same answer is your decision too. Make it
    And write it down.

CHECK IT YOURSELF
    Run it and never give the expected answer. If your program is still running after
    your stated maximum, it is wrong. Then run it and answer with capitals and extra
    spaces.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In:An answer entered by the user.
# 2. Process:The program repeats the question until the user types yes or reaches 5 attempts.
# 3. Out:A message and a summary of the attempts.
# 4. My stop condition, my attempt limit, my summary: My stop condition is typing yes. The maximum is 5 attempts.
# The summary shows the number of attempts.


# Your code below
answer = ""
attempts = 0

while answer != "yes" and attempts < 5:
    answer = input("Type yes to stop: ")
    answer = answer.strip().lower()
    attempts = attempts + 1

print("The loop has finished")
print("Number of attempts:", attempts)

if answer == "yes":
    print("You found the correct answer")
else:
    print("You reached the maximum number of attempts")


# Check: YES with extra spaces is accepted.
# Check: The program stops after 5 incorrect attempts.
# Check: The summary displays the number of attempts.