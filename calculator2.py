class calci():

    def __init__(self, n1, n2):
        self.n1 = n1
        self.n2 = n2

    def addition(self):
        add = self.n1 + self.n2
        print("the sum of the two numbers is:", add)

    def subraction(self):
        sub = self.n1 - self.n2
        print("the difference  of the two numbers is :", sub)

    def multiplication(self):
        mul = self.n1 * self.n2
        print("the multiplication of the two numbers is:", mul)

    def division(self):
        div = self.n1 / self.n2
        print("the division of the two numbers is:", div)


obj1 = calci(1,2)
obj1.addition()
obj1.subraction()
obj1.multiplication()
obj1.division()