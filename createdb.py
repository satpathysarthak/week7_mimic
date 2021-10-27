##############################################################
# Script: createdb.py
# Author: Sarthak Satpathy
# Running the script: python createdb.py
# input: CSV file paths mentioned the code for the tables to be added
# output a <filename>.db file which will be used for sql querying.
# Purpose: create a databse for the tables obtained from mimic csv files
# the input paths can be relative to the working directory
# the output will be created in the working directory
################################################################
import pandas as pd
import sqlite3
#connect to a database
conn = sqlite3.connect("mimic.db")
#read the CSV
df = pd.read_csv('./physionet.org/files/mimiciii/1.4/ADMISSIONS.csv')
#saves the csv as table admissions to the connection on the database mimic.db
df.to_sql('admissions', conn)
print('1')
df = pd.read_csv('./physionet.org/files/mimiciii/1.4/PATIENTS.csv')
df.to_sql('patients', conn)
print('2')
df = pd.read_csv('./physionet.org/files/mimiciii/1.4/DIAGNOSES_ICD.csv')
df.to_sql('diagnoses_icd', conn)
print('3')
df = pd.read_csv('./physionet.org/files/mimiciii/1.4/D_ICD_DIAGNOSES.csv')
df.to_sql('d_icd_diagnoses', conn)
print('4')
df = pd.read_csv('./physionet.org/files/mimiciii/1.4/LABEVENTS.csv')
df.to_sql('labevents', conn)
print('5')
df = pd.read_csv('./physionet.org/files/mimiciii/1.4/MICROBIOLOGYEVENTS.csv')
df.to_sql('microbiologyevents', conn)
print('6')
df = pd.read_csv('./physionet.org/files/mimiciii/1.4/D_LABITEMS.csv')
df.to_sql('d_labitems', conn)
print('7')
