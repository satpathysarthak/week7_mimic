 
##############################################################
# Script: UMAP_cluster.py
# Author: Sarthak Satpathy
# Running the script: preferred to be run chunk wise on Jupyter
# input: a <filename>.csv file which has the queried dataset with info on Urine test values
# output Figures with UMAP and accuracy calculations
# Purpose: UMAP clustering and accuracy calculations, defining labels for AKI stage based on clustering
# the input paths can be relative to the working directory
# the output will be created in the working directory
################################################################
# library imports
import numpy as np
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
%matplotlib inline
import hdbscan

#reading the subset data
df = pd.read_csv('df.csv')

# Umap import
import umap.umap_ as umap
reducer = umap.UMAP()

# data stored as matrix
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


# creating labels
df_new = df[['SUBJECT_ID','51081','51109','51087']]
df_new['serum'] = df_new['51081']
df_new['urine'] = df_new['51109']/(df_new['51087']*87)

#baseline for Serum Creatinine
baseline = df_new['serum'].min()
#using conditionals on the Serum creatinine and urine level
df_new['class'] = 0
lab = np.array(df_new['class'])
ScR = np.array(df_new['serum'])
Ur = np.array(df_new['urine'])
for i in range(0,len(df_new)):
    if((ScR[i] > 1.5*baseline and ScR[i] < 2.0*baseline) or (Ur[i] > 1.0 or Ur[i] < 2.0)):
        lab[i] = 1
    if((ScR[i] > 2.0*baseline and ScR[i] < 2.9*baseline) or (Ur[i] > 0.3 or Ur[i] < 1.0)):
        lab[i] = 2
    if((ScR[i] > 3.0*baseline ) or (Ur[i] < 0.3 )):   
        lab[i] = 3
df_new['class'] = lab

#scatterplot with clusters labelled by the TRUE labels(set by condionals)
plt.scatter(clusterable_embedding[:, 0], clusterable_embedding[:, 1],
            c=lab, s=10, cmap='Spectral');


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

#scatterplot with clusters labelled by the UMAP algorithm
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
#calculating score
from sklearn.metrics import adjusted_rand_score, adjusted_mutual_info_score
adjusted_rand_score(lab, labels)
