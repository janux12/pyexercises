"""Exercise 4.1 — Reordering without losing the original (homework)

WHAT THE PROGRAM MUST DO
    Starting from the list you built in exercise 4.0, display it in four different
    orders, and prove at the end that the original list has not been damaged.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. Which four orders did you choose, and in which of them is your original list
       modified rather than copied?

WHAT THE AI CANNOT KNOW
    That your original must survive. Some ways of reordering a list change it in place,
    others return a new one. Find out which is which, and say so in your comments.
    That distinction is the entire exercise.

CHECK IT YOURSELF
    The last line of your program must display the original list. Compare it, item by
    item, with what you wrote in 4.0. If it has moved, your program is wrong even
    though it ran.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In:A list of marketing campaign budgets.
# 2. Process:The program displays the list in four different orders.
# 3. Out:Four different orders and the original list at the end.
# 4. My four orders, and which ones modify the original:My four orders, and which ones modify the original:
# sorted() and sorted(..., reverse=True) create copies.
# sort() and reverse() modify the original list.


# Your code below
budgets = [100, 200, 150, 300, 250, 400, 350, 500]

print("The original list")
print(budgets)

print("The list sorted")
print(sorted(budgets))

print("The list sorted from highest to lowest")
print(sorted(budgets, reverse=True))

print("The list sorted using sort()")
budgets_copy = budgets.copy()
budgets_copy.sort()
print(budgets_copy)

print("The list in reverse order")
budgets_copy = budgets.copy()
budgets_copy.reverse()
print(budgets_copy)

print("The original list at the end")
print(budgets)

# Check: The original list stayed the same.
# Check: sorted() created new sorted lists.
# Check: sort() changed the copy, not the original.
# Check: reverse() changed the copy, not the original.