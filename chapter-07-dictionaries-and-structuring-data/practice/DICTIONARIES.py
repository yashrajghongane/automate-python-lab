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

