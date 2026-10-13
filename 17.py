import math
r = 6.5
a, b = map(float, input().split("x"))
d = r*2
D = math.sqrt(a**2 + b**2)
if D <= d:
    print("да")
else:
    print("нет")