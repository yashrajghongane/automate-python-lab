# Methods of list
# finding values index() - returns index if passed value found in list otherwise raises error
try:
    animals = ['cat',"dog","tiger","lion","tiger"]
    print(animals.index("tiger"))
    print((animals.index("Cow")))
except ValueError as err:
    print(err)

# Adding values
# append() - add items in the end of list.
# insert() - it can add items to specific index takes first argument as index , and second as value.
# this are the list methods and only works with it.

spam = ["cat","dog","tiger"]
spam.append("mouse")
print(spam) # cat, dog, tiger, mouse

spam.insert(2,"bat") 
print(spam) # cat, dog, bat, tiger, mouse

# Removing Values
# remove() - accepts a value to remove from the list  .
# if you attempt to delete a value that dose not present in list then it will give ValueError
# if value appers multiple times then it will remove only the first instance of it.

spam.remove("bat")
print(spam)

# del statement is useful when you want know the index.
# remove() is useful when you know the value it self

# Sorting Valuse
# can sort list of numbers of values or lists of strings . with sort()
# this method always return the numbers of numerical or strings in alphabetical order .
# we can also pass True as the value of reverse keyword to sort values in reverse order.
# we cannot sort list which as both numricals and strings values.

spam.sort()
print(spam)

spam.sort(reverse=True)
print(spam)

spam = [1,7,5,3,0,6,3,1]  
spam.sort()
print(spam)

# sort method uses ASCIIbetical order for sorting strings rather than actual alphabetical order . that means uppercase letter comes before lowercase letters

people = ["Alice","ant","Brother","bRother","Yash","yash","Ram","ram",]
people.sort()
print(people)

# if we need sorting in aplhabetical order then we pass str.lower to key keyword argument = sort(key=str.lower)
# this agrument casues to sort() to treat all letter as lowercase without changing the values in the list.

people.sort(key=str.lower)
print(people)

# Reversing Values
# if you needed to quickly reverse the order of list , you can call reverse() list method

spam.reverse()
print(spam)

# to write single instruction into multiple lins we can use (\).

print("Hello yash, i am siri! " + \
      "how are you")

# Short-Circuiting Boolean Operators
# Its simples means when use 1. and 2. or operators keep in mind this short-circuting behaviour
# its means if the 1st epression of "and" operator is False then no matter what the 2nd operator is either True or False it will evalutes to False
# and same for "or" operator if 1st operators is Ture the no matter 2nd is Ture or False it evaulates to True
# this helps to make python core few microsecond faster by avoiding the 2nd expression by running it 

spam = ["cats","dogs"]
# spam = []
if spam[0] == "cats":
    print("A Cat is First Item. ")
else: 
    print("A Cat is not First Item. ")

# in this above example if spam list is empty then it will gives IndexError: list Index out of range error to solve this we can take adavantage of short-circuting

if len(spam) > 0 and spam[0] == "cats":
    print("A Cat is First Item. ")
else:
    print("A Cat is not First Item." )

# in above example even list is empty it will not gives error. 