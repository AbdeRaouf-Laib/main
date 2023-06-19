n = {}
print(type(n))
user = {
    'name':'raouf'
    ,'phone':'0772648478'
    ,"age":26
    ,"country":'algerai'
}
print(user["age"])
phonebook = {
    'raouf' : '0772648478',
    "abdou" : '0554319607',
    "mourad": '0561343574',
    "abderahman":"0665444547"
}
name = input("enteeer the name: ")
if name in phonebook:
    print(f"phone: {phonebook[name]} ")