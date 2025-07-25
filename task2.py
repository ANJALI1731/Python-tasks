import pandas as pd
import matplotlib.pyplot as plt
from fpdf import FPDF
from PIL import Image

# Loading the CSV
df = pd.read_csv("weather_report.csv")

# PIE CHART 
# Count and group by Condition
condition_counts = df['Condition'].value_counts()
grouped_states = df.groupby('Condition')['State'].apply(list)

# Create pie chart
labels = [f"{cond} ({count})" for cond, count in condition_counts.items()]
sizes = condition_counts.values

fig, ax = plt.subplots(figsize=(8, 6))
wedges, texts, autotexts = ax.pie(
    sizes, labels=labels, autopct='%1.1f%%', startangle=140, textprops={'fontsize': 9}
)
legend_labels = [f"{cond}: {', '.join(states)}" for cond, states in grouped_states.items()]
ax.legend(wedges, legend_labels, title="States by Weather", loc="center left", bbox_to_anchor=(1, 0.5), fontsize=8)

plt.tight_layout()
pie_image_path = "weather_pie_chart.png"
plt.savefig(pie_image_path)
plt.close()

# PDF GENERATION 
pdf = FPDF()
pdf.add_page()

# Title
pdf.set_font("Arial", 'B', 16)
pdf.cell(0, 10, "Weather Report - India (18-07-2025)", ln=True, align='C')

# Table Headers
pdf.set_font("Arial", 'B', 12)
pdf.ln(10)
pdf.cell(60, 10, "State", 1)
pdf.cell(40, 10, "Temperature (°C)", 1)
pdf.cell(40, 10, "Humidity (%)", 1)
pdf.cell(50, 10, "Condition", 1)
pdf.ln()

# Table Data
pdf.set_font("Arial", '', 11)
for i, row in df.iterrows():
    pdf.cell(60, 10, row["State"], 1)
    pdf.cell(40, 10, str(row["Temperature"]), 1)
    pdf.cell(40, 10, str(row["Humidity"]), 1)
    pdf.cell(50, 10, row["Condition"], 1)
    pdf.ln()

# Weather Condition Counts with States
pdf.ln(5)
pdf.set_font("Arial", 'B', 13)
pdf.cell(0, 10, "Weather Condition Summary", ln=True)
pdf.set_font("Arial", '', 11)

for cond, states in grouped_states.items():
    count = condition_counts[cond]
    state_list = ', '.join(states)
    pdf.multi_cell(0, 8, f"{cond} ({count}): {state_list}")

# Add Pie Chart Image
pdf.ln(5)
pdf.set_font("Arial", 'B', 12)
pdf.cell(0, 10, "Weather Distribution Pie Chart", ln=True)
pdf.image(pie_image_path, x=25, w=160)

# Save PDF
pdf.output("weather_report_final.pdf")
print("✅ PDF saved as 'weather_report_final.pdf'")
