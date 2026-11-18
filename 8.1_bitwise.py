"""Exercise 8.1 — Bitwise operators (bonus, not graded)

WHAT THE PROGRAM MUST DO
    Represent a set of permissions as bits, combine two of them, test whether a third is
    present, then add it and remove one.

ANSWER THESE FIRST, in comments
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What are your permissions about? Not files: invent a set from your own field,
       such as who may view, edit and publish a campaign.

WHAT THE AI CANNOT KNOW
    Your permission set and what each one means in your context.

CHECK IT YOURSELF
    Display the value in binary at each step and read the bits yourself.

DELIVERABLE
    This file, with your comments and your code.
"""

# Your code below
# 1. What goes in?
# Three permissions: VIEW, EDIT and PUBLISH.

# 2. What happens to it?
# Bitwise operators combine, test, add and remove permissions.

# 3. What comes out?
# The permissions displayed in binary at each step.

# 4. What are your permissions about?
# My permissions are about managing a marketing campaign.
# VIEW means viewing a campaign.
# EDIT means editing a campaign.
# PUBLISH means publishing a campaign.

VIEW = 1
EDIT = 2
PUBLISH = 4

# Combine two permissions
permissions = VIEW | EDIT

print("Initial permissions:", permissions)
print("Binary:", bin(permissions))

# Test if PUBLISH permission is present
print("Can publish:", bool(permissions & PUBLISH))

# Add PUBLISH permission
permissions = permissions | PUBLISH

print("After adding PUBLISH:", permissions)
print("Binary:", bin(permissions))

# Remove EDIT permission
permissions = permissions & ~EDIT

print("After removing EDIT:", permissions)
print("Binary:", bin(permissions))
