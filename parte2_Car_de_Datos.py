import pandas as pd
from datasets import load_dataset

dataset = load_dataset("mstz/heart_failure")
data = dataset["train"]

df = pd.DataFrame(data)

tipos_de_datos = df.dtypes
print("Tipos de datos en cada columna:")
print(tipos_de_datos)

resultados_fumadores = df.groupby(['is_male', 'is_smoker']).size().unstack().fillna(0)
resultados_fumadores.columns = ['No Fumadora', 'Fumadora']
resultados_fumadores.index = ['Mujer', 'Hombre']

print("\nCantidad de hombres fumadores vs mujeres fumadoras:")
print(resultados_fumadores)
