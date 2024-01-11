##Descargar "pip install pandas numpy scikit-learn plotly" 

import pandas as pd
import numpy as np
from sklearn.manifold import TSNE
import plotly.express as px

df = pd.read_csv("datos_preparados.csv")

X = df.drop(columns=['DEATH_EVENT', 'edad_categorizada']).values

y = df['DEATH_EVENT'].values

X_embedded = TSNE(
    n_components=3,
    learning_rate='auto',
    init='random',
    perplexity=3
).fit_transform(X)

df_tsne = pd.DataFrame({'Dimension_1': X_embedded[:, 0], 'Dimension_2': X_embedded[:, 1], 'Dimension_3': X_embedded[:, 2], 'DEATH_EVENT': y})

fig = px.scatter_3d(df_tsne, x='Dimension_1', y='Dimension_2', z='Dimension_3', color='DEATH_EVENT', opacity=0.7,
                    title='Visualización t-SNE de Datos de Fallo Cardíaco',
                    labels={'Dimension_1': 'Dimensión 1', 'Dimension_2': 'Dimensión 2', 'Dimension_3': 'Dimensión 3'},
                    color_discrete_map={0: 'blue', 1: 'red'})
fig.show()
