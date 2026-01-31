# 🚀 Arise: The Smart Karma Tracker & Planner

> *"Action is thy duty, reward is not thy concern."* — A Python-based productivity ecosystem designed to bridge the gap between **Planning** and **Execution**.

---

## 🧐 Why I Built This? (The Motivation)
In the chaos of modern digital life, maintaining consistency is the hardest challenge. I realized that simple "To-Do" lists are passive—they wait for you to check them. I needed something **active**, something that acts as a strictly disciplined digital assistant.

I created **Arise** to transform my daily routine into a system of "Karma Yoga" (Discipline of Action), ensuring that no day passes without progress.

---

## 🛠 What Problem Does It Solve?
Most productivity tools fail because:
1.  **We forget:** We plan in the morning but lose track by noon.
2.  **Lack of Structure:** Doing random things at random times leads to burnout.
3.  **Invisible Progress:** We work hard but don't see the cumulative result, leading to demotivation.

**Arise solves this by:**
*   🔔 **Nagging you** with background notifications until you start working.
*   📅 **Dynamic Scheduling:** Blocking irrelevant tasks (e.g., stopping you from doing "Design" on a "Coding Day").
*   📊 **Visualizing Progress:** Showing a GitHub-style "Green Light" grid to gamify consistency.

---

## 🎯 Who Is This For?
This tool is crafted for **The Seekers of Discipline**:
*   **Students & Learners:** Who need to balance multiple subjects (Coding, Math, Design).
*   **Developers & Freelancers:** Who juggle between client work, learning, and health.
*   **Self-Improvers:** Anyone who wants to track habits like Reading, Meditation, or Exercise alongside professional work.

---

## ✨ Key Features & Benefits

### 1. 🧠 Dynamic Day-wise Planner
Unlike rigid trackers, this system is smart. It knows the difference between a **Sunday** and a **Monday**.
*   *Sunday* is for **Heavy Coding**? The planner activates only coding tasks.
*   *Monday* is for **Design**? Coding tasks become disabled/greyed out.
This forces you to focus on the **Right Task at the Right Time**.

### 2. 🔔 The Invisible Guardian (Background Service)
A lightweight script (`my_tracker.pyw`) runs silently in the background. It wakes up at specific times to send system notifications, reminding you of your current duty.

### 3. 📊 Visual Analytics (The Mirror)
*   **Future Planner:** Plan your week ahead with a visual dashboard.
*   **GitHub-Style Grid:** A heatmap of your consistency. The more you work, the greener it gets.
*   **Bar Charts:** Analyze your performance over the last 7 days.

---

## 💻 Tech Stack
*   **Language:** Python 3.x
*   **GUI:** Tkinter (Custom styled)
*   **Notifications:** Plyer
*   **Scheduling:** Schedule Library
*   **Analytics:** Matplotlib & JSON (Local Database)

---

## 🚀 How to Run
1.  Clone the repository.
2.  Install dependencies:
    ```bash
    pip install schedule plyer matplotlib
    ```
3.  Run the background notifier:
    ```bash
    pythonw my_tracker.pyw
    ```
4.  Open the Dashboard/Planner:
    ```bash
    python super_tracker.py
    ```

---

> Built with ❤️ and Discipline by **Subrata_Paul_Shuvo**.
