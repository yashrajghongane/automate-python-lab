# Sequence Data Types
# Python Sequence Data Types are lists, strings, range objects returned by range() and  tuples 
# we can do slicing indexing for loops len() all of this on this data types also
name = "Yashraj"
print(name[0])
print(name[-2])

print(name[0:4])
print("Yash" in name)
print("P" not in name)

for i in name:
    print("* * * " + i + " * * *")

# Mutable and Immutable Data Types
# lists are mutable data type and strings are immutable data types
# means you can change add remove lists values but cannot strings , if tryes to reassign value to a sting it will cause error

# name[2] = "p"
# print(name)

# this code give an error beacuse strings cannot reassign character to string
# the proper way to mutate a string it to use slicing and concatination to build new string
name = "Yashraj is boy"
new_string = name[0:10] + " Brave " + name[11:14]
print(new_string)

# and there is differnce between modifying list and replacing entire list with new list values

eggs = ["X","Y","Z"]
eggs = ["x","y","z"]
print(eggs)

# This code modifies the existing list in place.
# We remove the old items using del and add new items using append().
# The original list object is changed rather than replaced.

eggs = ['A', 'B', 'C']
# del eggs[0:]
# del eggs[2]
# del eggs[1]
# del eggs[0]
# or we can use list.clear()
eggs.clear()
eggs.append("a")
eggs.append("b")
eggs.append("c")
print(eggs)
 
print()
#  Tuple Data type
# its immutable form of list data type
# there is only 2 differnces between list and tuple 
# 1. we use () parentheses instead of [] brackets

spam = ("abc",23,5.4)
print(spam[1])
print(spam[1:3])
print(len(spam))

# 2. we can not add modify remove their values of tuple like string if try it will gives TypeError : 'tuple' obj does not support item assignment
try:
    spam[2] = 3.14
    print(spam)
except TypeError as err:
    print(err)

# if you have only one value in tuple you can indicate that using commma (,) after 1st item 
tup = type(("hello",))
print(tup)
# if you entred comma after 1st value then it acts as string 
tup1 = type(("hello"))
print(tup1)

# List and Tuple Type Conversion
# just as str() - str(32) return '32'
# list() and tuple() works same as str()
# list() converts an iterable into list 
# tuple() converts and iterable into tuple

list1 = ["X","Y","Z"]
tup = ("abc",23,5.4)

print(list(tup)) # will return list 
print(tuple(list1)) # will return tuple

# References
spam = 42 # we create value 42 in computers memory and stroing spam as refrence of that 42 value 
eggs = spam # here we storing eggs refrence for same 42 value 
# now 42 Has two refrences or both spam and eggs variable refer to value 

# but list dosent works like this 
spam = [0, 1, 2, 3]
eggs = spam # eggs also refer list [0,1,2,3] 
eggs[1] = "Hello" # this will change value of list so list becomes [0, "Hello", 2, 3]
print(spam)
print(eggs)
# both will vairables refers to the same list.

# if you want the python not just copies just refrence and a functions changes the original values mutable data types such as list and dict.
# for avoiding that we use copy module and its copy()
import copy

spam = [1,2,3,4]
eggs = copy.copy(spam)
eggs[2] = 5
print(spam)
print(eggs)

list = [[1,3],[1,23]]
list1 = copy.deepcopy(list)
print(list)
print(list1)