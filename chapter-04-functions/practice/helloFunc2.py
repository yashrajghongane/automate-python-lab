#Arguments and Parameters
def say_hello_to(name):
    print("Good Morning "+ name)
    print("Good Afternoon " + name)
    print("Good Eveing " + name)

say_hello_to("Yash")
say_hello_to("Yashraj")

say_hello_to("Yash")


import random

def get_answer(answer_num):
    if answer_num == 1:
        return 'It is certain.'
    elif answer_num == 2:
        return 'It is dicidely so'
    elif answer_num == 3:
        return 'Yes'
    elif answer_num == 4:
        return 'Reply hazy try again'
    elif answer_num == 5:
        return 'No'
    
print("Ask a yes or no Quetions")
input("->")
r = random.randint(1,5)
fortune = get_answer(r)
print(fortune)

