try:
    file = open("mytrext.txt")
    a_dict = {"key":"value"}
    print(a_dict["key"])
except FileNotFoundError:
    file = open("mytrext.txt",'w')
    file.write("Something")
else:
    content = file.read()
    print(content)
finally:
    file.close()
    print("file is closed")
raise TypeError
