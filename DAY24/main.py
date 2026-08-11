# with open("myfile.txt") as file:
#     contents = file.read()
#     print(contents)

with open("myfile.txt",mode='a') as file:
    file.write("\nNew Test/")
