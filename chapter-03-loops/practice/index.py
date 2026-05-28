# Loops 
# While Loop
spam = 0
while spam < 5:
    print("Hello ,world")
    spam = spam + 1

# # “TRUTHY” AND “FALSEY” VALUES AND THE BOOL() FUNCTION
name = ''
while not name:
    name = input("What is your name : ")
    num_of_guest = int(input("How many Guesst will you have : "))
    if num_of_guest:
        print("Be sure to have room for all guests.")
print("Done")

# # sum of all num 0 to 100
total = 0
for num in range(101):
    total = total + num
print(total)

# Argument to range()

for i in range(10,20): # 10 is starting num , 20 - 1 = ending num
    print(i)

print("\n")

for i in range(0,21,2): # 0 is starting num , 21 - 1 = ending num, 2  = increment by that num
    print(i)

for i in range(5,1,-1): # 5 is starting num, -1 is ending num, -1 = decrement by that num
    print(i)