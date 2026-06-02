# Practice Questions

## 1.  Why are functions advantageous to have in your programs?
Ans. functions make code more modular and redable
___

## 2.  When does the code in a function execute: when the function is defined or when the function is called?
Ans. When the function is called
___

## 3.  What statement creates a function?
Ans. ' def ' statement 
___

## 4.  What is the difference between a function and a function call?
Ans. function have all the code which was not executed unitl function is called, \
and function call is used to call function so function can run their code (code inside the function body) and returing the exact line of code in program
___

## 5.  How many global scopes are there in a Python program? How many local scopes are there?
Ans. There is only 1 global socpes in python program and multiple local scopes a python program can have 
___

## 6.  What happens to variables in a local scope when the function call returns?
Ans. the varibles in local scope will be destroyed when the function call returns.
___

## 7.  What is a return value? Can a return value be part of an expression?
Ans. return value is result of their funtion when the function called then it return some value it is return value , yes
___

## 8.  If a function does not have a return statement, what is the return value of a call to that function?
Ans. It returns None value
___

## 9.  How can you force a variable in a function to refer to the global variable?
Ans.  by using global statement before variable name
___

## 10.  What is the data type of None?
Ans. NoneType
___

## 11.  What does the import areallyourpetsnamederic statement do?
Ans. --
___

## 12.  If you had a function named bacon() in a module named spam, how would you call it after importing spam?
Ans. spam.bacon()
___

## 13.  How can you prevent a program from crashing when it gets an error?
Ans. By using Exception Handling ( try and except )
___

## 14.  What goes in the try clause? What goes in the except clause?
Ans. The code which can cought an error it goes in try clause and the which handle that error will goes in except clause.
___

## 15.  Write the following program in a file named notrandomdice.py and run it. Why does each function call return the same number?
~~~python notrandomdice.py
import random
random_number = random.randint(1, 6)

def get_random_dice_roll():
    # Returns a random integer from 1 to 6
    return random_number

print(get_random_dice_roll())
print(get_random_dice_roll())
print(get_random_dice_roll())
print(get_random_dice_roll())
~~~
Ans. beacuse each function call return same value which is an global variable called random_number in that random.randint(1,6) will assign only one value and get_random_dice_roll(): dose not have any local variable called random_number so it useage global one.
