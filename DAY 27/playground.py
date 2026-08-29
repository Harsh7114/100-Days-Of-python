def add (*args):
    sum =0
    for i in args:
        sum +=i
    return sum
print(add(0,98))

def calculate(n,**kwargs):
    print(kwargs)
    # for key ,value in kwargs.items():
    #     print(key)
    #     print(value)
    #print(kwargs["add"])
    n+=kwargs["add"]
    n*=kwargs["multiply"]
    print(n)


calculate(2,add=3 , multiply =5)

class Car:
    def __init__(self,**kw):
        self.make = kw["make"]
        self.model = kw["model"]
        self.seed = kw.get("speed") #.get will work same as [] but will not give error when not provided argument unlike []

mycar = Car(make= "nissan",model="gtr")
print(mycar.make)
mycar2= Car(make = "hero",model="bbb",speed="33mph")
print(mycar2.seed)
