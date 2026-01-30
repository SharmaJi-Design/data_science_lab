import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Given data
X = [10, 12, 15, 18, 20, 22, 25, 28, 30, 35]
Y = [8, 11, 14, 17, 19, 21, 24, 26, 29, 33]

# Create DataFrame
data = pd.DataFrame({"X": X, "Y": Y})

# Calculate correlation matrix
corr_matrix = data.corr()
print("Correlation Matrix:")
print(corr_matrix)

# Visualize using heatmap
plt.figure(figsize=(5,4))
sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", vmin=-1, vmax=1)
plt.title("Correlation Matrix Heatmap")
plt.show()
