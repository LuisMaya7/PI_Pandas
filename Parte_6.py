import sys
import requests
import pandas as pd

def descargar_datos(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        print(f"Error al descargar los datos. Código de estado: {response.status_code}")
        sys.exit(1)

def cargar_dataframe(datos_csv):
    return pd.read_csv(pd.compat.StringIO(datos_csv))

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

    return dataframe

def exportar_csv(dataframe, nombre_archivo):
    dataframe.to_csv(nombre_archivo, index=False)
    print(f"Datos limpios y preparados exportados como '{nombre_archivo}'.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python script.py <URL>")
        sys.exit(1)

    url = sys.argv[1]

    datos_csv = descargar_datos(url)

    df = cargar_dataframe(datos_csv)

    df = limpiar_y_preparar_datos(df)

    exportar_csv(df, "datos_preparados.csv")

