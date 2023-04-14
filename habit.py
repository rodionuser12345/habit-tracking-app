from datetime import timedelta, datetime


class Habit:
    """
    Represents a habit to be tracked.

    Attributes:
        id (int): Unique identifier for the habit.
        name (str): Name of the habit.
        task (str): Task associated with the habit.
        periodicity (str): Frequency with which the task should be completed.
        creation_date (str): Date the habit was created.
        completion_dates (list): List of dates on which the habit task was completed.
    """

    def __init__(self, id, name="", task="", periodicity="", creation_date="", completion_dates=None):
        """
        Initializes a Habit object with the provided attributes.

        Args:
            id (int): Unique identifier for the habit.
            name (str, optional): Name of the habit. Defaults to an empty string.
            task (str, optional): Task associated with the habit. Defaults to an empty string.
            periodicity (str, optional): Frequency with which the task should be completed. Defaults to an empty string.
            creation_date (str, optional): Date the habit was created. Defaults to an empty string.
            completion_dates (list, optional): List of dates on which the habit task was completed. Defaults to None.
        """
        if completion_dates is None:
            completion_dates = []
        self.id = id
        self.name = name
        self.task = task
        self.periodicity = periodicity
        self.creation_date = creation_date
        self.completion_dates = self.validate_completion_dates(completion_dates)

    def complete_task(self, completion_date):
        """
        Marks the task associated with the habit as complete for a given date.

        Args:
            completion_date (str): The date on which the task was completed.

        Returns:
            bool: True if the task was successfully marked as complete, False otherwise.
        """
        self.completion_dates.append(completion_date)

    @property
    def streaks(self):
        """
        Calculates the current streaks for the habit based on the completion dates.

        Returns:
            int: The current streak count.
        """
        if not self.completion_dates:
            return 0

        streaks_count = 0
        period = timedelta(days=1 if self.periodicity == "daily" else 7)

        sorted_dates = sorted(datetime.strptime(date_str, "%Y-%m-%d") for date_str in self.completion_dates)
        streaks = []
        current_streak = [sorted_dates[0]]

        for i in range(1, len(sorted_dates)):
            if sorted_dates[i] - sorted_dates[i - 1] == period:
                current_streak.append(sorted_dates[i])
            else:
                if len(current_streak) >= 2:
                    streaks.append(current_streak)
                    streaks_count += 1
                current_streak = [sorted_dates[i]]

        if len(current_streak) >= 2:
            streaks.append(current_streak)
            streaks_count += 1

        return streaks_count

    def validate_completion_dates(self, completion_dates):
        """
        Validates the list of completion dates.

        Args:
            completion_dates (list): List of dates to validate.

        Returns:
            list: List of validated completion dates.
        """
        if completion_dates is None:
            return []

        valid_dates = []
        for date_str in completion_dates:
            try:
                date = datetime.strptime(date_str, "%Y-%m-%d").date()
                valid_dates.append(date_str)
            except ValueError:
                print(f"Invalid date format found: {date_str}, skipping this date.")
        return valid_dates

    def __str__(self):
        """
        Returns the string representation of the Habit object.

        Returns:
            str: The string representation of the Habit object.
        """
        return f"{self.id} - {self.name} - {self.task} - {self.periodicity} - {self.creation_date}"
