# First and last name: JANA WEHBE
# Group: A
#
# PLANNING NOTES — review and rewrite these in your own words.
#
# 1. What goes in?
# A comma-separated CSV containing the scenario ID, situation,
# three choices, their budget and reputation changes, and feedback.
# Budget and reputation changes are signed whole numbers.
#
# 2. What happens each day?
# Show the day, budget and reputation.
# Display a scenario and its three choices.
# Ask for a valid choice.
# Apply the changes, display feedback and record the move.
# Stop immediately if either gauge reaches zero or below.
#
# 3. What comes out?
# The final gauges, title, best move and worst move.
# Save name, budget, reputation, title and date in results.csv.
#
# 4. What could go wrong?
# Invalid choice: ask again.
# Missing or invalid CSV: show a clear error.
# Gauge reaches zero: stop the game.
# Player cancels: exit without saving an incomplete game.
#
# BONUS: The algorithm.
# One random day doubles the reputation change.
# I chose this because it makes the game less predictable.


# Step 1: Import the modules and define the file locations.
import csv
import random
from datetime import date
from pathlib import Path

FOLDER = Path(__file__).resolve().parent
SCENARIO_FILE = FOLDER / "scenarios_A.csv"
RESULTS_FILE = FOLDER / "results.csv"

DAYS = 10


# Step 2: Load every scenario and store each option as a tuple.
def load_scenarios(filename):
    scenarios = []
    used_ids = set()

    expected_columns = [
        "ID", "Scenario",
        "OptionA", "OptionB", "OptionC",
        "BudgetA", "BudgetB", "BudgetC",
        "ReputationA", "ReputationB", "ReputationC",
        "FeedbackA", "FeedbackB", "FeedbackC",
    ]

    with open(filename, newline="", encoding="utf-8-sig") as file:
        reader = csv.DictReader(file)

        if reader.fieldnames != expected_columns:
            raise ValueError("The CSV does not have the Group A columns.")

        for line_number, row in enumerate(reader, start=2):
            # Check that the row has all its values and no extra columns.
            if None in row or any(
                value is None or not value.strip()
                for value in row.values()
            ):
                raise ValueError(
                    f"Missing or extra values on line {line_number}."
                )

            # Convert the ID and impacts from text to whole numbers.
            try:
                scenario_id = int(row["ID"])

                options = {}

                for letter in "ABC":
                    options[letter] = (
                        row["Option" + letter],
                        int(row["Budget" + letter]),
                        int(row["Reputation" + letter]),
                        row["Feedback" + letter],
                    )

            except ValueError:
                raise ValueError(
                    f"Invalid whole number on line {line_number}."
                ) from None

            # Avoid loading two scenarios with the same ID.
            if scenario_id in used_ids:
                raise ValueError(f"Duplicate scenario ID: {scenario_id}")

            used_ids.add(scenario_id)

            scenarios.append({
                "id": scenario_id,
                "situation": row["Scenario"],
                "options": options,
            })

    if len(scenarios) < DAYS:
        raise ValueError("The CSV must contain at least 10 scenarios.")

    return scenarios


# Step 3: Ask again until the player enters A, B or C.
def ask_choice():
    while True:
        choice = input("Your choice (A, B or C): ").strip().upper()

        if choice in ("A", "B", "C"):
            return choice

        print("Please type A, B or C.")


# Step 4: Apply the choice and return both gauges as a tuple.
def apply_choice(budget, reputation, option, multiplier):
    text, budget_change, reputation_change, feedback = option

    budget += budget_change
    reputation += reputation_change * multiplier

    # Reputation cannot go above 100.
    reputation = min(100, reputation)

    return budget, reputation


# Step 5: Determine the final title and score.
def get_title(budget, reputation):
    if budget <= 0 or reputation <= 0:
        return "Fired", None

    score = reputation + budget // 200

    if score < 95:
        title = "Eternal Intern"
    elif score < 120:
        title = "Growth Hacker"
    elif score < 140:
        title = "CMO Material"
    else:
        title = "Viral Legend"

    return title, score


