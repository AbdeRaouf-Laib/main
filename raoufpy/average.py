x = [72 , 33 , 73]
print(f"Average { (x[0] + x[1] + x[2] ) / 3}")
#for function
print(f"Average {sum(x) / len(x)}")
#Request values ​​from the user
s = [72 ]
for i in range(2):
    x = int(input("score: "))
    s.append(x)
print(f"Average { sum(s)/ len(s)}")
d = [72 ]
for i in range(2):
    x = int(input("score: "))
    s += (x)
print(f"Average { sum(s)/ len(s)}")