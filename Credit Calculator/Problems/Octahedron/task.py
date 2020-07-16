import math
n = int(input())
area = 2 * math.sqrt(3) * pow(n, 2)
v = 1 / 3 * math.sqrt(2) * pow(n, 3)
print(f'{round(area, 2)} {round(v, 2)}')
