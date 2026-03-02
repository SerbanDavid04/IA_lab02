import seaborn as sns

tips = sns.load_dataset("tips")

print("Row, cols: ", tips.shape)
print("Tipuri de date: ", tips.dtypes)
print("Stats: ", tips.describe(include="all"))

mean_tips = tips.groupby(["day", "sex"]).mean(numeric_only=True)["tip"]
print("Avg tip: ", mean_tips)

tips_copie = tips.copy()
tips_copie["procent_bacsis"] = tips_copie["tip"] / tips_copie["total_bill"] * 100
print(tips_copie)

top5 = tips_copie["procent_bacsis"].nlargest(5)
print(top5)

count_mese = tips_copie.groupby(["day", "smoker"]).size()
print("Count mese: \n", count_mese)
