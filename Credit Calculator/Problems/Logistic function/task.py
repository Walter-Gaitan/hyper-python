import math

x = int(input())
formula = 1 / (1 + pow(math.e, -x))
print(f'{round(formula, 2)}')
