# This program counts frequency of words in a string
message = "Hello world , hello world and this is Hello form Yashraj , hello to Yashraj "
message = message.lower()
count = {}

for word in message.split():
    word = word.strip(",.?!")
    count.setdefault(word,0)
    count[word] += 1

for key,value in count.items():
    print(f"{key}: {value}")