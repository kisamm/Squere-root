
import math

print("This is program who count squere root with complex number")
a = int(input("Give me a: "))
b = int(input("Give me b: "))
c = int(input("Give me c: "))

delta = (b**2 - (4*a*c))
re = b/(2*a)
im = ((-delta)/(2*a))
squere = math.sqrt(delta)

if delta < 0:
    print("This is a complex number: ","Your RE is: ",re,"Your IM is: ",im)
elif delta == 0:
    print("Delta is 0 ")
elif delta > 0:
    print("Your delta is: ", delta, "your squere is: ", round(squere,3))

user = input("Do you wanna count a vertices of the parabola y/n ")

p = -b - (2*a)
q = -delta/(4*a)

if user == "y":
    print("p is: ", p, "q is: ",q)
elif user == "n":
    exit()

user2 = input("Do you wanna count the x1 and x2? y/n")


x1 = -b + math.sqrt(delta)/(2*a)
x2 = -b - math.sqrt(delta)/(2*a)

if user2 == "y":
    print("x1 is: ", round(x1,2), "x2 is: ", round(x2,2))
if user2 =="n":
    exit()

