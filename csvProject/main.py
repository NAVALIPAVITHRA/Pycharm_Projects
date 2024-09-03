import csv
with open("data.csv") as file :
 data = csv.reader(file)
 temp = []
 for row in data:
    if row[1] != "temp" :
        temp.append(int(row[1]))
print(temp)
