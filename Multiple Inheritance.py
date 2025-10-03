# Can be inherite multiple classes
class Father:
    def skill(self):
        print("Father: I can drive")

class Mother:
    def skill(self):
        print("Mother: I can cook")

class Mother2:
    def skill(self):
        print("Mother: I can cook")
class Child(Father, Mother, Mother2):   # Inherits from all
    pass

child = Child()
child.skill()  # Output: Father: I can drive
               # (because of Method Resolution Order
               # - left to right)
