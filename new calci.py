

print("Enter your choices of mathematical operation to perform:")
print("1. Addition")
print("2. subraction")
print("3.Division")
print("4.multiplication")

opt = input("Enter choice(1/2/3/4): ")

x = float(input("Enter first number: "))
y = float(input("Enter second number: "))

#def calculate(x,y):


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


#calculate(x,y)


def again():


    calc_again = input('''
Do you want to calculate again?
Please type Y for YES or N for NO.
''')

    if calc_again == 'Y':
        calculate()


    elif calc_again == 'N':
        print('See you later.')
again()