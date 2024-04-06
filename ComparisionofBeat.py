import modin.pandas as pd

# Load the dataset with Modin
df = pd.read_csv('Fir without zero.csv')

# Group the data by 'Year' and 'Beat_Name' to get the count of crimes
df_analyse = df.groupby(['Year', 'District_Name', 'Beat_Name']).size().reset_index()
df_analyse.columns = ['Year', 'District_Name', 'Beat_Name', 'Number of crimes']

# Get unique years and districts for filtering
unique_years = df_analyse['Year'].unique()
unique_districts = df_analyse['District_Name'].unique()

# Get user input for preferred year and district
preferred_year = int(input("Enter the preferred year: "))
preferred_district = input("Enter the preferred district: ")

# Check if the preferred year and district exist in the dataset
if (preferred_year not in unique_years) or (preferred_district not in unique_districts):
    print("Data for the preferred year or district not found.")
else:
    # Filter the data based on user preferences
    filtered_data = df_analyse[(df_analyse['Year'] == preferred_year) & (df_analyse['District_Name'] == preferred_district)]

    if filtered_data.empty:
        print("No data found for the selected year and district.")
    else:
        # Rank the beats based on the number of crimes reported
        ranked_beats = filtered_data.sort_values(by='Number of crimes', ascending=False)

        # Print the ranking list
        print(f"Ranking of beats with the highest number of crimes for Year {preferred_year} and District {preferred_district}:")
        for rank, (beat, num_crimes) in enumerate(zip(ranked_beats['Beat_Name'], ranked_beats['Number of crimes']), start=1):
            print(f"Rank {rank}: {beat} - Number of Crimes: {num_crimes}")

        # Save the ranking list to a text file
        with open(f'crime_ranking_{preferred_year}_{preferred_district}.txt', 'w') as f:
            f.write(f"Ranking of beats with the highest number of crimes for Year {preferred_year} and District {preferred_district}:\n")
            for rank, (beat, num_crimes) in enumerate(zip(ranked_beats['Beat_Name'], ranked_beats['Number of crimes']), start=1):
                f.write(f"Rank {rank}: {beat} - Number of Crimes: {num_crimes}\n")

        print(f"Ranking for Year {preferred_year} and District {preferred_district} has been saved to 'crime_ranking_{preferred_year}_{preferred_district}.txt'.")
