import time
import schedule
from plyer import notification
from datetime import datetime

# --- 1. Message delivery system (Notification Function) ---
def send_alert(karma_name, time_period):
    now = datetime.now()
    today_date = now.strftime("%d %B")  # e.g., 25 October
    today_day = now.strftime("%A")      # e.g., Wednesday
    
    print(f"🔔 Alert: {karma_name} ({today_day})")
    
    notification.notify(
        title = f"📅 {today_day} | {today_date}",
        message = (
            f"⏰ Time: {time_period}\n"
            f"🙏 Today's task: {karma_name}\n"
            f"Give up laziness and get to work."
        ),
        timeout = 10
    )

# --- 2. Master Controller (Smart Scheduler) ---
# Here we have added 'day' or weekday-based scheduling
def set_karma(day, time_range, task_name):
    # Remove mechanical formatting issues
    clean_range = time_range.replace("–", "-")
    start_time = clean_range.split("-")[0].strip()
    
    if len(start_time) == 4:
        start_time = "0" + start_time

    # Schedule based on weekday logic
    try:
        # Convert to lowercase to avoid mismatch
        d = day.lower().strip()

        if d == "daily":
            schedule.every().day.at(start_time).do(
                send_alert, task_name, clean_range
            )
            print(f"✅ Daily task: '{task_name}' scheduled for every day.")
            
        elif d == "sunday":
            schedule.every().sunday.at(start_time).do(
                send_alert, task_name, clean_range
            )
            print(f"✅ Sunday task: '{task_name}' scheduled.")
            
        elif d == "monday":
            schedule.every().monday.at(start_time).do(
                send_alert, task_name, clean_range
            )
            print(f"✅ Monday task: '{task_name}' scheduled.")
            
        elif d == "tuesday":
            schedule.every().tuesday.at(start_time).do(
                send_alert, task_name, clean_range
            )
            
        elif d == "wednesday":
            schedule.every().wednesday.at(start_time).do(
                send_alert, task_name, clean_range
            )
            
        elif d == "thursday":
            schedule.every().thursday.at(start_time).do(
                send_alert, task_name, clean_range
            )
            
        elif d == "friday":
            schedule.every().friday.at(start_time).do(
                send_alert, task_name, clean_range
            )
            
        elif d == "saturday":
            schedule.every().saturday.at(start_time).do(
                send_alert, task_name, clean_range
            )
        
        else:
            print(
                f"⚠️ Warning: Unable to recognize a day named '{day}'. "
                f"Please check the spelling."
            )
            
    except Exception as e:
        print(f"❌ Error: There is a problem in the settings for '{task_name}'.")

