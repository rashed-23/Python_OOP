# Create neccessary methods required later are created as abstract

from abc import ABC, abstractmethod  # Must include it because it is the build in class need to be parent class

class food(ABC):
    @abstractmethod
    def test(self):
        pass

class pizza:
    def test(self): # Must presented because it has been abstracted before
        print("Pizza is Yammi")
    def size(self):
        print("Size of Pizza is 12 inch")


p=pizza();

p.test()
p.size()