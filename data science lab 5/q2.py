import pandas as pd

df = pd.read_csv('data.csv')

pd.set_option('display.float_format', '{:.2f}'.format)

print("Column Names:")
print(df.columns.tolist())
print("-" * 40)

print("Data Types:")
print(df.dtypes)
print("-" * 40)

print("Basic Statistics:")
print(df.describe())
print("-" * 40)

print("First 5 Rows:")
print(df.head())
