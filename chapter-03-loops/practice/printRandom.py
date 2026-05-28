# Importing Module
import random
for i in range(5):
    print(random.randint(1,10))

# Ending a Program Early with sys.exit()
import sys
while True:
    response = input("Enter exit to exit : ")
    if response == "exit":
        sys.exit()
    print("You typed " + response +'.')
