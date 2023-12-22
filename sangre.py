from datasets import load_dataset
import numpy as np


dataset = load_dataset("mstz/heart_failure")

data = dataset["train"]

ages_list = data['age']

ages_array = np.array(ages_list)

average_age = np.mean(ages_array)

print("El promedio de edad de las personas participantes en el estudio es: {:.1f}".format(average_age))
