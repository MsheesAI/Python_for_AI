#Module is a file containing Large Python code. WE can import and reuse them module like math random and os


#importing math library
import math
from math import sqrt

#importing myownmodule
import mymodule
from mymodule import greet

#square root
print(math.sqrt(16))
print(sqrt(16))

#greet
mymodule.greet("shees")
greet("shees")