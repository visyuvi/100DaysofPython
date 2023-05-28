class Customer:

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def intro(self):
        print("I am",self.name,"and I am", self.age)


c1 = Customer("Vishal",31)

c2 = Customer("Praks",30)

c3 = Customer("Akshi",35)

c4 = Customer("neha",30)

S = {c1,c2,c3}

for i in S:
    i.intro()
