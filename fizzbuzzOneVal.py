#!/usr/bin/env python3.5

value = int(input("Enter an integer value: "))

if value % 5 == 0 and value % 3 ==0:
	print("Fizz-Buzz")

elif value % 3 == 0:
	print("Fizz")

elif value % 5 == 0:
	print("Buzz")

else:
	print(value)


