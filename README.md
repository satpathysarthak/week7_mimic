# BMI500_Satpathy_SQL_UMAP

This repository contains the code for Homework assignment for BMI-500 course: Week 7.  The aim of the project was to query urine indicators like serum creatinine and output to run an unsupervised clustering algorithm on a choice of publically available dataset. 

## Dataset

MIMIC datset was procured from physionet.org with credentialed access. The data was hosted on the BMI clusters after approval from MIMIC team.

## Installation:

```install
https://github.com/satpathysarthak/week7_mimic.git
```

### Requirements


This can be done either directly in the cloned repository or by setting up an [Anaconda](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html) or Python [virtualenv](https://virtualenv.pypa.io/en/stable/user_guide.html) environment

### Files and Directories
`createdb.py`: Script that creates the database using the .csv files provided by the MIMIC data providers.

`sqlquery.py`: Scripts with Sqlite commands to query a reference and a clustering dataset. 

`UMAP_cluster.py`: Scripts with commands for AKI classification based on conditionals, UMAP clustering and Accuracy claculation.
`TRUE_labels.png` : Labeling or coloring the datasets based on labels defined for stages 1,2,3 of AKI
`UMAP_labels.png` : Labeling or coloring the datasets based on labels obtained from UMAP clustering
