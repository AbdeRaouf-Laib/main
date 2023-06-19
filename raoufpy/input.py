#for one function
from cs50 import get_string
#for all function
from cs50 import *
#for import onli lib
import cs50
name = get_string("enter your name: ")
print(f"hello { name}")
answer = cs50.get_string("enter your name: ")
print(f"hello { answer}")
x = get_int("enter your age: ")
y = get_int("enter your date of borne: ")
print(f"the date is: {y + x}")
#his cs50 library
inp = input("enter your name: ")
print(f"hello {inp}")
a = float(input("enter your tall: "))
b = int(input("enter your weight: "))
print(f"hello { answer } { name } your weight is: { b } and your tall is: { a } ")