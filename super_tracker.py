import tkinter as tk
from tkinter import ttk, messagebox
import json
from datetime import datetime, timedelta
import os
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# --- 1. Configuration: Day-wise task schedule ---
DATA_FILE = "super_history.json"

# Define which tasks will be done on which day
SCHEDULE_CONFIG = {
    "Daily": [  # These tasks will appear every day
        "Wake up & Fresh",
        "Prayer / Meditation",
        "Exercise / Walk"
    ],
    "Sunday": [
        "Heavy Coding (Python)",
        "Web dev Project Building",
        "Client outreach",
        "Client Task",
        "Robotics Parctice",
        "CSE Parctice",
        "AI/ML Projects",
        "Development Projects(SaaS)"   
    ],
    "Monday": [
        "UI/UX Case Study",
        "UI/UX Design Practice",
        "Client Hunting",
        "Client Task",
        "Robotics Class",
        "CSE CLASS",
        "AI/ML CLASS",
        "UI/UX Projects(SaaS)"
    ],
    "Tuesday": [
        "Heavy Coding (Python)",
        "Web dev Project Building",
        "Client outreach",
        "Client Task",
        "Robotics Parctice",
        "CSE Parctice",
        "AI/ML Projects",
        "Development Projects(SaaS)"  
    ],
    "Wednesday": [
        "UI/UX Case Study",
        "UI/UX Design Practice",
        "Client Hunting",
        "Client Task",
        "Robotics Class",
        "CSE CLASS",
        "AI/ML CLASS",
        "UI/UX Projects(SaaS)"
    ],
    "Thursday": [
       "Heavy Coding (Python)",
        "Web dev Project Building",
        "Client outreach",
        "Client Task",
        "Robotics Parctice",
        "CSE Parctice",
        "AI/ML Projects",
        "Development Projects(SaaS)"  
    ],
    "Friday": [
        "TEST",
        "ASSETS SELL",
        "NEW/NEXT PLAN",
        "Review CLIENTS",
        "Robotics Projects",
        "CSE Projects",
        "AI/ML Projects",
        "Lanching Day & Next Projects Plan"
    ],
    "Saturday": [
        "UI/UX Case Study",
        "UI/UX Design Practice",
        "Client Hunting",
        "Client Task",
        "Robotics Class",
        "CSE CLASS",
        "AI/ML CLASS",
        "UI/UX Projects(SaaS)"
    ]
}

# Create a master list of all unique tasks (for left-side rows)
def get_all_unique_tasks():
    all_tasks = set(SCHEDULE_CONFIG["Daily"])
    for day in ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]:
        all_tasks.update(SCHEDULE_CONFIG.get(day, []))
    # Sort list (Daily tasks first)
    sorted_list = SCHEDULE_CONFIG["Daily"] + [
        t for t in list(all_tasks) if t not in SCHEDULE_CONFIG["Daily"]
    ]
    return sorted_list

ALL_TASKS = get_all_unique_tasks()

def load_data():
    if not os.path.exists(DATA_FILE):
        return {}
    with open(DATA_FILE, "r") as f:
        return json.load(f)

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f)

# --- 2. Logic ---
def toggle_status(date, task, btn_widget):
    data = load_data()
    if date not in data:
        data[date] = {}

    current_status = data[date].get(task, False)
    new_status = not current_status

    data[date][task] = new_status
    save_data(data)
    update_button_active(btn_widget, new_status)
    app.needs_refresh = True

# Active button style
def update_button_active(btn, status):
    if status:
        btn.config(bg="#2cbe4e", text="✔", fg="white", state="normal")
    else:
        btn.config(bg="#f0f0f0", text="Active", fg="black", state="normal")

# Disabled button style (task not scheduled for that day)
def set_button_disabled(btn):
    btn.config(bg="#e0e0e0", text="✕", fg="#999", state="disabled", relief="flat")

