class profile():

    def __init__(self,fn,ln):
        self.fn= fn
        self.ln=ln

    def email(self):
        print("your generated email id is: {}.{} @gmail.com".format(self.fn,self.ln))

obj = profile("jana","prasanna")
obj2= profile("danny","dann")

obj.email()
obj2.email()