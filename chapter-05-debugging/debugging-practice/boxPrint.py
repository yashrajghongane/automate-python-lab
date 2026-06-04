def box_print(symbol,width,height):
    if len(symbol) != 1:
        raise Exception("Symbol must be a single Character string. ")
    if width <= 2:
        raise Exception("Width must be more than 2. ")
    if height <= 2:
        raise Exception("Height must be more than 2. ")

    print(symbol * width)
    for i in range(height - 2):
        print(symbol + (" " * (width - 2)) + symbol)
    print(symbol * width)

try:
    box_print("*",4,4)
    box_print("o",3,3)
    box_print("ZZ",2,1)
    box_print("11",22,11)
except Exception as err:
    print("An Exception happened: "+ str(err))

star = "*"
print(len(star))