import pandas as pd
import sqlite3

#connect to a database
conn = sqlite3.connect("mimic.db")

# the query where Serum Creatinine and Urine output information is stored
sql_string = 'SELECT SUBJECT_ID, ITEMID, VALUENUM FROM labevents WHERE ITEMID = 51081 OR ITEMID = 51109'
df = pd.read_sql(sql_string, conn) # the sql query is assigned as a pandas dataframe
# df_ref stores the query and will be the dataframe on which we would give labels to the clusters based on AKI info
df_ref = df
df['TEST']= df['ITEMID'].map(str)
df_ref = df_ref.drop_duplicates(subset=['TEST', 'SUBJECT_ID'], keep='last') # removes duplicates
df_ref = df_ref.drop('ITEMID',1) # drpos the ITEMID which stored as integer
df_ref = df_ref.drop_duplicates() # check for overall duplicates
df_ref= df_ref.pivot(index='SUBJECT_ID', columns='TEST', values='VALUENUM')
df_ref.index.name = 'SUBJECT_ID' # inserts rownames as a column
df_ref.reset_index(inplace=True)
#df_ref #

# the query to get the training set 
sql_string = 'SELECT SUBJECT_ID, ITEMID, VALUE, VALUENUM, VALUEUOM FROM labevents WHERE ITEMID = 51081 OR ITEMID = 51109 OR ITEMID = 51066 OR ITEMID = 51067 OR ITEMID = 51077 OR ITEMID = 51078 OR ITEMID = 51087 OR ITEMID = 51088 OR ITEMID = 51095 OR ITEMID = 51097'
df = pd.read_sql(sql_string, conn)
df_cluster = df
df_cluster['TEST']= df_cluster['ITEMID'].map(str)
df_cluster = df_cluster.drop_duplicates(subset=['TEST', 'SUBJECT_ID'], keep='last')
df_cluster = df_cluster.drop('ITEMID',1)
df_cluster = df_cluster.drop_duplicates()
df_cluster= df_cluster.pivot(index='SUBJECT_ID', columns='TEST', values='VALUENUM')
df_cluster.index.name = 'SUBJECT_ID'
df_cluster.reset_index(inplace=True)
#df_cluster

# the merged dataset with necessary information will be used as it is 
df = df_cluster[df_cluster.SUBJECT_ID.isin(df_ref.SUBJECT_ID)]
df.to_csv('df.csv')
