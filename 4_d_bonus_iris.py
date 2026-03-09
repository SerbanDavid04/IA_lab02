import matplotlib.pyplot as plt
import seaborn as sns


iris = sns.load_dataset('iris')


pairplot = sns.pairplot(iris, hue='species', diag_kind='kde')
pairplot.fig.suptitle('Pairplot Iris - Specii', y=1.02, fontweight='bold')
plt.savefig('iris_pairplot.png', dpi=150, bbox_inches='tight')
plt.show()


fig, axes = plt.subplots(1, 4, figsize=(16, 4))
fig.suptitle('Violinplot - Variabile Iris', fontweight='bold', fontsize=14)


variabile = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width']
titluri = ['Lungime Sepală', 'Lățime Sepală', 'Lungime Petală', 'Lățime Petală']


for i, (var, titlu) in enumerate(zip(variabile, titluri)):
    sns.violinplot(data=iris, x='species', y=var, ax=axes[i])
    axes[i].set_title(titlu)
    axes[i].set_xlabel('')
    axes[i].tick_params(axis='x', rotation=45)

plt.tight_layout()
plt.savefig('iris_violinplots.png', dpi=150, bbox_inches='tight')
plt.show()

print("✅ Ambele figuri au fost salvate!")