# Can be Access one directional classes
class Grandparent:
    def origin(self):
        print("I am the grandparent")

class Parent(Grandparent):
    def origin(self):
        print("I am the parent")

class Child(Parent):
    def origin(self):
        print("I am the child")

c = Child()
c.origin()       # Output: I am the child
