# Python Calendar Application

This is a Python application built using the Tkinter library to display a monthly calendar. It highlights weekends and Romanian holidays using the `holidays` library.

## Features

- **Customizable Calendar View**: Users can view the calendar for any specified year and month.
- **Weekend Highlighting**: Weekends are marked with a light green background for easy identification.
- **Holiday Highlighting**: Romanian holidays are automatically detected and displayed with a red background and text.
- **Interactive Interface**: Simple graphical interface with entry fields for the year and month.

## Requirements

- Python 3.x
- Libraries:
  - `tkinter` (pre-installed with Python)
  - `calendar` (built-in module)
  - `holidays` (install using "pip install holidays")

### How It Works
1. The user inputs a year and month in the entry fields.
2. Clicking the "Show" button updates the calendar display for the specified month and year.
3. Weekends are highlighted with a green background, while Romanian public holidays are highlighted with a red background and text.
4. Non-existent dates (padding for weeks) are shown as blank cells.

### Code Structure
## CalendarApp Class:
1. Initializes the UI with controls for year and month selection.
2. Displays a calendar grid with weekdays, weekends, and holidays.
3. Handles input validation and updates the calendar dynamically.

## Libraries Used:
1. tkinter: For the graphical user interface.
2. calendar: To generate the monthly calendar layout.
3. holidays: To fetch Romanian public holidays.
