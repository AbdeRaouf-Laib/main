# type function
#int
num = 10
print(type(num))
#float
num = 1.5
print(type(num))
#bool
num = True
print(type(num))
#string
num = "raouf"
print(type(num))

# type  |  brackets  |  ordered  |  mutable  |  duplicate  |     use      |
#-------|------------|----------------------------------------------------|
# list  |     []     |    yes    |    yes    |     yes     |      عام     |
# tuple |     ()     |    yes    |    no     |     yes     |    احداثيات    |
# set   |     {}     |    no     |    no     |     no      | العمليات الرياضة |
# dict  |     {}     |    key    |    yes    |   yes/no    |  قواعد البيانات  |

# --------------------list--------------------------#
# brackets
num = [1,4.5,"hello",[1.5,2],True]
print(num)
# ordered
print(num[2])
# mutable
num[1] = 'ali'
print(num)
# duplicate
num = [1,1,1,1]
print(num)
#---------------------tuple--------------------------#
# brackets
my_tuple = (1,4.5,"hello",[1.5,2],True)
print(my_tuple)
# ordered
print(my_tuple[2])
#duplicate
my_tuple = (1,1,1,1)
print(my_tuple)
#----------------------set---------------------------#
#brackets
my_set = ("ahmed","ali","laib","raouf")
print(my_set)
#---------------------dict---------------------------#
# brackets
car = {
    "color":"red",
    "model":2022,
    "price":200000
}
# ordered
print(car["color"])
# mutable
car["color"] = "black"
print(car["color"])
# duplicate
car = {
    "color":"red",
    "model":2022,
    "color":"black",#no
    "colore":"red"#yes
}
print(car)