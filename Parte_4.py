import requests

def descargar_y_guardar_csv(url, nombre_archivo):
    response = requests.get(url)
    
    if response.status_code == 200:
        
        with open(nombre_archivo, 'w', encoding='utf-8') as file:
            file.write(response.text)
        print(f"Datos descargados exitosamente y guardados en {nombre_archivo}")
    else:
        print(f"Error al descargar los datos. Código de estado: {response.status_code}")

url_datos = "https://huggingface.co/datasets/mstz/heart_failure/raw/main/heart_failure_clinical_records_dataset.csv"

descargar_y_guardar_csv(url_datos, "datos_descargados.csv")
