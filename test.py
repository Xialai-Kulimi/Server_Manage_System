import math

n = 0

while True:
    a = math.sqrt((math.pow(3, n) - 1)/2)
    if a - math.floor(a) == 0:
        print(n)
        print(a)
    n += 1
