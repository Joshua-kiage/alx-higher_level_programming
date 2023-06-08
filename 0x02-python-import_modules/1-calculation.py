#!/usr/bin/python3
from calculator_1 import add, subtract, multiply, divide

a = 10
b = 5

sum_result = add(a, b)
diff_result = subtract(a, b)
prod_result = multiply(a, b)
div_result = divide(a, b)

print(f"Sum: {a} + {b} = {sum_result}")
print(f"Difference: {a} - {b} = {diff_result}")
print(f"Product: {a} * {b} = {prod_result}")
print(f"Division: {a} / {b} = {div_result}")
