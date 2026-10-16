import streamlit as st
import json
from pathlib import Path
from datetime import date

# ----------------------------------
# PAGE SETTINGS
# ----------------------------------

st.set_page_config(
    page_title="FocusTrack | Student Productivity",
    page_icon="🎯",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ----------------------------------
# CUSTOM DASHBOARD DESIGN
# ----------------------------------

st.markdown("""
<style>

/* Main application background */
.stApp {
    background-color: #FFFFFF;
}

/* Main content spacing */
.block-container {
    padding-top: 2rem;
    padding-bottom: 3rem;
}

/* Main headings */
h1, h2, h3 {
    color: #172554;
    font-weight: 700;
}

/* Paragraph text */
p, label {
    color: #334155;
}

/* Metric cards */
[data-testid="stMetric"] {
    background-color: white;
    padding: 20px;
    border-radius: 14px;
    border: 1px solid #E2E8F0;
    box-shadow: 0 3px 10px rgba(15, 23, 42, 0.04);
}

/* Buttons */
.stButton > button {
    background-color: #2563EB;
    color: white;
    border: none;
    border-radius: 9px;
    padding: 0.55rem 1rem;
    font-weight: 600;
}

/* Button hover */
.stButton > button:hover {
    background-color: #1D4ED8;
    color: white;
}

/* Input fields */
.stTextInput input,
.stNumberInput input,
.stTextArea textarea {
    border-radius: 8px;
}

/* Sidebar */
[data-testid="stSidebar"] {
    background-color: #EAF0FA;
}

/* Dividers */
hr {
    border-color: #DCE3EF;
}

</style>
""", unsafe_allow_html=True)
# ----------------------------------
# PERMANENT STORAGE
# ----------------------------------

DATA_FILE = Path(__file__).parent / "focus_data.json"


def load_data():
    """Load saved information from the JSON file."""

    if DATA_FILE.exists():
        try:
            with open(DATA_FILE, "r", encoding="utf-8") as file:
                return json.load(file)
        except (json.JSONDecodeError, OSError):
            return {}

    return {}


def save_data(data):
    """Save information permanently to the JSON file."""

    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)


# Load saved information
data = load_data()

# Today's date is used as the record key
today = date.today().isoformat()

# Create today's record if it doesn't exist
if today not in data:
    data[today] = {
        "goal": 3,
        "studied": 0.0,
        "tasks": [],
        "reflection": ""
    }
    save_data(data)

today_data = data[today]

# ----------------------------------
# APPLICATION HEADER
# ----------------------------------

st.title("🎯 FocusTrack")
st.subheader("Student Productivity Analyzer")

st.write(
    "Track your study hours, manage your tasks, "
    "and build better study habits."
)

st.caption(f"Today's date: {today}")

st.divider()

# ----------------------------------
# STUDY TRACKER
# ----------------------------------

st.header("📚 Study Tracker")

goal = st.number_input(
    "Daily study goal (hours)",
    min_value=1,
    max_value=24,
    value=int(today_data["goal"]),
    key="study_goal"
)

studied = st.number_input(
    "Hours studied today",
    min_value=0.0,
    max_value=24.0,
    value=float(today_data["studied"]),
    step=0.5,
    key="study_hours"
)

# Save study information automatically
today_data["goal"] = goal
today_data["studied"] = studied

save_data(data)

# Calculate study progress
progress = min(studied / goal, 1.0)

st.progress(progress)

st.write(f"Study goal completed: {progress * 100:.1f}%")

if studied >= goal:
    st.success("Excellent! You achieved your study goal! 🎉")
else:
    remaining = goal - studied
    st.info(f"You have {remaining:.1f} hours left.")

st.divider()

# ----------------------------------
# TASK MANAGER
# ----------------------------------

st.header("✅ Daily Task Manager")

