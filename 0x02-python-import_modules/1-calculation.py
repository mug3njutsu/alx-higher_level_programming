#!/usr/bin/python3

import calculator_1

a = 10
b = 5

sum = calculator_1.add(a, b)
diff = calculator_1.sub(a, b)
multiplication = calculator_1.mul(a, b)
quotient = calculator_1.div(a, b)

print(f"{a:d} + {b:d} = {sum}")
print(f"{a:d} - {b:d} = {diff}")
print(f"{a:d} * {b:d} = {multiplication}")
print(f"{a:d} / {b:d} = {quotient}")
