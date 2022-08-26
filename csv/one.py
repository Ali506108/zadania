import csv
import pymongo
import json 

db_client = pymongo.MongoClient("mongodb://localhost:27017")

with open('date/origin.csv' ) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    writer = csv.writer(open('result.json', 'w', newline=''))
    writer.writerow(["year", "region", "value"])
    next(csv_reader,None)
    for row in csv_reader:  
        writer.writerow((row[0]+"-01-01",row[1],row[2]))
