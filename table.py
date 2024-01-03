import pandas as pd


with open("sales.json", "r") as file:
    data = pd.read_json(file)

# Create a Pandas DataFrame from the JSON data
df = pd.DataFrame(data)

# Order the DataFrame by total_transaction (descending)
df = df.sort_values(by="total_transaction", ascending=False)

# Print the table as a table
print(df.to_string(index=False))