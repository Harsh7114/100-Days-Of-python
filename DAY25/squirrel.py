import pandas

data = pandas.read_csv("2018squirrel.csv")
#print(data["Primary Fur Color"])
gray_squirrel_count = len(data[data["Primary Fur Color"]=='Gray'])
print(gray_squirrel_count)
black_squirrel_count = len(data[data["Primary Fur Color"]=='Black'])
print(black_squirrel_count)
red_squirrel_count = len(data[data["Primary Fur Color"]=='Cinnamon'])
print(red_squirrel_count)

data_dict ={
    "fur color":["Gray","Black","Cinnamon"],
    "scores":[gray_squirrel_count,black_squirrel_count,red_squirrel_count]
}

datat = pandas.DataFrame(data_dict)
print(datat)
datat.to_csv("new_squirrel_count.csv")