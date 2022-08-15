import csv
from datetime import datetime
import datetime

with open('data/original.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    writer = csv.writer(open('data/result.csv', 'w', newline=''))
    nw = datetime.datetime.today() + datetime.timedelta(days=2 , hours=5 , minutes=72 , seconds=130)
    writer.writerow(["start_time","end_time","days","hours","minutes","seconds","participants","name"])
    next(csv_reader,None)
    for date in csv_reader:
        date[0] = datetime.datetime.today()
        date[1] = nw.strftime("%Y-%m-%d %H:%M:%S , %d , %H , %M , %S")
        writer.writerow(date)