# r+ => read and write
# w+ => read and write and creat file clear old data
# a+ => read and write and crear file save old data
file = open("file3.txt","r+")
print(  file.readable())
print( file.writable())
file.close()
file = open("file4.txt","a+")
print(  file.readable())
print( file.writable())
file.close()
file = open("file5.txt","w+")
print(  file.readable())
print( file.writable())
file.close()
#with is a function in which you assign a shortcut to text for use 'as'
with open("file6.txt","a+") as file:
    print(file.readable())
