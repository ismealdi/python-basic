import pandas as pd
import matplotlib.pyplot as plt

# Read JSON data from file
with open("sales.json", "r") as file:
    data = pd.read_json(file)

# Create DataFrame
df = pd.DataFrame(data)

# Order by total_transaction (descending)
df = df.sort_values(by="total_transaction", ascending=False)

# Create pie chart
plt.figure(figsize=(8, 6))  # Adjust figure size as needed
plt.pie(df["total_transaction"], labels=df["customer_name"], autopct="%1.1f%%")
plt.title("Sales Distribution by Customer")
plt.show()