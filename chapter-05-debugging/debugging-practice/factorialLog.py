import logging
logging.basicConfig(filename='factorialLogs.txt',level=logging.DEBUG, format=' %(asctime)s -  %(levelname)s -  %(message)s')
logging.debug("Start of Program")

def factorail(n):
    logging.debug('Start of factorial(' + str(n) + ')')
    total = 1
    for i in range(1,n + 1):
        total *= i
        logging.debug(f'i is ({i}) total is ({total})')
    logging.debug(f'end of factorial ({n})')
    return total

print(factorail(5))
logging.debug("End of Program ")