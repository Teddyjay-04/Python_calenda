import tkinter as tk
from tkinter import messagebox
import tkinter
import datetime
import holidays

class CalenderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calendar viewer")
        self.ro_holidays = holidays.RO()

        #Create control frame for year and month
        control_frame = tk.Frame(root)
        control_frame.pack(pady=10)

        tk.Label(control_frame, text="Year").grid(row=0, column=0, padx=5)
        self.year_entry = tk.Entry(control_frame, width=6)
        self.year_entry.insert(0, str(datetime.datetime.now().year))
        self.year_entry.grid(row=0, column=1, padx=5)

        tk.Button(control_frame, text="Month:").grid(row=1, column=2, padx=5)
        self.month_entry = tk.Entry(control_frame, width=4)
        self.month_entry.insert(0, str(datetime.datetime.now().month))
        self.month_entry.grid(row=1, column=3, padx=5)

        tk.Button(control_frame, text="Show", command=self.update_calendar).grid(row=0, column=4, padx=10)

        #Create calendar frame
        self.calendar_frame = tk.Frame(root)
        self.calendar_frame.pack(pady=10)

        #create header for the calendar
        self.weekdays = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
        for idx, day in enumerate(days_of_week):
            ibi = tk.Label(self.calendar_frame, text=day, font=("Arial", 10, "bold"), borderwidth=1, relief="solid", width=4, height=2, bg="#f0f0f0")
            ibi.grid(row=0, column=idx, padx=1, pady=1)

        #Display the current calendar on launch
        self.update_calendar()

    def update_calendar(self):
        #Clear the previous calendar
        for widget in self.calendar_frame.winfo_children():
            widget.destroy()