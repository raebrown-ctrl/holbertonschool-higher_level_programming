#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_dig = (abs(number) % 10)
if(number < 0):
    last_dig *= -1
str1 = "and is greater than 5"
str2 = "and is 0"
str3 = "and is less than 6 and not 0"
if(last_dig > 5):
    str4 = str1
elif(last_dig == 0):
    str4 = str2
else:
    str4 = str3
print(f"Last digit of {number:d} is {last_dig:d} {str4}")
