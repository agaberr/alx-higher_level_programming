#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
line1 = " and is greater than 5"
line2 = " and is less than 6 and not 0"
if number < 0:
    n = number % -10
else:
    n = number % 10
if n > 5:
    print("Last digit of {} is {}".format(number, n) + line1)
elif n == 0:
    print("Last digit of {} is {}".format(number, n) + " and is 0")
else:
    print("Last digit of {} is {}".format(number, n) + line2)
