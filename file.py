# r => only read
# w => only write and create a file"clear old data"
# a => append and create a file "save to old data"
#how to use
# open file
# do what you want
# close file
open("week6/tsta.txt","w")
open("test.txt","a")
file1 = open("test.txt","r")
data = file1.read()
print(data)
data = file1.readable()
print(data)
file2 = open("tst.txt","w")
x = file2.readable()
print(x)
file1.close()
file2.close()