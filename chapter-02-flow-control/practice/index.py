# IF ELSE and FLOW Control

user_name = "Yashraj"
password = "Pass_#1927"

if user_name == "Yashraj":
    print("Hello, Yashraj")
    if password == "Pass_#1927":
        print("Access Granted.")    
    else:
        print("Wrond Password.")


# Boolean Values
spam = True
notspam = False
if spam:
    print("This is spam.")
if notspam:
    print("This is not spam.")


# elif Keyword
name = 'Carol'
age = 3000
if name == 'Alice':
    print('Hi, Alice.')
elif age < 12:
    print('You are not Alice, kiddo.')
else:
    print('You are neither Alice nor a little kid.')

