import pandas as pd

def limpiar_y_preparar_datos(dataframe):
    if dataframe.isnull().any().any():
        dataframe = dataframe.dropna()
        print("Se eliminaron las filas con valores faltantes.")

    if dataframe.duplicated().any():
        dataframe = dataframe.drop_duplicates()
        print("Se eliminaron las filas duplicadas.")

    dataframe = dataframe[(dataframe['age'] >= 10) & (dataframe['age'] <= 100)]
    print("Se eliminaron los valores atípicos en la columna 'age'.")

    bins = [0, 12, 19, 39, 59, float('inf')]
    labels = ['Niño', 'Adolescente', 'Joven Adulto', 'Adulto', 'Adulto Mayor']
    dataframe['edad_categorizada'] = pd.cut(dataframe['age'], bins=bins, labels=labels)

    dataframe.to_csv("datos_preparados.csv", index=False)
    print("Datos limpiados y preparados guardados como 'datos_preparados.csv'.")

df = pd.read_csv("datos_descargados.csv")

limpiar_y_preparar_datos(df)
