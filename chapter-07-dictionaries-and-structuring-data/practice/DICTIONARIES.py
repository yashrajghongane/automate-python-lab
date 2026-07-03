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
