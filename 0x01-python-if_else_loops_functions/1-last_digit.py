#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
ldt = abs(number) % 10
if ldt > 5:
    print('Last digit of {} is {} and is greater than 5'.format(number, ldt))
elif ldt < 6 and ldt != 0:
    print('Last digit of {} is {} and is less than 6 and not 0'.format(number, ldt))
else:
    print('Last digit of {} is {} and is 0'.format(number, ldt))
