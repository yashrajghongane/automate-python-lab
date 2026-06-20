cat_names = []
while True:
    name = input("Enter the name of cat " + str(len(cat_names) + 1 ) + "(or just press enter to stop. : ")
    if name == "":
        break
    cat_names = cat_names + [name]
print("The cats names are :")
for name in cat_names:
    print("  " + name)  
    