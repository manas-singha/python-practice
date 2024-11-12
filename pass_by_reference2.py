class Customer:
    def __init__(self,name):
        self.name=name
def greet(customer):
    print(id(customer))
    customer.name="Nitish"
    print(customer.name)
    print(id(customer))
        
cust=Customer("Ankita")
print(id(cust))
greet(cust)
print(cust.name)
