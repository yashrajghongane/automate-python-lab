# Practice Questions
## 1. What keys can you press if your Python program is stuck in an infinite loop?
Ans. Ctrl + C
___

## 2.  What is the difference between break and continue?
Ans. 1. break will exit the loop when loop meets certain condition. \
     2. continue will goes back to start of the loop when loop meets certain condition.
___

## 3.  What is the difference between range(10), range(0, 10), and range(0, 10, 1) in a for loop?
Ans. 1. range(10) -> for loop will continue iteration in upto (0,9) \
     2. range(0,10) -> for loop start with 0 and ends with 9 \
     3. range(0,10,1) -> for loop start with 0 , ends with 9 and incresed the iteration by 1 each time.
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
