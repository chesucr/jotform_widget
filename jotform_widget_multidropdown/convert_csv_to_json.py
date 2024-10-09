import pandas as pd
import pdb
import json

df = pd.read_csv('confrarias.csv', encoding='utf-8')

df = df.drop(columns=['lat', 'lon'])

dic = {}
for index, row in df.iterrows():
    if row.provincia not in dic:
        dic[row.provincia] = {}
    if row.confraria not in dic[row.provincia]:
        dic[row.provincia][row.confraria] = []
    dic[row.provincia][row.confraria].append(row.banco)

# pdb.set_trace()

with open('output.json', 'w') as json_file:
    json.dump(dic, json_file, indent=4)

# json_data = df.to_json('output.json')

