# Practice Questions
## 1. What keys can you press if your Python program is stuck in an infinite loop?
Ans. Ctrl + C
___

## 2.  What is the difference between break and continue?
Ans. 1. break will exit the loop completely when loop meets certain condition. \
     2. continue skips the current iteration and moves to next iteration.

## 3.  What is the difference between range(10), range(0, 10), and range(0, 10, 1) in a for loop?
Ans. 1. range(10) -> start at 0 by default \
     2. range(0,10) -> explicitly start at 0 and ends brefore 10\
     3. range(0,10,1) -> explicitly start at 0, ends before 10 and increased by 1.
___

## 4.  Write a short program that prints the numbers 1 to 10 using a for loop. Then, write an equivalent program that prints the numbers 1 to 10 using a while loop.
Ans. Using for loop ->
~~~python
for i in range(1,11):
    print(i)
~~~ 
\
    Using while loop ->
~~~python
i = 1
while i < 11:
    print(i)
    i = i + 1
~~~ 
___

## 5.  If you had a function named bacon() inside a module named spam, how would you call it after importing spam?
Ans. Firstly we import module using : 
~~~python 
import spam 
~~~
Then we call it using : 
~~~python 
spam.bacon()
~~~
___
