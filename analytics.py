from datetime import datetime, timedelta


def get_habits_by_periodicity(habits, periodicity):
    """
    Filters a list of habits by their periodicity.

    Args:
        habits (list): List of Habit objects to filter.
        periodicity (str): The periodicity to filter by ("daily" or "weekly").

    Returns:
        list: List of Habit objects with the specified periodicity.
    """
    return list(filter(lambda habit: habit.periodicity == periodicity, habits))


def longest_streak(habit):
    """
    Calculates the longest streak of task completions for a given habit.

    Args:
        habit (Habit): The Habit object for which to calculate the longest streak.

    Returns:
        int: The length of the longest streak of task completions.
    """
    if not habit.completion_dates:
        return 0

    completion_dates = sorted([datetime.strptime(date, "%Y-%m-%d") for date in habit.completion_dates])
    streak = 1
    streak_longest = 1
    for i in range(1, len(completion_dates)):
        delta = completion_dates[i] - completion_dates[i - 1]
        if habit.periodicity == "daily" and delta <= timedelta(days=1):
            streak += 1
        elif habit.periodicity == "weekly" and delta <= timedelta(weeks=1):
            streak += 1
        else:
            streak = 1
        streak_longest = max(streak_longest, streak)

    return streak_longest


def longest_streak_all_habits(habits):
    """
    Calculates the longest streak of task completions across all given habits.

    Args:
        habits (list): List of Habit objects for which to calculate the longest streak.

    Returns:
        int: The length of the longest streak of task completions across all habits.
    """
    return max(map(lambda habit: longest_streak(habit), habits))
