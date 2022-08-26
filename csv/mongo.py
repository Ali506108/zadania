import csv
import json
with open('date/result.csv') as f:
    reader = csv.DictReader(f)
    rows = list(reader)

with open('result.json' , 'w') as f:
    json.dump(rows, f)