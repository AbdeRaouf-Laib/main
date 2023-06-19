import csv
for i in range(10):
    file = open("phonebookf.csv","a")
    #get name ,number
    name = input("name: ")
    number = input("number: ")
    #append data to csv file as row
    writer = csv.writer(file)
    writer.writerow([name,number])