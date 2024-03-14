#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
ldt = abs(number) % 10
if number < 0:
    ldt = ldt * -1

message = 'Last digit of {} is {} and is '.format(number, ldt)
if ldt > 5:
    message += 'greater than 5'
elif ldt < 6 and ldt != 0:
    message += 'less than 6 and not 0'
else:
    message += '0'

print(message)
