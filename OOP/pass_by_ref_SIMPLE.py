class Customer:

    def __init__(self,name,gender):
        self.name = name
        self.gender = gender


def greet(customer):

    if customer.gender == "Male":
        print("Hello",customer.name,"sir")
    else:
        print("Hello",customer.name,"mam")

    cust2 = Customer("Prakrati","Female")

    return cust2



cust = Customer("Vishal","Male")

new_cust = greet(cust)

print(new_cust.name)
