import pandas as pd

# Define the filename (use the actual filename generated in the previous step)
filename = "SAP.DE_2024-06-02.csv"

# Read the CSV file into a DataFrame
data = pd.read_csv(filename)

# Display the first few rows of the DataFrame
print(data.head())

# Optionally, display more detailed information about the DataFrame
print(data.info())
print(data.describe())
