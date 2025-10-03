# Using the property of another class
class phone:
    def __init__(self):
        print("I am in Super Class")
class samsung(phone):
    def __init__(self):
        #super().__init__()
        print("I am in Sub Class")

mobail=samsung()

