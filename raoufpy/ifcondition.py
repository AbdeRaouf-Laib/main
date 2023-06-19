#even
a = int(input("enter a number: "))
if a % 2 == 0:
    print("even")
else:
    print("odd")
#agree
try:
    a = input("do you agree? : ").lower()
except:
    print("Error")
if a in ['y' , 'Y' , 'yes' , 'YES' , 'Yes']:
    print("agreed!!")
#lower(): A = a
#upper(): a = A
elif a.upper() == 'N' or  a.upper() == 'NO':
    print("not agreed!!")