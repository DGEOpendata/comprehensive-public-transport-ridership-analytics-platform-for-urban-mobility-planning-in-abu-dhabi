import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load ridership dataset
file_path = 'Public_Transport_Ridership_Statistics.csv'
data = pd.read_csv(file_path)

# Data cleaning and processing
data['date'] = pd.to_datetime(data['date'])
data['month'] = data['date'].dt.month
data['year'] = data['date'].dt.year

# Aggregating monthly ridership
data_monthly = data.groupby(['year', 'month']).agg({
    'total_ridership': 'sum',
    'peak_hours_ridership': 'sum',
    'off_peak_hours_ridership': 'sum'
}).reset_index()

# Plotting monthly ridership trends
plt.figure(figsize=(12, 6))
sns.lineplot(data=data_monthly, x='month', y='total_ridership', hue='year', marker='o')
plt.title('Monthly Public Transport Ridership Trends')
plt.xlabel('Month')
plt.ylabel('Total Ridership')
plt.legend(title='Year')
plt.grid()
plt.show()

# Export cleaned data to JSON cleaned_data_path = 'Cleaned_Public_Transport_Ridership_Statistics.json'
data_monthly.to_json(cleaned_data_path, orient='records')