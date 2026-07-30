def check_prime(a):
    res=True
    for i in range (2,a):
        if a % i ==0 :
            res= False
    if res:
        print(" prime")
    else:
        print("it is not a prime")
a= int(input("enter the no:"))
res= check_prime(a)



