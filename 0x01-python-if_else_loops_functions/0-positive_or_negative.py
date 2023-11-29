#!/usr/bin/python3
import random
number = random.randint(-10, 10)
if number > 0:
    print(f"{number:d} Positive")
elif number == 0:
    print(f"{number:d} Zero")
else:
    print(f"{number:d} Negative")
