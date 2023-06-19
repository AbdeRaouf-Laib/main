x = input("enter the text: ")
print("after: ",end= "")
for i in x:
    print(i.upper(),end = "")
print()
#
print(f"after: {x.lower()}")
print(f"after: {x.upper()}")
print(f"after: {x.capitalize()}")