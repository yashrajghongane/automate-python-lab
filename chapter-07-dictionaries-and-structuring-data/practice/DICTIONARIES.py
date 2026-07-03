my_cat = {'size':'fat', 'color':'white','age':'2'}
print(my_cat['size'])
print(my_cat['color'])
print(my_cat['age'])

spam = {122:'yashraj',123:'yashraj'}
print(spam[122])
# print(spam[1]) it will raise KeyErr : 1

print()
# unlike list dict are unordered (you can enter list key-value pair in any order but cannot list)
spam = [1,2,3,4,5]
bcon = [5,4,3,2,1]
print(spam == bcon)

cat1 = {'name':'kitty','age':9,'color':'white' }
cat2 = {'age':9,'name':'kitty','color':'white'}
print(cat1 == cat2)

print()
# Returning Keys and Values
# Values
for v in cat1.values():
    print(v)

print()
# Keys
for k in cat1.keys():
    print(k)

print()
# Items (both key and values)
for i in cat2.items():
    print(i)

print()
# we can also use multiple assignment trick in for loop to assign key and value in sperate varibales

for k, v in cat1.items():
    print("Key: " + str(k), "Value: " + str(v))
    
print()
# Checking Whether a Key Exists or not if key not exits we can return defalut value using get() method.
# dict.get('key',default value)
picninc_items = {"apples":4 , " cups": 2}
print(f"I am bringing {picninc_items['apples']} apples. ")
print(f"I am bringing {picninc_items[' cups']} Cups. ")
print(f"I am bringing {picninc_items.get('eggs',3)} eggs. ")

# setdefault() method 
# if we dont know that key is exits or not in thedict we can use setdefault() ,this method take first arg as key and Second as values 
# if the key doesnt exits this method add that key and set value for that key
# once the key added by setDefault method then can not set value again for that key again beacuse method checks if key exits or not and then assign value 

print(f"I am bringing {picninc_items.setdefault("bottle",1)}") # 'bottle' : 1
print(f"I am bringing {picninc_items.setdefault("bottle",2)}") # 'bottle' : 1 this time it dose not set default value as 2 beacuse the key bottle is exits in dict.
print(picninc_items)

print()
# Nested Dict 
game_characters = {
    "player1" : {
        "name": "Yashraj",
        "role": "warrior",
        "health": 100
    },
    "player2": {
        "name": "Rahul",
        "role": "Wizard",
        "health": 65
    }
}

# Accesing values from nested loop using two sets of square breakets side by side [][]
# Step 1:  open the the player2 door
# Step 2: grab their role 

Rahul_role = game_characters['player2']['role']
print(Rahul_role)

# add and update nested dict

game_characters['player1']["health"] = 70 # point the player1 health and update the value
game_characters['player2']["attack"] = 78 # add new key attack with value 78

print(game_characters['player1']["health"])
print(game_characters['player2'])

# showing all the data usinf .item()

for player_id, stats in game_characters.items():
    print(f"_____ Stats for {player_id} _____")
    
    for key,value in stats.items():
        print(f"{key}: {value}")


print()
# Lists of Dict

students = [
    {"name": "yashraj","age": 18, "grade": "A+"},
    {"name": "rahul","age": 21, "grade": "B+"},
    {"name": "sachin","age": 12, "grade": "A+"}
]

# how to accessing values (Using [index]['key'])
# add or updadte 
new_student = {"name": "alice","age": 20, "grade": "B"} # add new dict to list student
students.append(new_student)

students[0]["age"] = 19
students[0]["performance"] = "Excellent"

# how to Loop thourgh whole stack 

for student in students:
    print(f"{student["name"]} is {student["age"]} years old and gets an {student["grade"]}")


print()
# dict conting list

report_card = {
    "maths":[],
    "science": [23,32,43],
    "history": [43,56,77]
}

# accesing list inside dict
science_marks = report_card["science"][0]
print(science_marks)

# add or update information
report_card["maths"].append(90)
print(report_card["maths"][0])

report_card["maths"][0] = 50
print(report_card["maths"][0])

report_card["Art"] = [100,60]
print(report_card["Art"][1])

# How to loop throught it

for subject,scores in report_card.items():
    avrage = sum(scores) / len(scores)
    print(f"In {subject} the scores are {scores}. Average: {avrage:.1f} ")

# dict.pop method on dict
# this method delete the key and grab the value (return the value of deleted key)

cat3 = {'name':'kitty','age':9,'color':'white' }
removede_feature = cat3.pop("color", "not found")
print(removede_feature)
print(cat3)

# dict.clear()
# this method maked dict empty and live it {}
cat3.clear()
print(cat3) # output {}