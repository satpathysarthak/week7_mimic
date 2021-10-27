import numpy as np
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
%matplotlib inline
import hdbscan


df = pd.read_csv('df.csv')

import umap.umap_ as umap
reducer = umap.UMAP()

df_data = df[
    [
        #'51066',
        '51067',
        '51077',
        '51078',
        #'51081',
        '51088',
        '51095',
        '51097',
        '51109',
    ]
].values
scaled_df_data = StandardScaler().fit_transform(df_data)
embedding = reducer.fit_transform(scaled_df_data)
#embedding.shape

#scatterplot 
plt.scatter(
    embedding[:, 0],
    embedding[:, 1])#,
    #c=[sns.color_palette()[x] for x in penguins.species_short.map({"Adelie":0, "Chinstrap":1, "Gentoo":2})])
plt.gca().set_aspect('equal', 'datalim')
plt.title('UMAP projection of the dataset', fontsize=24)


clusterable_embedding = umap.UMAP(
    n_neighbors=3,
    min_dist=0.0,
    n_components=4,
    random_state=3,
).fit_transform(scaled_df_data)
clusterable_embedding[:, 1]

labels = hdbscan.HDBSCAN(
    min_samples=3,
    min_cluster_size=20,
).fit_predict(clusterable_embedding)
labels

clustered = (labels >= 0)
plt.scatter(clusterable_embedding[~clustered, 0],
            clusterable_embedding[~clustered, 1],
            color=(0.5, 0.5, 0.5),
            s=10,
            alpha=0.5)
plt.scatter(clusterable_embedding[clustered, 0],
            clusterable_embedding[clustered, 1],
            c=labels[clustered],
            s=10,
            cmap='Spectral');