# Step 6: Display the ending and the best and worst moves.
def show_results(name, budget, reputation, history):
    title, score = get_title(budget, reputation)

    print("\n" + "=" * 40)

    if title == "Fired":
        reasons = []

        if budget <= 0:
            reasons.append("your budget reached zero or below")

        if reputation <= 0:
            reasons.append("your reputation reached zero or below")

        print("You are fired because " + " and ".join(reasons) + ".")
    else:
        print("Quarter survived!")
        print(f"Final score: {score}")

    print(f"Budget left: {budget} EUR")
    print(f"Reputation: {reputation}/100")
    print(f"{name}, your title: {title}")

    # Compare actual reputation changes after the bonus and the cap.
    # If moves are tied, use the earliest day.
    best_move = max(history, key=lambda move: move[0])
    worst_move = min(history, key=lambda move: move[0])

    change, day, text = best_move
    print(f'Best move: day {day}, "{text}" ({change:+d})')

    change, day, text = worst_move
    print(f'Worst move: day {day}, "{text}" ({change:+d})')

    return title


# Step 7: Append one completed game to results.csv.
def save_results(name, budget, reputation, title):
    needs_header = (
        not RESULTS_FILE.exists()
        or RESULTS_FILE.stat().st_size == 0
    )

    with open(RESULTS_FILE, "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        if needs_header:
            writer.writerow([
                "name", "budget", "reputation", "title", "date"
            ])

        writer.writerow([
            name,
            budget,
            reputation,
            title,
            date.today().isoformat(),
        ])


# Step 8: Prepare the player, scenarios and starting gauges.
def play_game():
    print("SURVIVE THE QUARTER")
    print("You are the marketing manager of Croissant Rocket!")

    name = input("Your name: ").strip()

    while not name:
        name = input("Please enter your name: ").strip()

    scenarios = load_scenarios(SCENARIO_FILE)
    random.shuffle(scenarios)

    budget = 10000
    reputation = 50
    history = []

    algorithm_day = random.randint(1, DAYS)

    print("\nSurvive 10 days without either gauge reaching zero.")
    print("On one random day, reputation changes are doubled!")


    # Step 9: Play ten different scenarios unless the player is fired.
    for day, scenario in enumerate(scenarios[:DAYS], start=1):
        print(f"\n--- Day {day} ---")
        print(
            f"[Budget: {budget} EUR | "
            f"Reputation: {reputation}/100]"
        )

        print(scenario["situation"])

        for letter in "ABC":
            option = scenario["options"][letter]
            print(f"  {letter}: {option[0]}")

        # Activate the required bonus on the selected day.
        multiplier = 1

        if day == algorithm_day:
            multiplier = 2
            print("THE ALGORITHM: reputation changes are doubled today!")

        choice = ask_choice()
        option = scenario["options"][choice]

        previous_reputation = reputation

        # Unpack the tuple returned by apply_choice.
        budget, reputation = apply_choice(
            budget, reputation, option, multiplier
        )

        actual_change = reputation - previous_reputation

        print(option[3])
        print(
            f"Budget {option[1]:+d} EUR, "
            f"Reputation {actual_change:+d}"
        )

        # Store one tuple per day, starting with reputation change.
        history.append((actual_change, day, option[0]))

        # Check both gauges immediately after each choice.
        if budget <= 0 or reputation <= 0:
            break


    # Step 10: Show the final result and save the completed game.
    title = show_results(name, budget, reputation, history)

    try:
        save_results(name, budget, reputation, title)
        print("Saved in results.csv")
    except OSError as error:
        print(f"The game finished, but saving failed: {error}")


# Step 11: Handle missing files, invalid data and cancellation.
def main():
    try:
        play_game()
    except (EOFError, KeyboardInterrupt):
        print("\nGame cancelled. No incomplete result was saved.")
    except (OSError, ValueError, csv.Error) as error:
        print(f"Cannot start the game: {error}")


# Step 12: Start the game when this file is run directly.
if __name__ == "__main__":
    main()