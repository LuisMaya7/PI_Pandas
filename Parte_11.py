import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

df = pd.read_csv("datos_preparados.csv")

df = df.drop(columns=['edad_categorizada'])

plt.figure(figsize=(6, 4))
df['DEATH_EVENT'].value_counts().plot(kind='bar', color=['skyblue', 'lightcoral'])
plt.title('Distribución de Clases')
plt.xlabel('Clase (DEATH_EVENT)')
plt.ylabel('Frecuencia')
plt.xticks(rotation=0)
plt.show()

X = df.drop(columns=['DEATH_EVENT'])
y = df['DEATH_EVENT']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, stratify=y, random_state=42)

model = DecisionTreeClassifier(max_depth=3, random_state=42) 

y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
print(f"Precisión del modelo: {accuracy}")
