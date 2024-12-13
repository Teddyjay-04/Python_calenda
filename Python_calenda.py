import tkinter as tk
from tkinter import messagebox
import calendar
import holidays
import datetime

class CalendarApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calendar Viewer")
        self.ro_holidays = holidays.RO()

        # Create control frame for year and month
        control_frame = tk.Frame(root)
        control_frame.pack(pady=10)

        tk.Label(control_frame, text="Year:").grid(row=0, column=0, padx=5)
        self.year_entry = tk.Entry(control_frame, width=6)
        self.year_entry.insert(0, str(datetime.datetime.now().year))
        self.year_entry.grid(row=0, column=1, padx=5)

        tk.Label(control_frame, text="Month:").grid(row=0, column=2, padx=5)
        self.month_entry = tk.Entry(control_frame, width=4)
        self.month_entry.insert(0, str(datetime.datetime.now().month))
        self.month_entry.grid(row=0, column=3, padx=5)

        tk.Button(control_frame, text="Show", command=self.update_calendar).grid(row=0, column=4, padx=10)

        # Create calendar frame
        self.calendar_frame = tk.Frame(root)
        self.calendar_frame.pack(pady=10)

        # Create header for the calendar
        self.weekdays = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
        for idx, day in enumerate(self.weekdays):
            tk.Label(self.calendar_frame, text=day, font=("Arial", 10, "bold"), borderwidth=1, relief="solid", width=4, height=2, bg="#f0f0f0").grid(row=0, column=idx, padx=1, pady=1)

        # Display the current calendar on launch
        self.update_calendar()

    def update_calendar(self):
        # Clear the previous calendar
        for widget in self.calendar_frame.winfo_children():
            widget.destroy()

        # Recreate the header
        for idx, day in enumerate(self.weekdays):
            tk.Label(self.calendar_frame, text=day, font=("Arial", 10, "bold"), borderwidth=1, relief="solid", width=4, height=2, bg="#f0f0f0").grid(row=0, column=idx, padx=1, pady=1)

        try:
            year = int(self.year_entry.get())
            month = int(self.month_entry.get())
            if not (1 <= month <= 12):
                raise ValueError
        except ValueError:
            messagebox.showerror("Error", "Year and month must be valid integers!")
            return

        # Generate the month's calendar
        cal = calendar.Calendar(firstweekday=0)  # Monday as the first day of the week
        month_days = cal.monthdayscalendar(year, month)

        # Get holidays for the specified year
        self.ro_holidays = holidays.RO(years=year)

        for r, week in enumerate(month_days, start=1):
            for c, day in enumerate(week):
                if day == 0:
                    # Non-existent day in this month
                    tk.Label(self.calendar_frame, text="", borderwidth=1, relief="solid", width=4, height=2).grid(row=r, column=c, padx=1, pady=1)
                else:
                    date = datetime.date(year, month, day)
                    text = str(day)
                    bg_color = "white"
                    fg_color = "black"

                    # Check if it's a weekend
                    if date.weekday() >= 5:
                        bg_color = "#d1e7dd"  # Light green for weekend
                    # Check if it's a holiday
                    if date in self.ro_holidays:
                        bg_color = "#f8d7da"  # Light red for holiday
                        fg_color = "red"

                    tk.Label(self.calendar_frame, text=text, borderwidth=1, relief="solid", width=4, height=2, bg=bg_color, fg=fg_color).grid(row=r, column=c, padx=1, pady=1)

        # Update the window title
        self.root.title(f"Calendar - {calendar.month_name[month]} {year}")

if __name__ == "__main__":
    root = tk.Tk()
    app = CalendarApp(root)
    root.mainloop()
