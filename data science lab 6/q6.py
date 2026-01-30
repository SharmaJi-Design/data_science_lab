df_hw = sns.load_dataset("tips")[["total_bill", "tip"]]
df_hw.columns = ["Height", "Weight"]  # for lab naming

print(df_hw.head())

print("Mean:\n", df_hw.mean())
print("Variance:\n", df_hw.var())
print("Covariance:\n", df_hw.cov())
print("Correlation:\n", df_hw.corr())

sns.jointplot(x="Height", y="Weight", data=df_hw, kind="scatter")
plt.show()
