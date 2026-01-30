# 5. Detect duplicate rows in the dataset. 
# Remove duplicates and verify the result. 
import pandas as pd
df = pd.read_csv('data.csv')

duplicates = df.duplicated()
print("Duplicates rows (True = duplicate):")
print(duplicates)
print("-"*40)

print("Duplicates rows in the dataset:")
print(df[duplicates])
print("-"*40)

df_cleaned = df.drop_duplicates()

print("Shape before removing duplicates:",df.shape)
print("Shape after removing duplicates:",df_cleaned.shape)
print("Any duplicates left?",df_cleaned.duplicated().any())