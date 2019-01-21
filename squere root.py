

print("This is program who count squere root with complex number")
a = int(input("Give me a: "))
b = int(input("Give me b: "))
c = int(input("Give me c: "))

delta = (b**2 - (4*a*c))
re = b/(2*a)
im = ((-delta)/(2*a))

if delta < 0:
    print("This is a complex number: ","Your RE is: ",re,"Your IM is: ",im)
elif delta == 0:
    print("Delta is 0 ")
elif delta > 0:
    print("Your delta is: ", delta)

user = input("Do you wanna count a vertices of the parabola y/n ")

p = -b/(2*a)
q = -delta/(4*a)

if user == "y":
    print("p is: ", p, "q is: ",q)
elif user == "n":
    exit()