with st.form("add_task_form", clear_on_submit=True):

    new_task = st.text_input(
        "Enter a new task",
        placeholder="Example: Complete Python assignment"
    )

    add_task = st.form_submit_button("➕ Add Task")

    if add_task:
        if new_task.strip():

            today_data["tasks"].append({
                "name": new_task.strip(),
                "completed": False
            })

            save_data(data)
            st.rerun()

        else:
            st.warning("Please enter a task.")

# Display saved tasks
if today_data["tasks"]:

    for index, task in enumerate(today_data["tasks"]):

        completed = st.checkbox(
            task["name"],
            value=task["completed"],
            key=f"task_{today}_{index}"
        )

        today_data["tasks"][index]["completed"] = completed

    # Save task completion changes
    save_data(data)

    total_tasks = len(today_data["tasks"])

    completed_tasks = sum(
        task["completed"]
        for task in today_data["tasks"]
    )

    st.write(
        f"Completed tasks: {completed_tasks}/{total_tasks}"
    )

    task_progress = completed_tasks / total_tasks

    st.progress(task_progress)

    if completed_tasks == total_tasks:
        st.success("All tasks completed! 🎉")

    if st.button("🗑️ Clear All Tasks"):

        today_data["tasks"] = []

        save_data(data)
        st.rerun()

else:
    st.info("You haven't added any tasks yet.")

st.divider()

# ----------------------------------
# DAILY REFLECTION
# ----------------------------------

st.header("📝 Daily Reflection")

reflection = st.text_area(
    "What did you learn today?",
    value=today_data["reflection"],
    placeholder="Write about what you learned..."
)

if st.button("💾 Save Reflection"):

    today_data["reflection"] = reflection

    save_data(data)

    st.success("Your reflection has been saved!")

st.divider()

# ----------------------------------
# FOOTER
# ----------------------------------
# ----------------------------------
# WEEKLY ANALYTICS
# ----------------------------------

import pandas as pd
import matplotlib.pyplot as plt
from datetime import timedelta

st.divider()
st.header("📊 Weekly Analytics")

# Get the last seven days, including today
today_date = date.today()

weekly_records = []

for i in range(6, -1, -1):
    current_date = today_date - timedelta(days=i)
    date_key = current_date.isoformat()

    record = data.get(date_key, {})

    weekly_records.append({
        "Day": current_date.strftime("%a"),
        "Date": date_key,
        "Study Hours": float(record.get("studied", 0)),
        "Goal": float(record.get("goal", 3)),
        "Tasks": len(record.get("tasks", [])),
        "Completed": sum(
            task.get("completed", False)
            for task in record.get("tasks", [])
        )
    })

# Convert records into a table
df = pd.DataFrame(weekly_records)

# Calculate weekly statistics
total_hours = df["Study Hours"].sum()
daily_average = total_hours / 7

days_goal_achieved = sum(
    df["Study Hours"] >= df["Goal"]
)

goal_percentage = (days_goal_achieved / 7) * 100

total_tasks = df["Tasks"].sum()
completed_tasks = df["Completed"].sum()

# Display statistics
col1, col2 = st.columns(2)

with col1:
    st.metric("⏱️ Weekly Study Hours", f"{total_hours:.1f}")

with col2:
    st.metric("📚 Daily Average", f"{daily_average:.1f} hrs")

col3, col4 = st.columns(2)

with col3:
    st.metric("🎯 Goal Achievement", f"{goal_percentage:.1f}%")

with col4:
    st.metric(
        "✅ Tasks Completed",
        f"{completed_tasks}/{total_tasks}"
    )

# Study hours chart
st.subheader("📈 Study Hours — Last 7 Days")

fig, ax = plt.subplots()

ax.bar(df["Day"], df["Study Hours"])

ax.set_xlabel("Day")
ax.set_ylabel("Study Hours")
ax.set_title("Daily Study Progress")

ax.set_ylim(
    bottom=0,
    top=max(1, df["Study Hours"].max() * 1.2)
)

st.pyplot(fig)
plt.close(fig)

