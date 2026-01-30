# 4. Check for missing values in the dataset. 
# Fill missing numerical values with the mean. 
import pandas as pd

df = pd.read_csv('data.csv')

print("Missing values in each column:")
print(df.isnull().sum()) 
print("-" * 40)

numerical_cols = df.select_dtypes(include='number').columns 
df[numerical_cols] = df[numerical_cols].fillna(df[numerical_cols].mean())

print("Missing values after filling:")
print(df.isnull().sum())

