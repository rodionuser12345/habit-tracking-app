import sqlite3

from habit_tracker import create_habit, delete_habit, delete_completion, complete_task, get_habits, get_completions
from datetime import datetime, timedelta


def create_tables(conn):
    """
    Creates the necessary tables in the SQLite database.

    Args:
        conn: SQLite database connection object.
    """
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS habits (
                    id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL,
                    task TEXT NOT NULL,
                    periodicity TEXT NOT NULL,
                    creation_date TEXT NOT NULL)''')

    c.execute('''CREATE TABLE IF NOT EXISTS completions (
                        id INTEGER PRIMARY KEY, 
                        habit_id INTEGER, 
                        completion_date TEXT,
                        FOREIGN KEY (habit_id) REFERENCES habits (id))''')
    conn.commit()


def create_sample_habits():
    """
    Creates a list of sample habits.

    Returns:
        list: List of sample Habit objects.
    """
    habit1 = create_habit("Exercise", "Go for a run", "daily", "2023-04-03")
    habit2 = create_habit("Meditation", "Meditate for 10 minutes", "daily", "2023-01-01")
    habit3 = create_habit("Reading", "Read 20 pages", "daily", "2023-01-01")
    habit4 = create_habit("Cooking", "Cook a healthy meal", "weekly", "2023-01-01")
    habit5 = create_habit("Learning", "Learn something new", "weekly", "2023-01-01")

    habits = [habit1, habit2, habit3, habit4, habit5]

    return habits


def clear_db():
    """
    Clears all data from the habits and completions tables in the database.
    """
    habits = get_habits()
    completions = get_completions()
    for habit in habits:
        delete_habit(habit.id)
    for completion in completions:
        delete_completion(completion)


def add_sample_data(habits):
    """
    Adds sample completion data for the given list of habits.

    Args:
        habits (list): List of Habit objects for which to add sample completion data.
    """
    start_date = datetime.strptime("2023-01-01", "%Y-%m-%d")

    for habit in habits:
        for i in range(28):
            if habit.periodicity == "daily":
                completion_date = start_date + timedelta(days=i)
                complete_task(habit.id, completion_date.strftime("%Y-%m-%d"))
            elif habit.periodicity == "weekly" and i % 7 == 0:
                completion_date = start_date + timedelta(weeks=i // 7)
                complete_task(habit.id, completion_date.strftime("%Y-%m-%d"))


def initialize_db():
    """
    Initializes the database by creating tables, clearing existing data, and adding sample data.
    """
    conn = sqlite3.connect('habits.db')
    create_tables(conn)
    clear_db()
    habits = create_sample_habits()
    add_sample_data(habits)