# Show detailed weekly records
st.subheader("📅 Weekly Study Records")

st.dataframe(
    df[["Date", "Study Hours", "Goal", "Tasks", "Completed"]],
    use_container_width=True,
    hide_index=True
)

# ----------------------------------
# ADVANCED PRODUCTIVITY INSIGHTS
# ----------------------------------

st.divider()
st.header("🚀 Advanced Productivity Insights")

# 1. Most Productive Day
if total_hours > 0:

    best_day_index = df["Study Hours"].idxmax()
    best_day = df.loc[best_day_index, "Day"]
    best_hours = df.loc[best_day_index, "Study Hours"]

    st.subheader("🏆 Most Productive Day")

    st.success(
        f"Your most productive day was {best_day}, "
        f"with {best_hours:.1f} hours of study."
    )

else:
    st.info(
        "Start recording your study hours to discover "
        "your most productive day."
    )


# 2. Study Consistency Score
st.subheader("🔥 Study Consistency")

consistency_score = (days_goal_achieved / 7) * 100

st.metric(
    "Study Goal Consistency",
    f"{consistency_score:.1f}%"
)

st.progress(consistency_score / 100)

if consistency_score >= 80:
    st.success("Fantastic consistency! Keep up the great work! 🌟")

elif consistency_score >= 50:
    st.info("Good progress! Try to achieve your goal on more days.")

else:
    st.info(
        "Build a regular study routine. Start with small, "
        "achievable daily goals."
    )


# 3. Productivity Trend
st.subheader("📈 Productivity Trend")

first_half = df.iloc[:3]["Study Hours"].mean()
second_half = df.iloc[4:]["Study Hours"].mean()

if second_half > first_half:
    st.success(
        "Your average study hours increased in the later "
        "part of the week. Keep going! 📈"
    )

elif second_half < first_half:
    st.info(
        "Your average study hours decreased in the later "
        "part of the week. Consider planning your time "
        "more carefully."
    )

else:
    st.info(
        "Your study hours remained approximately stable "
        "across the two parts of the week."
    )


# 4. Personalized Recommendations
st.subheader("💡 Your Productivity Recommendations")

if total_hours == 0:

    st.write(
        "📚 Record your daily study hours to receive "
        "personalized productivity insights."
    )

else:

    if daily_average < 2:
        st.write(
            "📖 **Study routine:** Try starting with "
            "two focused study hours per day."
        )

    else:
        st.write(
            "👏 **Study routine:** Your daily average is "
            f"{daily_average:.1f} hours. Keep maintaining "
            "a consistent schedule."
        )

    if goal_percentage < 50:
        st.write(
            "🎯 **Goal setting:** Try smaller daily goals "
            "that fit your college timetable."
        )

    else:
        st.write(
            "✅ **Goal setting:** You're achieving your "
            "goals regularly. Keep challenging yourself "
            "with realistic targets."
        )

    if total_tasks > 0:

        task_completion_rate = (
            completed_tasks / total_tasks
        ) * 100

        st.write(
            f"📋 **Task completion:** You've completed "
            f"{task_completion_rate:.1f}% of your recorded "
            "tasks this week."
        )

    else:
        st.write(
            "📋 **Task management:** Add daily tasks to "
            "track your completion rate."
        )


# ----------------------------------
# WEEKLY SUMMARY
# ----------------------------------

st.divider()
st.header("📋 Your Weekly Summary")

summary_col1, summary_col2, summary_col3 = st.columns(3)

with summary_col1:
    st.metric(
        "Total Study Hours",
        f"{total_hours:.1f} hrs"
    )

with summary_col2:
    st.metric(
        "Goals Achieved",
        f"{days_goal_achieved}/7 days"
    )

with summary_col3:
    st.metric(
        "Tasks Completed",
        f"{completed_tasks}/{total_tasks}"
    )

st.caption(
    "FocusTrack | Small steps lead to big achievements. 🎯"
)