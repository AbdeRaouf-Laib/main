
#to take from you
def hello(name):
    print(f"hello {name}")
try:
    name = input("enter your name: ")
except:
    print("Error!!")
print("hai,")
hello(name)
#to give you
def give():
    age = int(input("enter your age: "))
    return age
resultat = give()
print("Date of birth is: ")
print( 2023 - resultat)