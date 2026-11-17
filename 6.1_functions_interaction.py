"""Exercise 6.1 — Small functions working together

(Original instructions kept for reference: write three small functions, each doing
one thing, and a fourth that uses the other three to answer one question about
your data.)
"""

# 1. In:
#    A list of campaign budgets (numbers), the same list as in exercises 4.0 and 6.0.
#
# 2. Process, function by function:
#    - total_budget(budgets): adds up all the budgets.
#    - highest_budget(budgets): finds the largest single budget.
#    - percentage(part, whole): turns "part out of whole" into a percentage.
#    - biggest_campaign_share(budgets): the fourth function. It calls, in this
#      order: total_budget, then highest_budget, then percentage (biggest budget
#      as a share of the total), and rounds the result to one decimal.
#
# 3. Out:
#    biggest_campaign_share returns one number: the percentage of my total budget
#    that goes to my most expensive campaign.
#
# 4. The question my fourth function answers:
#    "How much of my total marketing budget depends on my single biggest
#    campaign?" If that share is very high, my spending is risky, because one
#    campaign carries too much of it.
#    Splitting it into three makes it easier to check because I can test each
#    small piece alone on a tiny input where I already know the right answer.
#    If the final answer is wrong, I know which of the three to look at, instead
#    of searching through one long function.


def total_budget(budgets):
    """Return the sum of all budgets."""
    return sum(budgets)


def highest_budget(budgets):
    """Return the largest budget in the list."""
    if len(budgets) == 0:
        raise ValueError("highest_budget needs at least one budget")
    return max(budgets)


def percentage(part, whole):
    """Return part as a percentage of whole."""
    if whole == 0:
        raise ValueError("percentage needs a whole that is not zero")
    return part / whole * 100


def biggest_campaign_share(budgets):
    """Return the percentage of the total budget taken by the biggest campaign."""
    total = total_budget(budgets)
    biggest = highest_budget(budgets)
    return round(percentage(biggest, total), 1)


# CHECK IT YOURSELF: testing each small function on its own first
#
# Test 1: total_budget([100, 200, 150])
#    Input: [100, 200, 150]   Expected output: 450
# Test 2: highest_budget([100, 200, 150])
#    Input: [100, 200, 150]   Expected output: 200
# Test 3: percentage(1, 4)
#    Input: part 1, whole 4   Expected output: 25.0

assert total_budget([100, 200, 150]) == 450
assert highest_budget([100, 200, 150]) == 200
assert percentage(1, 4) == 25.0
print("All three small function tests passed.")

# Now the combined function, on the list from exercise 4.0
campaign_budgets = [100, 200, 150, 300, 250, 400, 350, 500]

# By hand: total = 2250, biggest = 500, so 500 / 2250 * 100 = 22.2 (rounded)
print("Biggest campaign share of the total budget:",
      biggest_campaign_share(campaign_budgets), "%")
