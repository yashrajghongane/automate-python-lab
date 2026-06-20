my_pets = ["Kitty","Mannya","sweety","tommmy"]
name = input("Enter the your pet name : ")
if name not in my_pets:
    print("I do not have a pet named " + name)
else:
    print(name + " is my pet.")