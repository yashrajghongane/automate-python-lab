import random

for i in range(10):
    if random.randint(0,1) == 0:
        print("H",end=" ")
    else:
        print("T",end=" ")

print()

