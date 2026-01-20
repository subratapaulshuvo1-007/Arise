import time
import schedule
from plyer import notification
from datetime import datetime  # New astrology-style date handling added

# --- 1. Message delivery system (Notification Function) ---
def send_alert(karma_name, time_period):
    # Calculate current date and day
    now = datetime.now()
    today_date = now.strftime("%d %B, %Y")  # e.g., 25 October, 2023
    today_day = now.strftime("%A")          # e.g., Wednesday
    
    print(f"🔔 Sending alert: {karma_name}")
    
    notification.notify(
        # Title will include date and day
        title = f"📅 {today_date} | {today_day}",
        
        # Message body
        message = (
            f"⏰ Time period: {time_period}\n"
            f"🙏 Task: {karma_name}\n"
            f"Do not delay in performing good work."
        ),
        timeout = 10
    )

# --- 2. Automatic time scheduler (Helper Function) ---
def set_karma(time_range, task_name):
    # Remove mechanical issues (dash fix)
    clean_range = time_range.replace("–", "-")
    
    # Extract the start time
    start_time = clean_range.split("-")[0].strip()
    
    # Fix format (8:00 -> 08:00)
    if len(start_time) == 4:
        start_time = "0" + start_time
        
    try:
        schedule.every().day.at(start_time).do(
            send_alert, task_name, clean_range
        )
        print(f"✅ Completed: '{task_name}' has been scheduled.")
    except Exception as e:
        print(f"❌ Error: Invalid time for '{task_name}'.")

# --- 3. Your daily routine (Daily Routine) ---
def load_schedule():
    
    # Morning
    set_karma("08:00-08:30", "Planning & Prioritizing")
    set_karma("08:30-09:30", "Skill Learning (Coding)")
    set_karma("09:30-10:00", "Problem Solving Practice")
    set_karma("10:00-11:00", "UI/UX Practice / Design")
    set_karma("11:00-12:00", "Portfolio / Personal Projects")
    
    # Midday
    set_karma("12:00-13:00", "Break / Relaxation")
    set_karma("13:00-15:00", "Client Hunting (Income Time)")
    set_karma("15:00-16:00", "Execution of Client Tasks")
    set_karma("16:00-17:00", "Robotics Basic Practice")
    
    # Evening & Night
    set_karma("17:00-18:00", "Exercise / Walk")
    set_karma("18:00-19:00", "Course / Deep Learning")
    set_karma("19:00-22:00", "KodeBari Community Contribution")
    set_karma("22:00-23:00", "Review Clients & Outreach")
    set_karma("23:00-00:00", "CSE Study (Academic Topics)")
    set_karma("00:00-00:30", "Reflection & Journaling")
    set_karma("00:30-01:00", "Free Time + Sleep Prep")

# --- 4. Main engine (Main Engine) ---
if __name__ == "__main__":
    
    # This message appears when the computer starts (with date and day)
    now = datetime.now()
    start_msg = (
        f"Today is {now.strftime('%A')}, {now.strftime('%d %B')}.\n"
        f"I am ready to serve you."
    )
    
    notification.notify(
        title = "🙏 Good Morning / Greetings",
        message = start_msg,
        timeout = 10
    )
    
    load_schedule()
    
    while True:
        schedule.run_pending()
        time.sleep(1)
