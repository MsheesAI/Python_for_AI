#list:Ordered editable
#tuple:Ordered,Fixed
#Set:unique,unordered
#dict:key-value pairs

#list

names = ["shees","shafayee","shaoib","akram","qasim"]
names[0] = "unknown"
names.append("shees")
names.insert(1,"s")
names.remove("s")
names.pop()
names.sort()
print(names)

#for loop

for name in names:
    print(name)

#tuple
print("+____________TUPLE____________+")
print(' ')
colors = ("red","green","blue")
print(colors[2])
print(colors.count("red"))
print(colors.index("red"))


#set

print("+_____________SET_____________")
print(" ")
my_set = {1,2,3,4,4}
print(my_set)

#DICT
print("+_____________DICT_____________")
print(" ")

student = {
    "name":"shees",
    "age":"14",
    "courses":"piaic"
}
print(student["name"])
print(student.get("age"))

for key,value in student.items():
    print(key,":",value)