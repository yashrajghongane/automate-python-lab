list = [10,20,30,40,50,60]
list_slice = list[2:4]
print(list_slice)
index = len(list) - 1
print(list[index])

print()
# for loop in list

for i in range(4):
    print(i)

print()
#  range() in list

supplies = ["Pen","paper","staplers","binders"]
for i in range(len(supplies)):
    print(f"Index {i} in supplies is {supplies[i]}")


print()
# The in and not in operators 
spam = ["hello","Hi","howdy","hey"]
print("Hi" in spam) # Ture
print("helllllo" not in spam) # True
print("Hi" not in spam) # False

print()
# Random Selection and Ordering
import random

pets = ["cat","dog","mouse","camel"]
rand = random.choice(pets)
rand1 = random.choice(pets)
print(rand1)
print(rand)

people = ["Yash","shiv","Jarvis","falcon"]
random.shuffle(people)
print(people)

# Augmented Assignment Operators
# This operators also used with  +,-,*,/,% operators
spam = 44
spam = spam + 1
print(spam)

# Shortcut 
spam = 45
spam += 1
print(spam)

#  Augmented assignment operators also used with lists and strings

spam = "Hello"
spam += "world"
print(spam)

cats = ["Meomow"]
cats *= 3
print(cats)
