# Practice Questions

## 1.  What are the two values of the Boolean data type? How do you write them?
Ans.
True and False.
We write them as True and False, with a capital T and F.
___
## 2.  What are the three Boolean operators?
Ans.
and , or , not.
___
## 3.  Write out the truth tables of each Boolean operator (that is, every possible combination of Boolean values for the operator and what they evaluate to).
Ans.
| A | B | A and B | A or B | not A |
|---|---|---------|--------|-------|
| True | True | True | True | False |
| True | False | False | True | False |
| False | True | False | True | True |
| False | False | False | False | True |

## 4.  What do the following expressions evaluate to?

~~~python 
(5 > 4) and (3 == 5)
not (5 > 4)
(5 > 4) or (3 == 5)
not ((5 > 4) or (3 == 5))
(True and True) and (True == False)
(not False) or (not True)
~~~
Ans. (5 > 4) and (3 == 5) -> False \
not (5 > 4) -> False \
(5 > 4) or (3 == 5) -> True
not ((5 > 4) or (3 == 5)) -> False \
(True and True) and (True == False) -> False \
(not False) or (not True) -> True
___
## 5.  What are the six comparison operators?
|    |            |
|--- |------------|
| == |Equal to    |
| != |not Equal to|
| <  | Less Than  |
| >  | Greater Than|
| <= | Less than or Equal to |
| >= | Greater than or Equal to |


## 6.  What is the difference between the equal to operator and the assignment operator?
Ans. The equal to operator (==) is used to compare two values and returns True if they are equal, and False otherwise. The assignment operator (=) is used to assign a value to a variable. For example, x = 5 assigns the value 5 to the variable x, while x == 5 checks if the value of x is equal to 5.
___
## 7.  Explain what a condition is and where you would use one.
Ans. Condition is an expression that evaluates to True or False. It is used in control flow statements such as if, elif, and else to determine which block of code to execute based on the truth value of the condition. For example, you might use a condition to check if a user is logged in before allowing them to access certain features of a website.
## 8.  Identify the three blocks in this code:
~~~python
spam = 0
if spam == 10:
    print('eggs')
    if spam > 5:
       print('bacon')
    else:
        print('ham')
    print('spam')
print('Done')
~~~ 
Ans. The three blocks in the code are:
1. The first block is the code that is executed if the condition `spam == 10` is True. This block includes the lines:
```print('eggs')```
2. The second block is the code that is executed if the condition `spam > 5     ` is True, which includes the line:
```print('bacon')```
3. The third block is the code that is executed if the condition `spam > 5` is False, which includes the line:
```print('ham')```
___               
## 9.  Write code that prints Hello if 1 is stored in spam, prints Howdy if 2 is stored in spam, and prints Greetings! if anything else is stored in spam.
Ans.
```python
spam = int(input("Enter a value for spam: "))
if spam == 1:
    print("Hello")
elif spam == 2:
    print("Howdy")
else:
    print("Greeetings!")
```