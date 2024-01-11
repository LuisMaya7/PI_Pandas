import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("datos_preparados.csv")

fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(12, 10))

anemia_counts = df['anaemia'].value_counts()
axes[0, 0].pie(anemia_counts, labels=anemia_counts.index, autopct='%1.1f%%', startangle=90, colors=['skyblue', 'lightcoral'])
axes[0, 0].set_title('Distribución de Anémicos')

diabetes_counts = df['diabetes'].value_counts()
axes[0, 1].pie(diabetes_counts, labels=diabetes_counts.index, autopct='%1.1f%%', startangle=90, colors=['lightgreen', 'lightcoral'])
axes[0, 1].set_title('Distribución de Diabéticos')

smoking_counts = df['smoking'].value_counts()
axes[1, 0].pie(smoking_counts, labels=smoking_counts.index, autopct='%1.1f%%', startangle=90, colors=['lightgreen', 'lightcoral'])
axes[1, 0].set_title('Distribución de Fumadores')

death_counts = df['DEATH_EVENT'].value_counts()
axes[1, 1].pie(death_counts, labels=death_counts.index, autopct='%1.1f%%', startangle=90, colors=['lightcoral', 'lightgreen'])
axes[1, 1].set_title('Distribución de Muertos')

plt.tight_layout()
plt.show()
