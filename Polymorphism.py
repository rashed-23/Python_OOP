#Different Objects but same parameters
#Example 01
# class object:
#     def __init__(self,Brand,Price):
#         self.Brand=Brand
#         self.Price=Price
# class car(object):
#     pass
# class phone(object):
#     pass
#
# C=car("BMW",2000000)
# P=phone("Samsung",30000)
#
# print(C.Brand)
# print(P.Brand)

#----------------------------------------------------------

#Example 02

class adder:
    def __init__(self,a=0,b=0,c=0,d=0):
        self.sum=a+b+c+d


class add(adder):
    def __init__(self,a,b,c,d,e=0): # Can be add more parameters
        super().__init__(a,b,c,d)
        self.sum+=e

sum2=add(2,3,4,5)
print(sum2.sum)
sum3=adder(1,2,3)
print(sum3.sum)