# --- 3. Your routine (Daily & Weekly Routine) ---
def load_schedule():
    print("--- Loading Karma Routine ---")

    # === A) Daily tasks (executed every day) ===
    # Format: set_karma("daily", "time", "task")
    
    set_karma("daily", "08:00-08:30", "Wake up & Fresh (Morning routine)")
    set_karma("daily", "13:00-14:00", "Lunch Break")
    set_karma("daily", "23:00-00:00", "Sleep Preparation")

    # === B) Day-specific tasks ===
    # Format: set_karma("day", "time", "task")

    # Sunday
    set_karma("sunday", "07:00-09:00", "Heavy Coding Practice")
    set_karma("sunday", "10:00-12:00", "Web dev Practice")
    set_karma("sunday", "13:00-14:00", "Client Outreach")
    set_karma("sunday", "15:00-17:00", "Client Task")
    set_karma("sunday", "18:00-19:00", "Robotics Practice")
    set_karma("sunday", "19:30-20:30", "CSE Class")
    set_karma("sunday", "21:00-22:00", "AI/ML Practice")
    set_karma("sunday", "23:00-01:00", "PROJECTS(Real,SaaS)")

    # Monday -> 
    set_karma("monday", "07:00-09:00", "Design Theory Study")
    set_karma("monday", "10:00-12:00", "UI/UX Designing (Figma)")
    set_karma("monday", "13:00-14:00", "Client Hunting")
    set_karma("monday", "15:00-17:00", "Client Task")
    set_karma("monday", "18:00-19:00", "Robotics Class")
    set_karma("monday", "19:30-20:30", "CSE Class")
    set_karma("monday", "21:00-22:00", "AI/ML Class")
    set_karma("monday", "23:00-01:00", "PROJECTS (Real,SaaS)")
    
    # Tuesday
    set_karma("tuesday", "07:00-09:00", "Heavy Coding Practice")
    set_karma("tuesday", "10:00-12:00", "Web dev Practice")
    set_karma("tuesday", "13:00-14:00", "Client Outreach")
    set_karma("tuesday", "15:00-17:00", "Client Task")
    set_karma("tuesday", "18:00-19:00", "Robotics Practice")
    set_karma("tuesday", "19:30-20:30", "CSE Class")
    set_karma("tuesday", "21:00-22:00", "AI/ML Practice")
    set_karma("tuesday", "23:00-01:00", "PROJECTS(Real,SaaS)")
    
    # Wednesday
    set_karma("wednesday", "07:00-09:00", "Design Theory Study")
    set_karma("wednesday", "10:00-12:00", "UI/UX Designing (Figma)")
    set_karma("wednesday", "13:00-14:00", "Client Hunting")
    set_karma("wednesday", "15:00-17:00", "Client Task")
    set_karma("wednesday", "18:00-19:00", "Robotics Class")
    set_karma("wednesday", "19:30-20:30", "CSE Class")
    set_karma("wednesday", "21:00-22:00", "AI/ML Class")
    set_karma("wednesday", "23:00-01:00", "PROJECTS (Real,SaaS)")
    
    # Thursday
    set_karma("thursday", "07:00-09:00", "Heavy Coding Practice")
    set_karma("thursday", "10:00-12:00", "Web dev Practice")
    set_karma("thursday", "13:00-14:00", "Client Outreach")
    set_karma("thursday", "15:00-17:00", "Client Task")
    set_karma("thursday", "18:00-19:00", "Robotics Practice")
    set_karma("thursday", "19:30-20:30", "CSE Class")
    set_karma("thursday", "21:00-22:00", "AI/ML Practice")
    set_karma("thursday", "23:00-01:00", "PROJECTS(Real,SaaS)")

    #Friday
    set_karma("friday", "07:00-10:00", "Test")
    set_karma("friday", "09:00-12:00", "Assets Sell")
    set_karma("friday", "13:00-14:00", "New/Next Plan")
    set_karma("friday", "15:00-16:00", "Review Clients")
    set_karma("friday", "16:00-18:00", "Robotics Projects")
    set_karma("friday", "19:00-21:00", "CSE Projects")
    set_karma("friday", "22:00-00:00", "AI/ML Projects")
    set_karma("friday", "00:00-01:00", "Projects Launching Day & Next Projects Plan")

    #Saturday
    set_karma("saturday", "07:00-09:00", "Design Theory Study")
    set_karma("saturday", "09:00-12:00", "UI/UX Designing (Figma)")
    set_karma("saturday", "13:00-14:00", "Client Hunting")
    set_karma("saturday", "15:00-17:00", "Client Task")
    set_karma("saturday", "18:00-19:00", "Robotics Class")
    set_karma("saturday", "19:30-20:30", "CSE Class")
    set_karma("saturday", "21:00-22:00", "AI/ML Class")
    set_karma("saturday", "23:00-01:00", "PROJECTS (Real,SaaS)")



    print("----------------------------")

# --- 4. Main engine ---
if __name__ == "__main__":
    
    # Startup message
    now = datetime.now()
    day_name = now.strftime('%A')  # Today's weekday
    
    notification.notify(
        title = f"🙏 Happy {day_name}",
        message = (
            "HAR HAR MAHADEV, If I don't work, I will go out of my dream."
        ),
        timeout = 10
    )
    
    load_schedule()
    
    while True:
        schedule.run_pending()
        time.sleep(1)
