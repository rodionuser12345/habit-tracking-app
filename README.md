
# Habit Tracking App

## Overview

This is a habit tracking application that allows users to track their habits. The application provides features to create, update, delete, and mark tasks as complete for habits. It also provides analytics features such as finding the longest streak for habits. The application consists of several modules and includes CLI-based interaction for users.

## Modules

### Habit

This module defines the `Habit` class which serves as the data model for habits.

- `__init__`: Initializes a Habit object with attributes.
- `complete_task`: Marks a task as complete for a specific date.
- `validate_completion_dates`: Validates the list of completion dates.

### Database Operations

This module provides functions for database operations related to habits.

- `create_habit`: Creates a new habit in the database.
- `update_habit`: Updates an existing habit in the database.
- `delete_habit`: Deletes a habit from the database.
- `get_habits`: Fetches all habits from the database.

### Analytics

This module provides analytical functions.

- `get_habits_by_periodicity`: Filters habits by their periodicity.
- `longest_streak`: Calculates the longest streak for a given habit.
- `longest_streak_all_habits`: Calculates the longest streak across all habits.

### Database Initialization

This module handles the database initialization and sample data creation.

- `create_tables`: Creates the necessary tables in the database.
- `create_sample_habits`: Creates sample habits.
- `clear_db`: Clears the database.
- `add_sample_data`: Adds sample data to the database.

### CLI

This module provides a CLI-based interface for the application.

- `print_habits`: Prints a list of habits.
- `print_menu`: Prints the main menu.
- `main`: The main function to run the application.

### Unit Tests

This module provides unit tests for the application.

- `setUp`: Sets up initial data for each test case.
- `tearDown`: Cleans up after each test case.
- Various test methods for testing different functionalities.

## Installation

1. Clone the repository: `git clone https://github.com/rodionuser12345/habit-tracking-app.git`
2. Navigate to the project directory.
3. Run `python initialize_db.py` to set up the database.
4. Run `python habit_tracker.py` to start the application.

## Testing

Run `python test_habit_tracker.py` to run the unit tests.

## Contributing

Feel free to contribute to this project by submitting issues or pull requests.

