import csv

allColumns = []
for dataFileName in [ 'data/february.csv', 'data/january.csv', 'data/march.csv' ]:
  with open(dataFileName) as dataFile:
    fileColumns = zip(*list(csv.reader(dataFile, delimiter=' ')))
    allColumns += fileColumns

allRows = zip(*allColumns)

with open('data/result.csv', 'w' ) as resultFile:
  writer = csv.writer(resultFile, delimiter=' ' )
  for row in allRows:
    print(row[0])
    writer.writerow(row)



