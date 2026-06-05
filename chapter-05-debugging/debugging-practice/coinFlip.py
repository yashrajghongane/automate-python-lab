import random
head = 0
for i in range(1,1001):
    if random.randint(0,1) == 1:
        head += 1
    if i == 500:
        print("Halfway done!")
print(f"heads came up {head} times! ")