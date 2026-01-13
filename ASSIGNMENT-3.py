'''TASK-1'''
#Calculate Factorial Using a Function

def factorial(n):
    if n < 0:
        return "Factorial does not exist for negative numbers"
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

num = 5
print(f"Factorial of {num} is: {factorial(num)}")
print()

'''TASK-2'''
#Using the Math Module for Calculations

import math

number = float(input("Enter a number: "))

sqrt_result = math.sqrt(number)
log_result = math.log(number)
sin_result = math.sin(number)

print(f"Square root: {sqrt_result}")
print(f"Logarithm: {log_result}")
print(f"Sine: {sin_result}")
