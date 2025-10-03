# Using the property of another class
class phone:  # Parent Class/ Base Class/ Super Class
    def price(self):
        print(20000)
    def os(self):
        print("Android")
class samsung(phone): # Sub Class/ Child Class/ Derived Class
    pass

mobail=samsung()
mobail.price()
mobail.os()
