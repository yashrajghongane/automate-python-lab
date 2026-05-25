# Program That Ask Your name Continusly unitl break statemet stops it.

name = ''
while True:
    name = input("Please type your name: ")
    print(name)
    if name == "your name":
        break
   
print("Thank You!")