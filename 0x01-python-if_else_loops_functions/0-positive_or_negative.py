#!/usr/bin/python3
import random
number = random.randint(-10, 10)
for i in number:
    if i > 0:
        print("{} is positive\n".format(i))
    elif i == 0:
        print("{} is zero\n".format(i))
    else:
        print("{} is negative\n".format(i))
