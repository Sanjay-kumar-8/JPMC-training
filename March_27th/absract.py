from abc import ABC, abstractclassmethod

class Fruit:

    @abstractclassmethod   #annotation for declaring a class as a Abstract class
    
    
    def getColor(self):
        pass
    def getPrice(self):
        pass
class Demo(Fruit):
    
    def getPrice(self):
        print("Price is 150")
    def getColor(self):
        print("Color is red")

f=Demo()
f.getColor()
f.getPrice()
