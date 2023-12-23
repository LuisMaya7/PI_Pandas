import pandas as pd
from datasets import load_dataset

dataset = load_dataset("mstz/heart_failure")
data = dataset["train"]

df = pd.DataFrame(data)

df_fallecidos = df[df['is_dead'] == 1]
df_sobrevivientes = df[df['is_dead'] == 0]

promedio_edad_fallecidos = df_fallecidos['age'].mean()
promedio_edad_sobrevivientes = df_sobrevivientes['age'].mean()

print("Promedio de edad de personas que fallecieron:", promedio_edad_fallecidos)
print("Promedio de edad de personas que sobrevivieron:", promedio_edad_sobrevivientes)




