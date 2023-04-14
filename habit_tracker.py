import sqlite3
from datetime import datetime

from habit import Habit


def create_connection():
    """
    Creates and returns a new SQLite database connection.

    Returns:
        conn: SQLite database connection object.
    """
    conn = sqlite3.connect('habits.db')
    return conn


def get_habit_by_id(habit_id):
    """
    Retrieves a Habit object by its ID from the database.

    Args:
        habit_id (int): The ID of the habit to retrieve.

    Returns:
        Habit: The Habit object corresponding to the given ID, or None if not found.
    """
    conn = create_connection()
    c = conn.cursor()
    c.execute("SELECT * FROM habits WHERE id = ?", (habit_id,))
    habit_row = c.fetchone()

    if habit_row:
        id, name, task, periodicity, creation_date = habit_row
        c.execute("SELECT completion_date FROM completions WHERE habit_id = ?", (id,))
        completion_dates = [row[0] for row in c.fetchall()]
        conn.close()
        return Habit(id, name, task, periodicity, creation_date, completion_dates)
    else:
        conn.close()
        return None


def create_habit(name, task, periodicity, creation_date):
    """
    Creates a new habit.

    Args:
        name (str): The name of the habit.
        task (str): The task associated with the habit.
        periodicity (str): The frequency of the habit.

    Returns:
        bool: True if the habit was successfully created, False otherwise.
    """
    conn = create_connection()
    habit = Habit(None, name, task, periodicity, creation_date)
    c = conn.cursor()
    c.execute("INSERT INTO habits (name, task, periodicity, creation_date) VALUES (?, ?, ?, ?)",
              (habit.name, habit.task, habit.periodicity, habit.creation_date))
    conn.commit()
    habit.id = c.lastrowid
    conn.close()
    return habit


def update_habit(habit_id, name, task, periodicity):
    """
    Updates an existing habit in the database.

    Args:
        habit_id (int): The ID of the habit to update.
        name (str): The new name for the habit.
        task (str): The new task for the habit.
        periodicity (str): The new periodicity for the habit.
    """
    conn = create_connection()
    c = conn.cursor()
    c.execute("UPDATE habits SET name = ?, task = ?, periodicity = ? WHERE id = ?",
              (name, task, periodicity, habit_id))
    conn.commit()
    conn.close()


def delete_habit(habit_id):
    """
    Deletes a habit based on its ID.

    Args:
        habit_id (int): The ID of the habit to be deleted.

    Returns:
        bool: True if the habit was successfully deleted, False otherwise.
    """
    conn = create_connection()
    c = conn.cursor()
    c.execute("DELETE FROM habits WHERE id = ?", (habit_id,))
    conn.commit()
    conn.close()


def delete_completion(completion_id):
    """
    Deletes a completion record from the database based on its ID.

    Args:
        completion_id (int): The ID of the completion record to delete.
    """
    conn = create_connection()
    c = conn.cursor()
    c.execute("DELETE FROM completions WHERE id = ?", (completion_id,))
    conn.commit()
    conn.close()


def complete_task(habit_id, completion_date):
    """
    Marks the task associated with a habit as complete in the database.

    Args:
        habit_id (int): The ID of the habit whose task was completed.
        completion_date (str): The date on which the task was completed.
    """
    habit = get_habit_by_id(habit_id)
    if habit:
        # habit.complete_task(completion_date)
        # habit.completion_dates.sort()
        conn = create_connection()
        c = conn.cursor()
        c.execute("INSERT INTO completions (habit_id, completion_date) VALUES (?, ?)", (habit_id, completion_date))
        conn.commit()
        conn.close()


def get_habits():
    """
    Retrieves all Habit objects from the database.

    Returns:
        list: List of all Habit objects.
    """
    conn = create_connection()
    c = conn.cursor()
    c.execute("SELECT * FROM habits")
    habit_rows = c.fetchall()

    habits = []
    for id, name, task, periodicity, creation_date in habit_rows:
        c.execute("SELECT completion_date FROM completions WHERE habit_id = ?", (id,))
        completion_dates = [row[0] for row in c.fetchall()]
        habit = Habit(id, name, task, periodicity, creation_date, completion_dates)
        habits.append(habit)

    conn.close()
    return habits


def get_completions():
    """
    Retrieves all completion records from the database.

    Returns:
        list: List of all completion records.
    """
    conn = create_connection()
    c = conn.cursor()
    c.execute("SELECT * FROM completions")
    completion_rows = c.fetchall()
    conn.close()

    completions = []
    for id, habit_id, completion_date in completion_rows:
        completions.append(id)

    return completions


def get_completions_for_habit(habit_id):
    """
    Retrieves all completion records for a specific habit from the database.

    Args:
        habit_id (int): The ID of the habit for which to retrieve completion records.

    Returns:
        list: List of all completion records for the given habit.
    """
    conn = create_connection()
    c = conn.cursor()
    c.execute("SELECT id, completion_date FROM completions WHERE habit_id = ?", (habit_id,))
    completion_rows = c.fetchall()
    conn.close()

    completions = []
    for id, completion_date in completion_rows:
        completions.append({"id": id, "completion_date": completion_date})

    return completions