# --- 3. Tab 1: Future Planner ---
def build_planner_tab(parent):
    for widget in parent.winfo_children():
        widget.destroy()

    data = load_data()
    today = datetime.now()
    days_to_show = 7

    # Header
    header_frame = tk.Frame(parent, bg="white")
    header_frame.pack(pady=10)
    tk.Label(
        header_frame,
        text="Smart Weekly Planner",
        font=("Helvetica", 14, "bold"),
        bg="white"
    ).pack()
    tk.Label(
        header_frame,
        text="Black box = task not scheduled | White box = task available",
        font=("Arial", 9),
        fg="gray",
        bg="white"
    ).pack()

    # Grid frame
    grid_frame = tk.Frame(parent, bg="white")
    grid_frame.pack(padx=10, pady=5)

    # Column headers (dates)
    tk.Label(
        grid_frame,
        text="TASKS (Master List)",
        font=("Arial", 9, "bold"),
        bg="#333",
        fg="white",
        width=20,
        anchor="w"
    ).grid(row=0, column=0, padx=2, pady=2)

    for i in range(days_to_show):
        d = today + timedelta(days=i)
        day_short = d.strftime("%a")
        date_str = d.strftime("%d")

        full_text = f"{day_short}\n{date_str}"

        bg_color = "#e6f7ff"
        if i == 0:
            bg_color = "#fff3cd"  # Today

        tk.Label(
            grid_frame,
            text=full_text,
            font=("Arial", 9, "bold"),
            bg=bg_color,
            width=6,
            height=2,
            relief="solid",
            borderwidth=1
        ).grid(row=0, column=i + 1, padx=1, pady=1)

    # Body (task buttons)
    for r, task in enumerate(ALL_TASKS):
        tk.Label(
            grid_frame,
            text=task,
            font=("Arial", 9),
            bg="white",
            width=20,
            anchor="w"
        ).grid(row=r + 1, column=0, padx=2, pady=2)

        for c in range(days_to_show):
            d = today + timedelta(days=c)
            date_key = d.strftime("%Y-%m-%d")
            day_name = d.strftime("%A")

            # Core logic
            is_daily = task in SCHEDULE_CONFIG["Daily"]
            is_today_special = task in SCHEDULE_CONFIG.get(day_name, [])

            btn = tk.Button(grid_frame, width=4, height=1)

            if is_daily or is_today_special:
                is_planned = data.get(date_key, {}).get(task, False)
                update_button_active(btn, is_planned)
                btn.config(
                    command=lambda d=date_key, t=task, b=btn: toggle_status(d, t, b)
                )
            else:
                set_button_disabled(btn)

            btn.grid(row=r + 1, column=c + 1, padx=2, pady=2)

# --- 4. Tab 2: Analytics ---
def build_analytics_tab(parent):
    for widget in parent.winfo_children():
        widget.destroy()

    data = load_data()
    today = datetime.now()

    tk.Label(
        parent,
        text="Completed Tasks (History)",
        font=("Helvetica", 14, "bold"),
        bg="white"
    ).pack(pady=10)

    chart_frame = tk.Frame(parent, bg="white")
    chart_frame.pack(pady=15, fill="both", expand=True)

    dates = []
    counts = []

    for i in range(6, -1, -1):
        d = today - timedelta(days=i)
        d_str = d.strftime("%Y-%m-%d")
        d_lbl = d.strftime("%a")

        count = 0
        if d_str in data:
            count = sum(1 for status in data[d_str].values() if status)

        dates.append(d_lbl)
        counts.append(count)

    fig, ax = plt.subplots(figsize=(5, 4), dpi=100)
    bars = ax.bar(dates, counts, color="#40c463")

    ax.set_title("Tasks Finished (Last 7 Days)", fontsize=10)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    for bar in bars:
        yval = bar.get_height()
        if yval > 0:
            ax.text(
                bar.get_x() + bar.get_width() / 2,
                yval,
                int(yval),
                ha="center",
                va="bottom",
                fontsize=8
            )

    canvas = FigureCanvasTkAgg(fig, master=chart_frame)
    canvas.draw()
    canvas.get_tk_widget().pack()

# --- 5. Main App ---
class SuperPlannerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Dynamic Day-wise Planner 🚀")
        self.root.geometry("700x650")
        self.root.configure(bg="white")
        self.needs_refresh = False

        style = ttk.Style()
        style.theme_use("default")
        style.configure("TNotebook.Tab", padding=[15, 8], font=("Helvetica", 10, "bold"))

        self.notebook = ttk.Notebook(root)
        self.notebook.pack(pady=10, expand=True, fill="both")

        self.tab1 = tk.Frame(self.notebook, bg="white")
        self.tab2 = tk.Frame(self.notebook, bg="white")

        self.notebook.add(self.tab1, text="📅 Planner")
        self.notebook.add(self.tab2, text="📊 History")

        build_planner_tab(self.tab1)
        build_analytics_tab(self.tab2)

        self.notebook.bind("<<NotebookTabChanged>>", self.on_tab_change)

    def on_tab_change(self, event):
        selected_tab = self.notebook.index(self.notebook.select())
        if selected_tab == 1 and self.needs_refresh:
            build_analytics_tab(self.tab2)
            self.needs_refresh = False

if __name__ == "__main__":
    root = tk.Tk()
    app = SuperPlannerApp(root)
    root.mainloop()
