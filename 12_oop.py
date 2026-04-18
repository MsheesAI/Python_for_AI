#class:A class is a blueprint (template) for creating objects. Define attributes data and methods.

#Object:an object is a real instance of a class

#Basic class and object

#class
class Car:
    def __init__(self,company,ownership):
        self.company = company
        self.ownership = ownership

    def engine(self,engine="turbo v7"):
        print(f"owner is {self.ownership} and car engine is {engine}")

#object
mycar=Car("noddles","sheikh muhammad shees shoaib")
mycar.engine("turbo v9")

my_brother_car=Car("loyal cars","sheikh muhammad shafayee shoaib")
my_brother_car.engine("loyal 1b")

#Accessing Objects attribute

class Student:
    def __init__(self,name,age,grade):
        self.name = name
        self.age = age
        self.grade = grade
    def info(self):
        print(f"student name : {self.name}")
        print(f"student age : {self.age}")
        print(f"student grade : {self.grade}")
        
    def is_eligible(self):
        if self.age>=15:
            print(self.name , "is eligible")
        else:
            print(self.name , "is not eligible")

#creating instance
student_1 = Student("Shees",14,"9th")
student_2 = Student("Shafayee",20,"12th")


#Accessing attributes
print(student_1.name)
print(student_2.age)

#calling methods

student_1.info()
student_1.is_eligible()

student_2.info()
student_2.is_eligible()

#Encapsulation

print("_________ENCAPSULATION_________")
print("                               \n")

class Person:
    def __init__(self,name,salary):
        self.name = name
        self.__salary = salary #private attribute
    def get_salary(self): #accessing private attribute
        return self.__salary

person_1 = Person("shees",1000000)
print(person_1.get_salary())


#Inheritance

print("_________INHERITANCE_________")
print("                               \n")

class Animal:
    @property
    def speak(self):
        print("some sound")
    
class Cat(Animal):
    def speak(self): #Method overriding
        print("Meow")

cat_1 = Cat()
cat_1.speak()

#Polymorphism

print("_________POLYMORPHISM_________")
print("                               \n")