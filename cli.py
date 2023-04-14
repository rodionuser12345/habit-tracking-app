import sys
from habit_tracker import create_habit, delete_habit, complete_task, get_habits, get_habit_by_id, \
    get_completions_for_habit
from analytics import get_habits_by_periodicity, longest_streak
from initialize_db import initialize_db
from datetime import datetime
from tabulate import tabulate


def print_habits(habits):
    """
    Prints a list of habits in a tabulated format.

    Args:
        habits (list): List of Habit objects to display.
    """
    habits_table = [["ID", "Name", "Task", "Periodicity", "Creation Date", "Streaks"]]
    for habit in habits:
        habits_table.append([
            habit.id,
            habit.name,
            habit.task,
            habit.periodicity,
            habit.creation_date,
            habit.streaks
        ])
    print(tabulate(habits_table, headers="firstrow", tablefmt="grid"))


def print_menu():
    """
    Prints the main menu options to the console.
    """
    print("\nMENU")
    print("1. List habits")
    print("2. Create habit")
    print("3. Delete habit")
    print("4. Complete task")
    print("5. Get habits with same periodicity")
    print("6. Get longest streak for a habit")
    print("7. Get longest streak")
    print("8. Get completions for a habit")
    print("9. Exit")


def main():
    """
    The main function to run the CLI-based habit tracker application.
    """
    initialize_db()

    while True:
        print_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            habits = get_habits()
            print_habits(habits)
        elif choice == "2":
            name = input("Enter habit name: ")
            task = input("Enter task: ")
            periodicity = input("Enter periodicity (daily or weekly): ")
            creation_date = datetime.now().strftime("%Y-%m-%d")
            habit = create_habit(name, task, periodicity, creation_date)
            print(f"Created habit: {habit}")
        elif choice == "3":
            habit_id = int(input("Enter habit ID: "))
            delete_habit(habit_id)
            print(f"Habit with ID {habit_id} deleted.")
        elif choice == "4":
            habit_id = int(input("Enter habit ID: "))
            completion_date = input("Enter completion date (YYYY-MM-DD): ")
            complete_task(habit_id, completion_date)
            print(f"Task completed for habit with ID {habit_id} on {completion_date}")
        elif choice == "5":
            periodicity = input("Enter periodicity (daily or weekly): ")
            habits = get_habits_by_periodicity(get_habits(), periodicity)
            print_habits(habits)
        elif choice == "6":
            habit_id = int(input("Enter habit ID: "))
            habit = get_habit_by_id(habit_id)
            if habit:
                streak = longest_streak(habit)
                print(f"Longest streak for habit '{habit.name}' is {streak}")
            else:
                print("Habit not found.")
        elif choice == "7":
            habits = get_habits()
            longest_streak_habit = max(habits, key=longest_streak)
            streak = longest_streak(longest_streak_habit)
            print(f"Longest streak is {streak} for habit '{longest_streak_habit.name}'")
        elif choice == "8":
            habit_id = int(input("Enter habit ID: "))
            completions = get_completions_for_habit(habit_id)
            if completions:
                print("Completions for habit with ID", habit_id)
                for completion in completions:
                    print(f"ID: {completion['id']} - Date: {completion['completion_date']}")
            else:
                print("No completions found for habit with ID", habit_id)
        elif choice == "9":
            print("Goodbye!")
            sys.exit(0)
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
