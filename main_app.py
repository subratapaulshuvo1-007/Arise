import json
import datetime
from playsound import playsound
from config import XP_PER_TASK, XP_FOR_LEVEL_UP, RANKS, DATA_FILE, LEVEL_UP_SOUND

def load_data():
    """JSON ফাইল থেকে ডেটা লোড করে। ফাইল না থাকলে ডিফল্ট ডেটা তৈরি করে।"""
    try:
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        # যদি ফাইল না থাকে বা খালি থাকে
        return {"level": 1, "xp": 0, "tasks": []}

def save_data(data):
    """প্রদত্ত ডেটা JSON ফাইলে সেভ করে।"""
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=4)

def get_current_rank(level):
    """বর্তমান লেভেল অনুযায়ী র‍্যাঙ্ক রিটার্ন করে।"""
    current_rank = "Unranked"
    for rank_level, rank_name in sorted(RANKS.items(), reverse=True):
        if level >= rank_level:
            current_rank = rank_name
            break
    return current_rank

def check_for_level_up(data):
    """XP চেক করে এবং লেভেল আপ হলে ব্যবস্থা নেয়।"""
    if data["xp"] >= XP_FOR_LEVEL_UP:
        data["level"] += 1
        data["xp"] -= XP_FOR_LEVEL_UP
        
        new_rank = get_current_rank(data["level"])
        
        print("\n" + "="*40)
        print(f"🎉 অভিনন্দন! আপনার লেভেল আপ হয়েছে! 🎉")
        print(f"নতুন লেভেল: {data['level']}")
        print(f"বর্তমান র‍্যাঙ্ক: {new_rank}")
        print("="*40 + "\n")
        
        try:
            playsound(LEVEL_UP_SOUND)
        except Exception as e:
            print(f"সাউন্ড প্লে করা যায়নি: {e}")
        
    return data

def add_task(data):
    """নতুন টাস্ক যোগ করে।"""
    task_name = input("আপনার টাস্কের নাম লিখুন: ")
    
    while True:
        notify_time_str = input("কখন নোটিফিকেশন চান? (YYYY-MM-DD HH:MM ফরম্যাটে): ")
        try:
            # শুধু ফরম্যাট ঠিক আছে কি না তা চেক করা
            datetime.datetime.strptime(notify_time_str, "%Y-%m-%d %H:%M")
            break
        except ValueError:
            print("ভুল ফরম্যাট! দয়া করে YYYY-MM-DD HH:MM ফরম্যাটে সময় দিন (যেমন: 2023-11-20 14:30)।")

    task = {
        "id": len(data["tasks"]) + 1,
        "name": task_name,
        "status": "pending",
        "notify_at": notify_time_str,
        "notified": False  # নোটিফিকেশন পাঠানো হয়েছে কি না তার জন্য ফ্ল্যাগ
    }
    data["tasks"].append(task)
    save_data(data)
    print(f"\n✅ টাস্ক '{task_name}' সফলভাবে যোগ করা হয়েছে।\n")

def view_tasks(data):
    """পেন্ডিং টাস্কগুলো দেখায়।"""
    print("\n--- আপনার পেন্ডিং টাস্কসমূহ ---")
    pending_tasks = [t for t in data["tasks"] if t["status"] == "pending"]
    
    if not pending_tasks:
        print("কোনো পেন্ডিং টাস্ক নেই।")
    else:
        for task in pending_tasks:
            print(f"  [{task['id']}] - {task['name']} (নোটিফিকেশন: {task['notify_at']})")
    print("-" * 30 + "\n")

def complete_task(data):
    """একটি টাস্ক সম্পন্ন করে।"""
    view_tasks(data)
    if not any(t for t in data["tasks"] if t["status"] == "pending"):
        return

    try:
        task_id = int(input("যে টাস্কটি সম্পন্ন করেছেন তার ID নম্বর দিন: "))
        task_found = False
        for task in data["tasks"]:
            if task["id"] == task_id and task["status"] == "pending":
                task["status"] = "completed"
                data["xp"] += XP_PER_TASK
                task_found = True
                
                print(f"\n👍 দারুণ! '{task['name']}' টাস্কটি সম্পন্ন হয়েছে। আপনি {XP_PER_TASK} XP পেয়েছেন।")
                
                data = check_for_level_up(data)
                save_data(data)
                break
        if not task_found:
            print("ভুল ID অথবা টাস্কটি ইতিমধ্যে সম্পন্ন হয়েছে।")
    except ValueError:
        print("দয়া করে একটি সঠিক নম্বর দিন।")

def show_status(data):
    """ব্যবহারকারীর বর্তমান স্ট্যাটাস দেখায়।"""
    print("\n--- আপনার বর্তমান স্ট্যাটাস ---")
    print(f"লেভেল: {data['level']}")
    print(f"র‍্যাঙ্ক: {get_current_rank(data['level'])}")
    print(f"XP: {data['xp']}/{XP_FOR_LEVEL_UP}")
    print("-" * 30 + "\n")

def main():
    """মূল মেনু।"""
    user_data = load_data()
    print("\n" + "="*15 + " টাস্ক গ্যামিফিকেশন সিস্টেম " + "="*15)
    
    while True:
        # প্রতিবার মেনু দেখানোর আগে ডেটা রিলোড করা ভালো অভ্যাস
        user_data = load_data()
        show_status(user_data)
        
        print("মেনু:")
        print("1. নতুন টাস্ক যোগ করুন")
        print("2. পেন্ডিং টাস্কগুলো দেখুন")
        print("3. একটি টাস্ক সম্পন্ন করুন")
        print("4. প্রস্থান (Exit)")
        
        choice = input("আপনার পছন্দ নির্বাচন করুন (1-4): ")
        
        if choice == '1':
            add_task(user_data)
        elif choice == '2':
            view_tasks(user_data)
        elif choice == '3':
            complete_task(user_data)
        elif choice == '4':
            print("বিদায়! আপনার দিনটি ভালো কাটুক।")
            break
        else:
            print("ভুল ইনপুট। দয়া করে 1 থেকে 4 এর মধ্যে একটি নম্বর দিন।")

if __name__ == "__main__":
    main()