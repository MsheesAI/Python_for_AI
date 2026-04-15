for i in range(3):
    print("Outer lopp")
    for j in range(3):
       print("   Inner Loop")

print("____LOOPING OVER DATA STRUCTURES____")

for char in "Shanks":
    print(char)

count = 0

for char in "luffy":
    if char == "f":
        count +=1
print(count)

name = "zoro"
rev = ""
for char in name:
    rev = char+rev
print(rev)

student = {"name":"shees","age":20,"grade":"A"}

for key in student:
    print(key)
for key in student:
    print(student[key])