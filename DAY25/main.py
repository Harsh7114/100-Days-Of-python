# with open("./2. weather_data.csv",mode='r') as file:
#     row = file.readlines()
#     print(row)

import csv
import pandas

# with open("2. weather_data.csv") as file:
#     data=csv.reader(file)
#     next(data)  # skip header row
#     temperature =[]
#     for row in data:
#         temperature.append(int(row[1]))
#     print(temperature)

data = pandas.read_csv("2. weather_data.csv")
# print(data)
temp = data["temp"]
print(temp)
temp_list = temp.to_list()
print(temp_list)
print(len(temp_list))
### MY CODE TO TRY TO FIND AVERAGE OF TEMP
total = 0
for temp in temp_list:
    total += temp
avg = total / len(temp_list)
print(avg)
#angela
avg=sum(temp_list)/len(temp_list)
print(avg)
#m2
print(data["temp"].mean())
#max temp
print(data["temp"].max())

#get data in column
print(data["condition"])
#or using attribute
print(data.condition)

# to get data from row
print(data[data.day == "Monday"])
# which row has highest temp
print(data[data.temp==data.temp.max()])

monday = data[data.day == 'Monday']
c=(monday.temp)
f = (c * 1.8) + 32
print(f)

#create a dataframe
data_dict ={
    "students":["harsh","mary","com"],
    "scores":[75,6,99]
}
data=pandas.DataFrame(data_dict)
print(data)
data.to_csv("newdata.csv")