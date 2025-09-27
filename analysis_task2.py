import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# Load dataset (make sure participants.csv is in the same folder as this script)
df = pd.read_csv("participants.csv")

# Convert columns to numeric (just in case)
df['Attendance'] = pd.to_numeric(df['Attendance'], errors='coerce')
df['FeedbackScore'] = pd.to_numeric(df['FeedbackScore'], errors='coerce')

# === Attendance Analysis ===
attendance_by_year = df.groupby("Year")["Attendance"].mean()
attendance_by_dept = df.groupby("Department")["Attendance"].mean()

# Plot average attendance by Year
attendance_by_year.plot(kind="bar", title="Average Attendance by Year")
plt.xlabel("Year")
plt.ylabel("Average Attendance (0–5)")
plt.tight_layout()
plt.savefig("avg_attendance_by_year.png")
plt.close()

# Plot average attendance by Department
attendance_by_dept.plot(kind="bar", title="Average Attendance by Department")
plt.xlabel("Department")
plt.ylabel("Average Attendance (0–5)")
plt.tight_layout()
plt.savefig("avg_attendance_by_department.png")
plt.close()

# === Feedback Analysis ===
feedback_by_dept = df.groupby("Department")["FeedbackScore"].mean()
feedback_by_dept.plot(kind="bar", title="Average Feedback Score by Department")
plt.xlabel("Department")
plt.ylabel("Average Feedback (0–10)")
plt.tight_layout()
plt.savefig("avg_feedback_by_department.png")
plt.close()

# === Sponsorship Analysis ===
sponsorship_counts = df.groupby(["Department", "Sponsored"]).size().unstack(fill_value=0)
sponsorship_counts.plot(kind="bar", stacked=True, title="Sponsorship by Department")
plt.xlabel("Department")
plt.ylabel("Count of Participants")
plt.tight_layout()
plt.savefig("sponsorship_by_department_stacked.png")
plt.close()

print("✅ Analysis complete! Charts saved in the project folder.")
