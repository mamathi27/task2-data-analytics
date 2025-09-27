# Task 2 — Data Analytics / Visualization

This repository contains the analysis and visualizations for Task 2, using a sample participants dataset.

## Dataset

- `participants.csv` — Sample dataset with participant details, attendance, feedback, and sponsorship information.
- Columns:
  - `Name`, `Year`, `Department`, `Section`, `Email`, `Phone`, `Attendance`, `FeedbackScore`, `Sponsored`

## Analysis

1. **Attendance Patterns**
   - Average attendance by **Year** (I, II, III, IV)
   - Average attendance by **Department** (CSE, IT, ECE, etc.)
   - Heatmap of attendance by **Department vs Year**

2. **Feedback Analysis**
   - Average feedback score by **Department**

3. **Sponsorship Analysis**
   - Distribution of participants who sponsored events (`Yes/No`) by Department

## Visualizations

- `avg_attendance_by_year.png`
- `avg_attendance_by_department.png`
- `attendance_dept_year_heatmap.png`
- `avg_feedback_by_department.png`
- `sponsorship_by_department_stacked.png`

## How to Run

1. Ensure you have Python 3.x installed.
2. Install required packages:
   ```bash
   pip install pandas matplotlib
   ```
3.Place participants.csv in the same folder as analysis_task2.py.
4.Run the script:
```bash
python analysis_task2.py

```
5.The charts will be generated in the same folder.
## Insights
-Average attendance varies slightly across Years and Departments.
-Some departments consistently have higher feedback scores.
-Sponsorship distribution shows which departments are more likely to sponsor events.
