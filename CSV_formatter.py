import pandas as pd
import json
import hashlib
import csv
filename = "rules.xlsx"
print(filename)

df = pd.read_excel(filename)
header = ['hash', 'source', 'destination']
with open('upload.csv', 'w', newline='') as w:
    writer = csv.writer(w)
    writer.writerow(header)
    for index, row in df.iterrows():
        source_data = row['source']
        source_hash = hashlib.sha256(source_data.encode('utf-8')).hexdigest()
        destination = row['destination']
        ekvitem = [source_hash, source_data, destination]
        print("writing to ekv_update.json")
        writer.writerow(ekvitem)




