import math

with open('input.txt', 'r') as file:
    a, b, c = map(float, file.readline().split())

D = b**2 - 4*a*c

if D >= 0:
    x1 = (-b + math.sqrt(D)) / (2*a)
    x2 = (-b - math.sqrt(D)) / (2*a)
    print(f"Roots are: {x1} and {x2}")
else:
    print("Complex roots")
