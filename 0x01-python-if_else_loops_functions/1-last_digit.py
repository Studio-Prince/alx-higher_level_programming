#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

digit = abs(number)% 10

if number > 0:
    
   pigit = -digit
print(f"Last digit of {number:d} is {digit:d} and is ", end="")
