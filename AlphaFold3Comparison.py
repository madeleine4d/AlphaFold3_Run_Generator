import pandas as pd
import json

seqs = pd.read_csv('Seqs.csv')
jobs = []
print ('this is the data file you have imported:')
print (seqs)
for i in list(seqs.index.values):
    job = {
    "name": seqs.at[i, 'name'],
    "modelSeeds": [],  
    "sequences": [
      {"growthFactor": {'sequence': seqs.at[i, 'gf'], 'count': 2}},
      {"affibody": {'sequence': seqs.at[i, 'aff'], 'count': 1}},
    ],
    }
    jobs.append(job)

with open('jobs.json', 'w') as outfile:
    json.dump(jobs, outfile)