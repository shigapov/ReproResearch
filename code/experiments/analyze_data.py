# analyze_data.py
import pandas as pd

# Load the dataset
data = pd.read_csv('./data/raw_data/raw_data.csv')

# Calculate the descriptive statistics
stats = data.describe(include='all')

# Print it
print(stats)

# Save to processed_data-folder
stats.to_csv('./data/processed_data/descriptive_statistics.csv')
