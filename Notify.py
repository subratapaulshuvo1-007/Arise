import schedule
import time
import json
import datetime
from plyer import notification
from config import DATA_FILE

def check_and_notify():
    """টাস্ক চেক করে এবং সময় হলে নোটিফিকেশন পাঠায়।"""
    try:
        with open(DATA_FILE, 'r') as f:
            data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return  # ফাইল না থাকলে কিছু করার নেই

    now = datetime.datetime.now()
    tasks_updated = False

    for task in data.get("tasks", []):
        # যদি টাস্ক পেন্ডিং থাকে এবং এখনো নোটিফিকেশন না পাঠানো হয়
        if task.get("status") == "pending" and not task.get("notified"):
            try:
                notify_time = datetime.datetime.strptime(task["notify_at"], "%Y-%m-%d %H:%M")
                
                # যদি নোটিফিকেশনের সময় পার হয়ে যায়
                if now >= notify_time:
                    print(f"[{now.strftime('%H:%M:%S')}] Sending notification for: {task['name']}")
                    
                    # ডেস্কটপ নোটিফিকেশন পাঠানো
                    notification.notify(
                        title='টাস্কের সময় হয়েছে!',
                        message=f"এখন আপনার '{task['name']}' কাজটি করার সময়।",
                        app_name='TaskGamify',
                        timeout=15  # নোটিফিকেশনটি 15 সেকেন্ড দেখা যাবে
                    )
                    
                    task['notified'] = True  # নোটিফিকেশন পাঠানো হয়েছে বলে মার্ক করা
                    tasks_updated = True

            except (ValueError, KeyError):
                # যদি notify_at ফরম্যাট ভুল থাকে বা কী না থাকে
                continue
    
    # যদি কোনো টাস্কের স্ট্যাটাস আপডেট হয়, তাহলে ফাইলটি আবার সেভ করা
    if tasks_updated:
        with open(DATA_FILE, 'w') as f:
            json.dump(data, f, indent=4)


# প্রতি 30 সেকেন্ড পর পর check_and_notify ফাংশনটি চালানো হবে
schedule.every(30).seconds.do(check_and_notify)

print("Background Notifier is running...")
print("এই টার্মিনালটি মিনিমাইজ করে রাখুন। বন্ধ করবেন না।")

while True:
    schedule.run_pending()
    time.sleep(1)