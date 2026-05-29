import time, sys
indent = 0 # spaces
indent_increasing = True # whether it is incresing oe not

try:
    while True:
        print(" " * indent, end="")
        print("*******")
        time.sleep(0.1)

        if indent_increasing:
            indent += 1
            if indent == 20:
                indent_increasing = False
        else:
            indent -= 1
            if indent == 0:
                indent_increasing = True

except KeyboardInterrupt:
    print("Stopped!")
    sys.exit()