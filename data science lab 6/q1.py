# 1. Create a dataset of hours studied and marks scored for 10 students. 
#  Calculate the covariance between the two variables. 
#  Plot the data using a scatter plot. 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

np.random.seed(42)

hours = np.random.randint(1, 10, 10)
marks = hours * 10 + np.random.randint(-5, 5, 10)

df_study = pd.DataFrame({
    "Hours_Studied": hours,
    "Marks": marks
})

print(df_study)

covariance = df_study["Hours_Studied"].cov(df_study["Marks"])
print("Covariance:", covariance)

plt.scatter(df_study["Hours_Studied"], df_study["Marks"])
plt.xlabel("Hours Studied")
plt.ylabel("Marks")
plt.title("Hours Studied vs Marks")
plt.show()


