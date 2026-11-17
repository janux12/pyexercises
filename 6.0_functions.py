"""Exercise 6.0 — Naming a piece of work

WHAT THE PROGRAM MUST DO
    Write a function that computes something useful about the list you built in exercise
    4.0, then call it three times with different inputs and display the three results.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?  (what your function receives)
    2. What happens to it?
    3. What comes out?  (what your function returns)
    4. What is your function called, and does its name say what it does without reading
       the code?

WHAT THE AI CANNOT KNOW
    What is worth computing about your data, and what to call it. A function named
    "process" or "do_stuff" fails this exercise even if it works.

    Your function must RETURN its result, not print it. Find out why that difference
    matters and write the reason in a comment. It is the whole point of the exercise.

CHECK IT YOURSELF
    Call your function with an empty list. Note what happens. Then decide whether that
    behaviour is acceptable, and say so in a comment.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In:
# 2. Process:
# 3. Out:
# 4. My function name, and why return rather than print:


# Your code below
# Your code below

campaign_budgets = [100, 200, 150, 300, 250, 400, 350, 500]

def count_above_limit(budgets, limit):
    count = 0
    for budget in budgets:
        if budget > limit:
            count = count + 1
    return count


result_1 = count_above_limit(campaign_budgets, 200)
result_2 = count_above_limit(campaign_budgets, 300)
result_3 = count_above_limit(campaign_budgets, 400)

print(result_1)
print(result_2)
print(result_3)


# Test with an empty list

empty_list = []
result_empty = count_above_limit(empty_list, 200)

print(result_empty)

# The result is 0 because the list is empty.
# This behaviour is acceptable because there are no budgets to count.
