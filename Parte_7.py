import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("datos_preparados.csv")

plt.figure(figsize=(8, 6))
plt.hist(df['edad_categorizada'], bins=5, color='skyblue', edgecolor='black', alpha=0.7)
plt.title('Distribución de Edades')
plt.xlabel('Edad Categorizada')
plt.ylabel('Frecuencia')
plt.show()


grupos = ['anaemia', 'diabetes', 'smoking', 'DEATH_EVENT']
nombres_grupos = ['Anémicos', 'Diabéticos', 'Fumadores', 'Muertos']

plt.figure(figsize=(12, 8))

for i, grupo in enumerate(grupos):
    plt.subplot(2, 2, i+1)
    hombres = df[df['sex'] == 1][grupo]
    mujeres = df[df['sex'] == 0][grupo]

    plt.bar(hombres.unique(), hombres.value_counts(), width=0.4, label='Hombres', align='edge', alpha=0.7)
    plt.bar(mujeres.unique(), mujeres.value_counts(), width=-0.4, label='Mujeres', align='edge', alpha=0.7)

    plt.title(f'Distribución de {nombres_grupos[i]} por Género')
    plt.xlabel(nombres_grupos[i])
    plt.ylabel('Frecuencia')
    plt.legend()

plt.tight_layout()
plt.show()
