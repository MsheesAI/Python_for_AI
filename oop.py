#class:A class is a blueprint (template) for creating objects. Define attributes data and methods.

#Object:an object is a real instance of a class

class Car:
    def __init__(self,company,ownership):
        self.company = company
        self.ownership = ownership

    def engine(self,engine="turbo v7"):
        print(f"owner is {self.ownership} and car engine is {engine}")

mycar=Car("noddles","sheikh muhammad shees shoaib")
mycar.engine("turbo v9")

my_brother_car=Car("loyal cars","sheikh muhammad shafayee shoaib")
my_brother_car.engine("loyal 1b")