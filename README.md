# 🎯 FocusTrack — Student Productivity Analyzer

**Build better study habits. Track your progress. Understand your productivity.**

FocusTrack is a student productivity web application built with Python and Streamlit. It helps students set daily study goals, manage tasks, record daily reflections, and analyze their weekly study performance.

The project aims to make studying more organized by turning daily study activities into meaningful productivity insights.

## ✨ Features

### 📚 Study Tracking

* Set daily study-hour goals.
* Record daily study hours.
* Track progress toward study goals.
* Review your daily study performance.

### ✅ Task Management

* Add daily tasks.
* Mark tasks as completed.
* Monitor task completion.

### 📊 Weekly Analytics

* Analyze study hours over the last seven days.
* View average daily study hours.
* Track daily goal achievement.
* Review task completion statistics.
* Visualize study performance using charts and tables.

### 🧠 Advanced Productivity Insights

* Identify your most productive day.
* Calculate a study consistency score.
* Observe productivity trends.
* Receive personalized productivity recommendations.
* Generate a weekly productivity summary.

### 📝 Daily Reflection

* Record daily reflections.
* Review your study experience and progress.

### 💾 Local Data Storage

* Store productivity records in a local JSON file.
* Keep your study information available between local app sessions.

## 🛠️ Technology Stack

| Technology     | Purpose                             |
| -------------- | ----------------------------------- |
| Python         | Application logic                   |
| Streamlit      | Interactive web interface           |
| Pandas         | Data processing and analysis        |
| Matplotlib     | Data visualization                  |
| JSON           | Local data storage                  |
| Git and GitHub | Version control and project hosting |

## 🚀 Getting Started

Follow these instructions to run FocusTrack on your computer.

### Prerequisites

* Python 3.10 or a compatible version
* pip
* Git (optional, for cloning the repository)

### 1. Clone the repository

```bash
git clone https://github.com/vernayamgupta3-creator/FocusTrack.git
```

### 2. Open the project folder

```bash
cd FocusTrack
```

### 3. Create a virtual environment

```bash
python -m venv .venv
```

Activate it on Windows:

```bash
.venv\Scripts\activate
```

### 4. Install the dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the application

```bash
streamlit run app.py
```

Your browser should open the FocusTrack application automatically. If it doesn't, follow the local URL displayed in your terminal.

## 📁 Project Structure

```text
FocusTrack/
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
└── focus_data.json    # Created locally when the app saves data
```

The JSON data file may not appear in the GitHub repository because it is excluded by `.gitignore`.

## 🎯 Problem Statement

Students often struggle to maintain consistent study habits, organize daily tasks, and understand how effectively they use their study time.

FocusTrack addresses this problem by providing a simple interface for recording study hours, managing tasks, and reviewing productivity trends.

## 💡 What I Learned

Through this project, I practiced:

* Building an interactive application using Streamlit.
* Organizing application logic with Python.
* Saving and loading structured data using JSON.
* Processing data with Pandas.
* Creating charts using Matplotlib.
* Tracking changes and managing a project with Git and GitHub.
* Turning a practical student problem into a software project.

## 🔮 Future Improvements

Possible future enhancements include:

* Focus timer with study sessions and breaks.
* Subject-wise study tracking.
* Assignment and deadline management.
* Exam countdowns.
* Downloadable productivity reports.
* Improved data backup and multi-user support.

These are planned improvements, not features currently claimed to be implemented.

## 👨‍💻 About the Project

FocusTrack is a student-built project developed to practice Python programming, data analysis, and application development while exploring practical solutions to student productivity challenges.

**Project:** FocusTrack — Student Productivity Analyzer
**Repository:** [GitHub](https://github.com/vernayamgupta3-creator/FocusTrack)

---

⭐ If you find this project interesting, consider giving the repository a star!
