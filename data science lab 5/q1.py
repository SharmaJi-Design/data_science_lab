import pandas as pd

# Create a sample DataFrame
data = {
    'Name': ['Rohit', 'Amit', 'Razz', 'Rocky', 'Hrtik'],
    'Age': [20, 21, 19, 22, 20],
    'Marks': [85, 58, 90, 45, 75]
}

df = pd.DataFrame(data)

# Display first 5 rows
print("First 5 rows:\n", df.head())

# Display dataset shape
print("Dataset shape:", df.shape)
