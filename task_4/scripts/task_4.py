import csv 


allColums = []
for csvfile in ("data/february.csv", "data/january.csv", "data/march.csv"):
    with open(csvfile, newline="") as files:
        csv_reader = csv.reader(files, delimiter=',')
        next(csv_reader,None)
        allColums+=csv_reader

allRows = zip(*allColums)
print(allRows)
with open('data/result.csv', 'w',newline='' ) as resultFile:
  writer = csv.writer(resultFile, delimiter=',' )
  writer.writerow(["date","city","value"])

  for row in allRows:
    #print(row)
    writer.writerow(row)
