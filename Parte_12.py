import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix, accuracy_score, f1_score

# Cargar datos desde el archivo CSV
df = pd.read_csv("datos_preparados.csv")

# Eliminar la columna 'edad_categorizada'
df = df.drop(columns=['edad_categorizada'])

# Separar características (X) y la columna objetivo (y)
X = df.drop(columns=['DEATH_EVENT'])
y = df['DEATH_EVENT']

# Realizar la partición estratificada del conjunto de datos
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, stratify=y, random_state=42)

# Inicializar y ajustar el modelo de Random Forest
model_rf = RandomForestClassifier(n_estimators=100, max_depth=5, random_state=42)  # Puedes ajustar los parámetros según sea necesario
model_rf.fit(X_train, y_train)

# Realizar predicciones en el conjunto de prueba
y_pred_rf = model_rf.predict(X_test)

# Calcular la matriz de confusión
conf_matrix_rf = confusion_matrix(y_test, y_pred_rf)
print("Matriz de Confusión:")
print(conf_matrix_rf)

# Calcular la precisión y F1-Score
accuracy_rf = accuracy_score(y_test, y_pred_rf)
f1_rf = f1_score(y_test, y_pred_rf)

print(f"Precisión del modelo (Random Forest): {accuracy_rf}")
print(f"F1-Score del modelo (Random Forest): {f1_rf}")

