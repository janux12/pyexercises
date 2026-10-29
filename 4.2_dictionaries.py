"""Exercise 4.2 — Working with a dictionary

WHAT THE PROGRAM MUST DO
    Describe one real object from your field using a dictionary of at least five fields,
    then read it, change it, remove one field, and display every field with its value.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What object did you describe, which five fields did you choose, and why those?
       A field you would never actually use does not count.

WHAT THE AI CANNOT KNOW
    Your object and your fields. A campaign, a customer, a product, a store, a supplier.
    Choose something you would genuinely have to describe in your job.

CHECK IT YOURSELF
    Ask your program for a field that does not exist. Note what happens in a comment,
    then make it survive that Case.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: Information about a marketing campaign.
# 2. Process:The program reads, changes, and removes information from a dictionary.
# 3. Out:The campaign information with each field and its value.
# 4. My object, my five fields, and why those:
# # Name, budget, platform, target_audience, and duration.
# These fields are useful for describing a marketing campaign.


# Your code below

campaign = {
    "name": "Summer Campaign",
    "budget": 1000,
    "platform": "Instagram",
    "target_audience": "Young adults",
    "duration": 30
}

print("The marketing campaign")
print(campaign)

print("The campaign name")
print(campaign["name"])

print("The campaign budget after changing it")
campaign["budget"] = 1500
print(campaign["budget"])

print("Checking a field that does not exist")
print(campaign.get("location", "Field not found"))

print("Removing the duration")
campaign.pop("duration")

print("All the fields and their values")
for key, value in campaign.items():
    print(key, value)

# Check: The campaign has five fields at the beginning.
# Check: The budget changed from 1000 to 1500.
# Check: The missing location field displayed "Field not found".
# Check: The duration field was removed.
# Check: All remaining fields and their values were displayed.
