import pandas
#data = pandas.read_csv("weather_data.csv.csv")
#data_temp = data["temp"]
#data_temp_list = data_temp.to_list()
#data_temp_average = sum(data_temp_list) / 7
#print(data[data.temp == data.temp.max()])

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
gray_color = len(data[data["Primary Fur Color"] == "Gray"])
cinnamon_color = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_color = len(data[data["Primary Fur Color"] == "Black"])

squirrel_color ={
    "Fur Color" : ["Gray", "Cinnamon", "Black"],
    "Count" : [gray_color, cinnamon_color, black_color]
}
df = pandas.DataFrame(squirrel_color)
df.to_csv("SquirrelCount.csv")
