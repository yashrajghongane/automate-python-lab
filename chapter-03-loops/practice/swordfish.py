# continue Statement
while True:
    name = input("Who are You! : ")
    if name != "Yash":
        continue
    password = input("Hello Yash , What is the Password, (it is a fish!): ")
    if password == "swordfish":
        break
print("Access Granted!")