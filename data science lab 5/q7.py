# 7. Create a new column by transforming Marks (e.g., Marks / 10). 
# Rename columns and save the cleaned dataset to a CSV file. 
import pandas as pd

df = pd.read_csv('data.csv')
df['Transformed_Marks'] = df['Marks'] / 10

df.rename(columns={'Name': 'Student_Name', 'Marks': 'Original_Marks'}, inplace=True)

df.to_csv('cleaned_data.csv', index=False)
print("Cleaned dataset saved to 'cleaned_data.csv'")
print(df)   
