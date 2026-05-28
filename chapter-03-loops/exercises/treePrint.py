# Tree Pinter
size = int(input("Enter the Size of Tree : "))
for row_num in range(1,size + 1):
    print(" " * (size - row_num) + "^" *(row_num * 2 -1))

for i in range(2):
    print(" " * (size - 1) + "#" )

# Using while loop
row_num = 1
i = 0
while row_num < size + 1:
    print(" " * (size - row_num) + "^" *(row_num * 2 -1))
    row_num += 1
while i < 2:
    print(" " * (size - 1) + "#" )
    i +=1
