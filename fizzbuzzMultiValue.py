#!/usr/bin/env python3.5

num = int(input("How many numbers do you want to check? "))

x = 1
while x <= num:
    if x % 3 == 0 and x % 5 == 0:
        print("Fizz-Buzz")
    elif x % 3 == 0:
        print("Fizz")
    elif x % 5 == 0:
        print("Buzz")
    else:
        print(x)
    x += 1
