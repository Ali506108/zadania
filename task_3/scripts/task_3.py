import csv
from datetime import datetime
from datetime import date



with open('data/original.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    writer = csv.writer(open('data/result.csv', 'w', newline=''))
    writer.writerow(["start_time","end_time","days","hours","minutes","seconds","participants","name"])
    next(csv_reader,None)
    for data in csv_reader:

        da = f'{data[0]}'
        dat = f'{data[1]}'

        date_time_obj = datetime.strptime(da, '%Y-%m-%d %H:%M:%S')
        date_time_obe  = datetime.strptime(dat, '%Y-%m-%d %H:%M:%S')
        das  = date_time_obe - date_time_obj
        iq = das
        data[1] = datetime.strftime(date_time_obe , f"%Y-%m-%d %H:%M:%S , {iq}") 
       
        writer.writerow(data)
