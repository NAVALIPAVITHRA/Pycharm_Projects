import pandas#imported pandas library
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20240831.csv")#reads the csv file
grey_squirells = len(data[data["Primary Fur Color"] == "Gray"])#counts the len of gray
red_squirells = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirells = len(data[data["Primary Fur Color"] == "Black"])


print(grey_squirells)
print(black_squirells)
print(red_squirells)
#data dict to create the seperate csv file
data_dict = {
    "fur color": ["gray","red","blsck"],
    "count" : [grey_squirells,black_squirells,red_squirells]
}
#dataframe is created(rows and collumns)
df = pandas.DataFrame(data_dict)
df.to_csv("squirell_count.csv")#creates the csv file