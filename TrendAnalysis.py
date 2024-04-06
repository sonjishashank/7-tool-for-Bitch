import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load your crime data into a DataFrame (replace 'crime_data.csv' with your file)
crime_df = pd.read_csv('crime_data.csv')

# Assuming your dataset has a datetime column named 'date_time'
crime_df['date_time'] = pd.to_datetime(crime_df['date_time'])

# Extract features like hour, day of the week, month, and season
crime_df['hour'] = crime_df['date_time'].dt.hour
crime_df['day_of_week'] = crime_df['date_time'].dt.dayofweek
crime_df['month'] = crime_df['date_time'].dt.month
crime_df['season'] = (crime_df['date_time'].dt.month % 12 + 3) // 3

# Plot the trend of crime occurrence by hour
plt.figure(figsize=(10, 6))
sns.countplot(x='hour', data=crime_df, palette='muted')
plt.title('Crime Occurrence by Hour')
plt.xlabel('Hour of the Day')
plt.ylabel('Number of Crimes')
plt.show()

# Plot the trend of crime occurrence by day of the week
plt.figure(figsize=(10, 6))
sns.countplot(x='day_of_week', data=crime_df, palette='muted')
plt.title('Crime Occurrence by Day of the Week')
plt.xlabel('Day of the Week (0=Monday, 6=Sunday)')
plt.ylabel('Number of Crimes')
plt.show()

# Plot the trend of crime occurrence by month
plt.figure(figsize=(10, 6))
sns.countplot(x='month', data=crime_df, palette='muted')
plt.title('Crime Occurrence by Month')
plt.xlabel('Month')
plt.ylabel('Number of Crimes')
plt.show()

# Plot the trend of crime occurrence by season
plt.figure(figsize=(10, 6))
sns.countplot(x='season', data=crime_df, palette='muted')
plt.title('Crime Occurrence by Season')
plt.xlabel('Season (1=Winter, 2=Spring, 3=Summer, 4=Autumn)')
plt.ylabel('Number of Crimes')
plt.show()
