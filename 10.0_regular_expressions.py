"""Exercise 10.0 — Checking the shape of text (bonus, not graded)

WHAT THE PROGRAM MUST DO
    Validate three pieces of information typed by the user, and only save them when all
    three are acceptable.

ANSWER THESE FIRST, in comments
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What are your three fields, and what makes a value acceptable for each? Write the
       rule in plain English before writing any pattern.

WHAT THE AI CANNOT KNOW
    Your three rules. "A valid email" is not a rule, it is a wish. Say what you accept
    and what you reject, and be ready to defend a borderline case.

WHAT TO WATCH
    An assistant will hand you a pattern that looks like line noise. Do not accept it
    until it has explained it to you piece by piece, and you have written that
    explanation in your own words above it.

CHECK IT YOURSELF
    For each field, prepare one value that must pass and two that must fail. Run all
    nine. Any surprise goes in a comment.

DELIVERABLE
    This file, with your comments and your code.
"""

# Your code below

import re

# 1. What goes in?
# The user enters an email, a phone number and a campaign code.

# 2. What happens to it?
# Python checks if the three values follow specific rules
# using regular expressions.

# 3. What comes out?
# The information is saved only if all three values are valid.

# 4. What are your three fields?

# Field 1: Email
# Accepts letters, numbers, dots, underscores and hyphens
# before @, followed by a domain and an extension of 2 to 4 letters.
# Pattern explanation:
# [A-Za-z0-9._-]+ means letters, numbers, dots, underscores or hyphens.
# @ means the email must contain @.
# [A-Za-z0-9-]+ means the domain name.
# \. means a dot.
# [A-Za-z]{2,4} means an extension of 2 to 4 letters.

# Field 2: Phone number
# Must contain exactly 10 digits and start with 0.
# Pattern explanation:
# 0 means the first digit must be zero.
# [1-9] means the second digit must be between 1 and 9.
# [0-9]{8} means exactly 8 more digits.

# Field 3: Campaign code
# Must start with CMP- followed by exactly 4 digits.
# Pattern explanation:
# CMP- means the code must start with CMP-.
# [0-9]{4} means exactly 4 digits.


while True:

    email = input("Enter your email: ")
    phone = input("Enter your phone number: ")
    campaign = input("Enter your campaign code: ")

    valid_email = re.fullmatch(
        r"[A-Za-z0-9._-]+@[A-Za-z0-9-]+\.[A-Za-z]{2,4}", email
    )

    valid_phone = re.fullmatch(r"0[1-9][0-9]{8}", phone)

    valid_campaign = re.fullmatch(r"CMP-[0-9]{4}", campaign)

    if valid_email and valid_phone and valid_campaign:

        print("All information is valid!")
        print("Information saved successfully.")

        saved_email = email
        saved_phone = phone
        saved_campaign = campaign

        break

    else:
        print("Some information is incorrect.")

        if not valid_email:
            print("Invalid email.")

        if not valid_phone:
            print("Invalid phone number.")

        if not valid_campaign:
            print("Invalid campaign code.")

        print("Please try again.")
