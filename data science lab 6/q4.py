# 4. Calculate the correlation for the temperature vs ice-cream sales dataset. 
#  Compare the covariance and correlation values. 
#  Explain why correlation is easier to interpret. 
import numpy as np
import pandas as pd

np.random.seed(42)

temperature = np.random.randint(20, 40, 15)
sales = temperature * 15 + np.random.randint(-20, 20, 15)

df_sales = pd.DataFrame({
    "Temperature": temperature,
    "Ice_cream_sales": sales
})

print("Temperature vs Ice-cream sales dataset:")
print(df_sales)

covariance = df_sales["Temperature"],df_sales["Ice_cream_sales"]
correlation = df_sales["Temperature"].corr(df_sales["Ice_cream_sales"])

print("\nCovariance between temperature and ice-cream sales:", covariance)

print("Correlation between temperature and ice-cream sales:", correlation)

dice = np.random.randint(1, 7, 1000)
df_dice = pd.DataFrame({"Dice_Rolls": dice})

print("\nDice roll dataset (first 5 values)")
print(df_dice.head())