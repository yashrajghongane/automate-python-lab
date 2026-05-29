import time, sys

try:
    while True:
        for i in range(1,9):
            print("-" * (i * i))
        time.sleep(0.60)
         
        for i in range(9,1,-1):
            print("-" * (i * i))
        time.sleep(0.60)

except KeyboardInterrupt:
    sys.exit()