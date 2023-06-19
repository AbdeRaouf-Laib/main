
#for
a = int(input("enter a number: "))
for i in range(a):
    print("#")
#while
def main():
    a = get_positive()
    for i in range(a):
        print("#")





def get_positive():
    while True:
        try:
            n = int(input("n: "))
            if n > 0:
                break
        except ValueError:
            print("Error that`s is not an integer")
    return n



main()

for i in range(3):
    print("#")

#\n
for i in range(3):
    print("#",end = ' ')
print()
print("# " * 3)
for i in range(3):
    for i in range(3):
        print("#",end = ' ' )
    print(end = '\n')
for i in range(3):
    print("# " * 3)