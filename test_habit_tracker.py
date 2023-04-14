import unittest
from habit_tracker import create_habit, update_habit, delete_habit, complete_task, get_habits, get_habit_by_id
from analytics import longest_streak, get_habits_by_periodicity
from datetime import datetime, timedelta


class TestHabitTracker(unittest.TestCase):
    """
    Unit test class for the Habit Tracker application.
    """

    def setUp(self):
        """
        Set up initial data before each test case.
        """
        self.habit1 = create_habit("Test Exercise", "Run for 30 minutes", "daily", "2023-01-01")
        self.habit2 = create_habit("Test Meditation", "Meditate for 10 minutes", "weekly", "2023-01-01")

    def tearDown(self):
        """
        Clean up data after each test case.
        """
        delete_habit(self.habit1.id)
        delete_habit(self.habit2.id)

    def test_create_habit(self):
        """
        Test the habit creation functionality.
        """
        habit = create_habit("Test Reading", "Read 20 pages", "daily", "2023-01-01")
        self.assertIsNotNone(habit.id)
        delete_habit(habit.id)

    def test_update_habit(self):
        """
        Test the habit update functionality.
        """
        update_habit(self.habit1.id, "Test Exercise Updated", "Run for 45 minutes", "daily")
        updated_habit = get_habits()[0]
        self.assertEqual(updated_habit.name, "Test Exercise Updated")
        self.assertEqual(updated_habit.task, "Run for 45 minutes")

    def test_delete_habit(self):
        """
        Test the habit deletion functionality.
        """
        habit_id = self.habit1.id
        delete_habit(habit_id)
        habits = get_habits()
        habit_ids = [habit.id for habit in habits]
        self.assertNotIn(habit_id, habit_ids)

    def test_complete_task(self):
        """
        Test the task completion functionality.
        """
        complete_task(self.habit1.id, "2023-01-02")
        completed_habit = get_habit_by_id(self.habit1.id)
        self.assertIn("2023-01-02", completed_habit.completion_dates)

    def test_longest_streak(self):
        """
        Test the longest streak calculation functionality.
        """
        start_date = datetime.strptime("2023-01-01", "%Y-%m-%d")
        for i in range(5):
            completion_date = start_date + timedelta(days=i)
            complete_task(self.habit1.id, completion_date.strftime("%Y-%m-%d"))

        streak = longest_streak(get_habit_by_id(self.habit1.id))
        self.assertEqual(streak, 5)

    def test_get_habits_by_periodicity(self):
        """
        Test the functionality of getting habits by their periodicity.
        """
        daily_habits = get_habits_by_periodicity(get_habits(), "daily")
        self.assertEqual(len(daily_habits), 1)
        self.assertEqual(daily_habits[0].name, "Test Exercise")

        weekly_habits = get_habits_by_periodicity(get_habits(), "weekly")
        self.assertEqual(len(weekly_habits), 1)
        self.assertEqual(weekly_habits[0].name, "Test Meditation")


if __name__ == "__main__":
    unittest.main()
