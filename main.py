with open("weather_data.csv", mode="r")as file:
    read = file.readlines()
    print(read)

import csv

with open("weather_data.csv", mode="r")as data:
    read = csv.reader(data)
    temperature = []
    for row in data:
        print(row)

import pandas
data= pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
print(data["Primary Fur Color","Highlight Fur Color,Combination of Primary and Highlight Color"])

data_to_dict = data.to_dict()
print(data_to_dict)

temp_list = data["temp"].to_list()
print(len(temp_list))

print(data["temp"].mean())
print(data["temp"].max())

print(data[data.temp == temp_list].max())

monday = data[data.day == "Monday"]
print(monday.condition)
#
# Fahrenheit = data[data.day == "Monday" ]
# print(Fahrenheit.temp)
