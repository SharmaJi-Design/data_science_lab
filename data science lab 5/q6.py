#6. Identify outliers in the Marks column using the IQR method. 
# Remove the outliers from the dataset. 
import pandas as pd
df = pd.read_csv('data.csv')

Q1 = df['Marks'].quantile(0.25)
Q3 = df['Marks'].quantile(0.75)
IQR = Q3 - Q1

print(f"Q1 (25 percentile): {Q1}")
print(f"Q3 (75 percentile): {Q3}")
print(f"IQR: {IQR}")

outliers = df[(df['Marks'] < (Q1 - 1.5 * IQR)) | (df['Marks'] > (Q3 + 1.5 * IQR))]
print("Outliers in the Marks column:")
print(outliers)
print("-" * 40)

df_no_outliers = df[~((df['Marks'] < (Q1 - 1.5 * IQR)) | (df['Marks'] > (Q3 + 1.5 * IQR)))]

print("Data shape before removing outliers:", df.shape)
print("Data shape after removing outliers:", df_no_outliers.shape)
print("Any outliers left?", df_no_outliers[((df_no_outliers['Marks'] < (Q1 - 1.5 * IQR)) | (df_no_outliers['Marks'] > (Q3 + 1.5 * IQR)))].shape[0] > 0)