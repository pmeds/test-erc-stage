import pandas as pd
import hashlib
import csv
import re
# Master file with all the rules
filename = "rules.xlsx"
print(filename)
# header for the CSV files
header = ['hash', 'source', 'destination']
# False check to only write the header row once
header_added = False
# Read spreadsheet, openpyxl is required for old versions of python
df = pd.read_excel(filename, engine='openpyxl')
# Iterate through the rows of the spreadsheet and extract the enxt data:
# source is the incoming URL
# source_hash is the hash of the incoming URL and the key for EKV
# destination is the redirect URL
# ekvitem has the value of the variables to be written to the respective upload.csv
for index, row in df.iterrows():
    source_data = row['source']
    source_hash = hashlib.sha256(source_data.encode('utf-8')).hexdigest()
    destination = row['destination']
    ekvitem = [source_hash, source_data, destination]
# Check if source_data contains any of the paths that belong to the games namespace
# Creates the respective upload csvs for ekvuploader
    if re.search(r'games|editorial|ps4-games|ps-vr-games|ps-plus', source_data):
        with open('games-upload.csv', 'a') as gamesw:
            writerg = csv.writer(gamesw, lineterminator='\n')
            if not header_added:
                writerg.writerow(header)
                print(header)
                header_added = True
            print(ekvitem)
            writerg.writerows([ekvitem])
    elif re.search(r'support|soporte', source_data):
        with open('support-upload.csv', 'a') as supportw:
            writers = csv.writer(supportw, lineterminator='\n')
            if not header_added:
                writers.writerow(header)
                header_added = True
            writers.writerows([ekvitem])
    else:
        with open('general-upload.csv', 'a') as generalw:
            writer = csv.writer(generalw, lineterminator='\n')
            if not header_added:
                writer.writerow(header)
                header_added = True
            writer.writerows([ekvitem])




