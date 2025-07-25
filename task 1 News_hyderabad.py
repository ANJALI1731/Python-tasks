import requests
import matplotlib.pyplot as plt
api_key = "06822b6de8d44376af2b9151fd930979"
categories = ['business', 'entertainment', 'health', 'science', 'sports', 'technology']
category_counts = {}
print("\n News Article Counts in Hyderabad by Category")
print("=" * 50)
for category in categories:
    url = (
        f"https://newsapi.org/v2/everything?"
        f"q=Hyderabad+{category}&"
        f"apiKey={api_key}&pageSize=100"
    )
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        count = data.get("totalResults", 0)
        count = min(count, 100)  
        category_counts[category.capitalize()] = count
        print(f"{category.capitalize():<15} {count} articles")
    else:
        category_counts[category.capitalize()] = 0
        print(f"Failed to fetch news for {category}")
labels = list(category_counts.keys())
counts = list(category_counts.values())
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0', '#ffb3e6']
plt.figure(figsize=(10, 6))
bars = plt.bar(labels, counts, color=colors)
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval + 2, yval, ha='center', fontsize=12)
plt.title("News Distribution by Category – Hyderabad", fontsize=16)
plt.xlabel("News Categories", fontsize=12)
plt.ylabel("Number of Articles", fontsize=12)
plt.ylim(0, max(counts) + 20)
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()
