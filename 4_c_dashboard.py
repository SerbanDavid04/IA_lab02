import matplotlib.pyplot as plt
import seaborn as sns


tips = sns.load_dataset('tips')


fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('Analiza Tips - Matplotlib & Seaborn', fontsize=16, fontweight='bold')


culori = {'Male': 'blue', 'Female': 'red'}
for sex, culoare in culori.items():
    subset = tips[tips['sex'] == sex]
    axes[0, 0].scatter(subset['total_bill'], subset['tip'], label=sex, color=culoare, alpha=0.6)
axes[0, 0].set_title('Total Bill vs Tip')
axes[0, 0].set_xlabel('Total Bill ($)')
axes[0, 0].set_ylabel('Tip ($)')
axes[0, 0].legend()
axes[0, 0].grid(True, alpha=0.3)


ordine_zile = ['Thur', 'Fri', 'Sat', 'Sun']
sns.boxplot(data=tips, x='day', y='total_bill', order=ordine_zile, ax=axes[0, 1])
axes[0, 1].set_title('Distribuția Total Bill per Zi')
axes[0, 1].set_xlabel('Ziua')
axes[0, 1].set_ylabel('Total Bill ($)')


sns.histplot(data=tips, x='tip', hue='time', kde=True, ax=axes[1, 0], alpha=0.6)
axes[1, 0].set_title('Distribuția Tip - Lunch vs Dinner')
axes[1, 0].set_xlabel('Tip ($)')
axes[1, 0].set_ylabel('Frecvență')


sns.barplot(data=tips, x='day', y='tip', order=ordine_zile, ax=axes[1, 1], errorbar='ci')
axes[1, 1].set_title('Bacșiș Mediu per Zi (cu 95% CI)')
axes[1, 1].set_xlabel('Ziua')
axes[1, 1].set_ylabel('Bacșiș Mediu ($)')

plt.tight_layout()
plt.savefig('tips_analiza.png', dpi=150)
plt.show()
print("Figura salvată!")