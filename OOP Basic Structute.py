class Student:   # Class definition
    # Constructor (special method called when object is created)
    def __init__(self, name, age, grade):
        self.name = name        # Attribute (instance variable)
        self.age = age          # Attribute
        self.grade = grade      # Attribute

    # Method (function inside a class)
    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Grade: {self.grade}")

    # Another Method
    def is_passed(self):
        return self.grade >= 50


# Creating an Object (Instance of class)
student1 = Student("Alice", 20, 85)

# Accessing Attributes
print(student1.name)   # Output: Alice

# Calling Methods
student1.display_info()   # Output: Name: Alice, Age: 20, Grade: 85
print(student1.is_passed())  # Output: True
