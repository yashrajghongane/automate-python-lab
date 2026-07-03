#This program check occuparance of each character in a string 
message = "It was a bright cool day in April, and clocks were striking thirteen, "
count = {}

for ch in message:
    count.setdefault(ch,0)
    count[ch] = count[ch] + 1

print(count)
