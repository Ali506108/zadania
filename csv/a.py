import pymongo
import csv 
import json 
import psycopg2
from config import host, user, password, db_name , port

db_client = pymongo.MongoClient("mongodb://localhost:27017")

with open('date/result.csv') as f:
    reader = csv.DictReader(f)
    rows = list(reader)

with open('result.json' , 'w') as f:
    json.dump(rows, f)
    for i in rows:
        print(i)
        
        current_db = db_client["pyMongo"]
        collection = current_db["csvs"]
        pyloungn = i
        ins_result = collection.insert_one(pyloungn)
        print(ins_result.inserted_id)



try:
    connection = psycopg2.connect(
        host=host,
        user=user,
        password=password,
        database=db_name, 
        port=port
    )
    connection.autocommit = True
    
    
    #with connection.cursor() as cursor:
        #cursor.execute(
        #    "CREATE table khans(name varchar,country varchar,board int)"
        #)
        #print("[INFO] Table created succsfely")
        
    #with connection.cursor() as cursor:
    #    a = ['Batu','Mode','Mengu-Temir','Az Janibek','Urus']
    #    #d = ['Ju-van','Shayu','Khan','Ulug-khan','khan']
    #    s = [1227,209,1266,1342,1373]
    #    for i in a:
    #        cursor.execute(
    #        f"INSERT INTO khans(name,country,board) VALUES ('{i}', 'JU-VAN','209')"
    #        )
                        
    #    print("[INFO] Data was succesfuly inserted")
    

    #with connection.cursor() as cursor:
    #    cursor.execute(
    #    " UPDATE khans SET country = 'ulug-ulus'")
    #    print("[INFO] Table")

    #with connection.cursor() as cursor:
    #        cursor.execute(
    #        "  DROP TABLE ulus"
    #        )
    #        print("[INFO] delelte Table")
except Exception as _ex:
    print("[INFO] Error while working with PostgreSQL", _ex)
finally:
    if connection:
        connection.close()
        print("[INFO] PostgreSQL connection closed")




















