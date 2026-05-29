# Global and local scope


name = "yash"
salary1 = 20000

def greet():
    print("Hello ", name) # print global varaibles value
    local_name = "yashraj" # local varibale
    print(local_name) # print local variables value

greet()

def change_global():
    global salary # it uses gloabal varible dose not create local one
    salary = 1000000 # it chnages value of that gloabal varible
    print(salary1)

change_global()