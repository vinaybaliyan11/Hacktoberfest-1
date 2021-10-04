import random
passlen = int(input("enter the lenght of password"))
a="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz01234567890!@#$%^&*()?"
b = "".join(random.sample(a,passlen))
print(b)
