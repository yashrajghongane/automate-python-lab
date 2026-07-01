#birthdays
brithdays = {'Yashraj':"Apr 19",'Shailesh':'Dec 20','Shiv':'Apr 12'}

while True:
    name = input("Enter a Name: (Blank to quit.) ")
    if name == '':
        break

    if name in brithdays:
        print(brithdays[name] + ' is birthday of ' + name) 
    else:
        print("I dont have birthday information for " + name )
        bday = input("What is Their Birthday : ")
        brithdays[name] = bday
        print("birthday Database Updated. ")