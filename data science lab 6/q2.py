# 2. Using the same dataset, compute the correlation coefficient. 
#   Interpret whether the relationship is positive, negative, or weak. 
#  Visualize it using a seaborn regression plot. 
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

np.random.seed(42)
scores = np.random.randint(50, 100, 10)
df_scores = pd.DataFrame({"Scores": scores})
print("Random Scores Dataset:")
print(df_scores)

hours = np.random.randint(1, 10, 10)
marks = hours * 10 + np.random.randint(-5, 5, 10)

df_study = pd.DataFrame({
    "Hours_Studied": hours,
    "Marks": marks
})

print("\nHours Studied vs Marks Dataset:")
print(df_study)

correlation = df_study["Hours_Studied"].corr(df_study["Marks"])
print("\nCorrelation Coefficient:", correlation)

sns.regplot(x="Hours_Studied", y="Marks", data=df_study)
plt.xlabel("Hours Studied")
plt.ylabel("Marks")
plt.title("Regression Plot: Hours Studied vs Marks")
plt.show()
