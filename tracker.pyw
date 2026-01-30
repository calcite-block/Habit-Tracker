import tkinter as tk
from datetime import datetime
import calendar
import json
import os



# ----------------------------
# Configuration


ACTIVITIES = [
    "Example"
]


data = datetime.now().month
SAVE_FILE = "data/"+str(data)+".json"

GREEN = "#00cc44"
RED = "#ff3333"
EMPTY = "white"


cells = {}  # (activity, day) -> Label widget


# Event handlers


def left_click(event):
    label = event.widget
    current = label.cget("bg")

    if current == GREEN:
        label.config(bg=EMPTY)
    else:
        label.config(bg=GREEN)
    save_data()

def right_click(event):
    label = event.widget
    current = label.cget("bg")

    if current == RED:
        label.config(bg=EMPTY)
    else:
        label.config(bg=RED)
    save_data()



# Build UI


root = tk.Tk()
root.title("Habit Tracker")
y=len(ACTIVITIES)*18+100
root.geometry(f"980x{y}")

now = datetime.now()
year = now.year
month = now.month
days_in_month = calendar.monthrange(year, month)[1]

# Month title
month_label = tk.Label(
    root,
    text=f"{calendar.month_name[month]} {year}",
    font=("Arial", 14, "bold")
)
month_label.grid(row=0, column=0, columnspan=days_in_month + 1)

# Day headers
for day in range(1, days_in_month + 1):
    tk.Label(root, text=str(day), width=3).grid(row=1, column=day)

# Activity rows and cells
row_start = 2

for r, activity in enumerate(ACTIVITIES, start=row_start):
    tk.Label(
        root,
        text=activity,
        anchor="w",
        width=15
    ).grid(row=r, column=0)

    for day in range(1, days_in_month + 1):
        cell = tk.Label(
            root,
            bg=EMPTY,
            width=3,
            height=1,
            relief="solid",
            borderwidth=1
        )
        cell.grid(row=r, column=day)

        cell.bind("<Button-1>", left_click)
        cell.bind("<Button-3>", right_click)

        cells[(activity, day)] = cell

def save_data():
    data = {}
    for (activity, day), cell in cells.items():
        color = cell.cget("bg")
        if color != EMPTY:
            key = f"{activity}|{day}"
            data[key] = color

    with open(SAVE_FILE, "w") as f:
        json.dump(data, f)


def load_data():
    if not os.path.exists(SAVE_FILE):
        return

    with open(SAVE_FILE, "r") as f:
        data = json.load(f)

    for key, color in data.items():
        activity, day = key.split("|")
        day = int(day)

        if (activity, day) in cells:
            cells[(activity, day)].config(bg=color)

def on_close():
    save_data()
    root.destroy()



root.protocol("WM_DELETE_WINDOW", on_close)
load_data()
root.mainloop()
