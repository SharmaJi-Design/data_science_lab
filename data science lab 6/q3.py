# 3. Generate a dataset of daily temperature and ice-cream sales. 
#   Find the covariance between temperature and sales. 
#  Plot the relationship using a scatter plot. 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

np.random.seed(42)

temperature = np.random.randint(20, 40, 15)
sales = temperature * 15 + np.random.randint(-20, 20, 15)

df_sales = pd.DataFrame({
    "Temperature": temperature,
    "Ice_Cream_Sales": sales
})

print("Temperature vs Ice-Cream Sales Dataset:")
print(df_sales)

covariance = df_sales["Temperature"].cov(df_sales["Ice_Cream_Sales"])
print("\nCoveriance between temperature and ice cream sales:", covariance)

plt.scatter(df_sales["Temperature"], df_sales["Ice_Cream_Sales"])
plt.xlabel("Temperature (°C)")  
plt.ylabel("Ice-Cream Sales ($)")
plt.title("Scatter plot: Temperature vs Ice-cream sales.")
plt.show()