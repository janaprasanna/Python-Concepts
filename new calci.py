print("Enter your choices of mathematical operation to perform:")
print("1. Addition")
print("2. subraction")
print("3.Division")
print("4.multiplication")

opt = input("Enter choice(1/2/3/4): ")

x = float(input("Enter first number: "))
y = float(input("Enter second number: "))


def add(x,y):
    return x+y

def sub(x,y):
    return x-y

def div(x,y):
    return x/y

def mul(x,y):
    return x*y

if opt == '1':
   print(x,"+",y,"=", add(x,y))

elif opt == '2':
   print(x,"-",y,"=", sub(x,y))

elif opt == '3':
   print(x,"*",y,"=", div(x,y))

elif opt == '4':
   print(x,"/",y,"=", mul(x,y))
else:
   print("Invalid input")

op = True
while op:
    print("Do you want to  continue using calculator??")

    cont = str(input("choose (y) for yes and (n) for no:"))
    if cont == 'y' or cont == 'YES' or cont == "yes" or cont == "Yes":
        opt = input("Enter choice(1/2/3/4): ")

        x = float(input("Enter first number: "))
        y = float(input("Enter second number: "))

        if opt == '1':
            print(x, "+", y, "=", add(x, y))

        elif opt == '2':
            print(x, "-", y, "=", sub(x, y))

        elif opt == '3':
            print(x, "*", y, "=", div(x, y))

        elif opt == '4':
            print(x, "/", y, "=", mul(x, y))
        else:
            print("Invalid input")
    elif cont == 'n':
        op = False
        print("Goodbye")
    else:
        print("Invalid operation")


