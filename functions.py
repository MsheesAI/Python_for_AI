#Function: function is a reuseable block of code 

def greet(user):
    print("Hello",user)

greet("shees")

def add (a,b):
    return a + b
r = add(2,2)
print(r)

#lambda functions

add = lambda a,b : a+b
print(add(1,1))

double = lambda n:n*2
print(double(2))

nums = [1,2,3,4]
squares = list(map(lambda X:X*X,nums))
print(squares)

numbers = [1,2,3,4,5,6,7,8]
odd_numbers = list(filter(lambda x:x%2 !=0,numbers))
print(odd_numbers)