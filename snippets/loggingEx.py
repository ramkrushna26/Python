#!/bin/python3

import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(message)s')

# provide filename to capture log in file
#logging.basicConfig(filename='',level=logging.DEBUG, format='%(asctime)s - %(message)s')
# for disabling DEBUG type of log
#logging.disable(logging.DEBUG)

logging.debug('start of program')
def factorial(n):
    logging.debug('start of factorial(%s)' % (n))
    total = 1
    for i in range(n + 1):
        total = i * total
        logging.debug('i is %s, total is %s' % (i, total))

    logging.debug('return value is %s' % (total))
    return total

print(factorial(5))
logging.debug('end of program')

# there are file levels of logging levels, like this case we are using DEBUG
# there other like info, critical, warning and error
