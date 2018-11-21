import csv
listes=[]
liste2019=[]
with open('datajoueurscsv2019.csv',newline='') as csvfile:
    reader=csv.reader(csvfile,delimiter=';')
    for row in reader:
        liste2019=liste2019+[row]
liste2019=liste2019[1:]
listes.append(liste2019)
liste2018=[]
with open('datajoueurscsv2018.csv',newline='') as csvfile:
    reader=csv.reader(csvfile,delimiter=';')
    for row in reader:
        liste2018=liste2018+[row]
liste2018=liste2018[1:]
listes.append(liste2018)
liste2017=[]
with open('datajoueurscsv2017.csv',newline='') as csvfile:
    reader=csv.reader(csvfile,delimiter=';')
    for row in reader:
        liste2017=liste2017+[row]
liste2017=liste2017[1:]
listes.append(liste2017)
liste2016=[]
with open('datajoueurscsv2016.csv',newline='') as csvfile:
    reader=csv.reader(csvfile,delimiter=';')
    for row in reader:
        liste2016=liste2016+[row]
liste2016=liste2016[1:]
listes.append(liste2016)
