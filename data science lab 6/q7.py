linear = np.arange(1, 51)
random = np.random.randint(1, 50, 50)

df_compare = pd.DataFrame({
    "Linear": linear,
    "Random": random
})

print("Covariance:", df_compare["Linear"].cov(df_compare["Random"]))
print("Correlation:", df_compare["Linear"].corr(df_compare["Random"]))

plt.scatter(df_compare["Linear"], df_compare["Random"])
plt.xlabel("Linear Variable")
plt.ylabel("Random Variable")
plt.title("Linear vs Random")
plt.show()
