#String using single quotes
print('Hi, i am Yash!')
print()

#string using Double qoutes
print("what is you name ?")
print()

# Escape sequence 
#  The escape sequences \' and \" let you put single quotes and double quotes inside your strings
# We can Add more characters in string using escape sequence , such as 
# \'  -   Single quote
# \"  -   Double quote
# \t  -   Tab
# \n  -   Newline (line break)
'''\\  -   Backslash # Note - Keep in mind that because the \ backslash begins an escape sequence,
if you want an actual backslash in your string, you must use the \\ escape sequence.'''
spam = 'Say hi to Bob\'s brother.'

print(spam)
print()
question = "Hello,there!\nHow are you?\nI\'m doing fine."
print(question)
print()


# Raw String 
# Raw string let use us string values contain many backslashes. like os files paths.

# without_r_str = "The file is in C:\Users\Alice\Desktop"
# print(without_r_str)
# This line raise an SyntaxError: (unicode error)

with_r_string = r"The file is in C:\Users\Alice\Desktop"
print(with_r_string)
print()

# Multiline Strings
# its easier to use if we want strings without escape sequences 
# A multiline string in Python begins and ends with either three single quotes or three double quotes
# Multiline strings lets use us strings value as we want by ignoring the escape sequences 
'''# means that - Any quotes, tabs, or newlines in between the “triple quotes” are considered part of the string. 
Python’s indentation rules for blocks don’t apply to lines inside a multiline string.''' # ''' is multiline comment

print('''Dear Rahul,

Can you feed Eve's cat this weekend?

Sincerely,
Yash''')

print()

#Multiline Comments
''' While the hash character (#) marks the beginning of a comment for the rest of the line,
a multiline string is often used for comments that span multiple lines '''
"""This is a test Python program.
Written by Al Sweigart al@inventwithpython.com

This program was designed for Python 3, not Python 2.
"""
def say_hello():
    """This function prints hello.
    It does not return anything."""
    print('Hello!')
    
say_hello()

# Indexes and Slices
''' 
'   H  e   l   l   o  ,     w  o  r  l  d   !  '  # String
    0  1   2   3   4  5  6  7  8  9 10  11 12     # Index   
  -13 -12 -11 -10 -9 -8 -7 -6 -5 -4 -3 -2  -1     # Index   
'''

greeting = "Hello, world!"
print(greeting[1])
print(greeting[-1])
print(greeting[:5])
print(greeting[7:-1])
print(greeting[7:])
print()
'''
Note that slicing a string doesn’t modify the original string.
You can capture a slice from one variable in a separate variable.
'''

# The in and not in Operators
print('Hello' in 'Hello, World') # True
print('HELLO' in 'Hello, World')
print('cats' not in 'cats and dogs')
print()

# F-Strings
# F-strings let use us string literals in strings
# like Raw string which usages r prefix, F string usages f prefix begining of string

name = "Yashraj"
age = 18
print(f"I\'m {name} and I\'m {age} year old.")

# String Methods
# Changing the Case
# upper() and lower() method returns new string with all letters converted into uppercase or lowercase of the orginal string

spam = "Hello, World."
print(spam.upper())
print(spam.lower())

# This methods dose not change orginal strings that if we want to change it we need to asign it into same variable again.
spam = spam.upper()
print(spam)
print()

# This methods are useful when we need case insensitive comparison 
# here is small program that shows you example of its use 

feeling = input("How are You ? -> ")
if feeling.lower() == "great":
  print("I feel great too. ")
else: 
  print('I hope the rest of your day is good.')
  
print()
# checking that strings has at least one letter and all letters in either uppercase or lowercase otherwise method will return False 
spam = "Hello, World." 
print(spam.islower()) # False ( It will return False cause 2 letters are in upper case )  
new_spam = spam.lower() # here lower() method will return new string in all letters in lowercase since follwing like will return True.
print(new_spam.islower()) # True

# Same for Uppercase
print(spam.isupper()) # False 
spam_2 = spam.upper() 
print(spam_2.isupper()) # True

# Note this methods only apply on Strings which has letter (can be with numbers) If we try this with only numbers it will returns False
numbers = "num12345"
new_numbers = "12345"
print(numbers.islower()) # True (it has string abc in lowercase then method will return True)
print(new_numbers.islower()) # False
print(new_numbers.isupper()) # False 

print()

# like this above 2 methods string have other methods too that start with is. and return Boolean True or False
# isalpha() Returns True if the string consists only of letters and isn’t blank
# isalnum() Returns True if the string consists only of letters and numbers (alphanumerics) and isn’t blank
# isdecimal() Returns True if the string consists only of numeric characters and isn’t blank
# isspace() Returns True if the string consists only of spaces, tabs, and newlines and isn’t blank
# istitle() Returns True if the string consists only of words that begin with an uppercase letter followed by only lowercase letters

print('Hello'.isalpha()) # True
print("12345".isalnum()) # True
print('hello123'.isalnum()) # True
print("414".isdecimal()) # True
print('   '.isspace()) # True
print("This Is Title".istitle()) # True 
# There are many more methods string have that start with { is }
# these methods are useful while validating user inputs - 
print()

# here is examples of that 

# Ex 1 -
while True:
  age = input("Enter the your age -> ")
  if age.isdecimal():
    print(f"Age saved as {age}.")
    break
  print("Plz enter number for your age. ")

# Ex 2 - 
while True:
  password = input("Enter the your password -> ")
  if password.isalnum():
    print("password saved.")
    break
  print("Passwords can only have letters and numbers.")
  
print()
# Checking the Start or End of a String
# there are 2 methods of strings we have so we can check that they are begins or end respectively with the string passed to method; otherwise it will retrun False.
# "str".startswith("string") # True
# "str".endswith("string") # False
print("Hello, world".startswith("Hello")) # True
print("Hello, world".startswith("hello")) # False
print("Hello, world".endswith("Hello")) # False
print("Hello, world".endswith("ld")) # True
print("Hello, world".endswith("world")) # True
print()

# Joining and Splitting Strings
# the join method is usefull when we list of strings that needed to join together into a string value
# we call the join method on string and pass it a list of string and it returns the concatenation of each string in the passed-in list.
print(", ".join(["cats","dogs","bats"]))
print(' '.join(['My', 'name', 'is', 'Simon']))