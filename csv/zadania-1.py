import csv
import pymongo
import json 
import psycopg2
from config import host, user, password, db_name , port


db_client = pymongo.MongoClient("mongodb://localhost:27017")

with open('date/result.csv') as f:
        reader = csv.DictReader(f)
        rows = list(reader)   
        print(rows)
with open('result.json' , 'w') as f:
    json.dump(rows, f)
    for i in rows:
        print(i)
        current_db = db_client["pyMongo"]
        collection = current_db["csvs"]
        pyloungn = i
        ins_result = collection.insert_one(pyloungn)
        print(ins_result.inserted_id)
        writer = csv.writer(open('result.json', 'w', newline=''))

with open('date/origin.csv' ) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    writer = csv.writer(open('out.csv', 'w', newline=''))
    writer.writerow(["year", "region", "value"])
    next(csv_reader,None)
    for row in csv_reader:  
        writer.writerow((row[0]+"-01-01",row[1],row[2]))
        
        try:
            connection = psycopg2.connect(
            host=host,
            user=user,
            password=password,
            database=db_name, 
            port=port
            )
            connection.autocommit = True
            with connection.cursor() as cursor:
                cursor.execute(
                f"INSERT INTO task1(year,region,value) VALUES ('{row[0]}-01-01','{row[1]}',{row[2]})"
                )
                print(row[2])
                print("[INFO] info is bd")
            #with connection.cursor() as cursor:
            #    cursor.execute(
            #    f"DELETE FROM task1 WHERE region='Almaty';"
            #    )  
            #    print("[INFO] row is delete")              

        except Exception as _ex:
            print("[INFO] Error while working with PostgreSQL", _ex)
        finally:
            if connection:
                connection.close()
                print("[INFO] PostgreSQL connection closed")