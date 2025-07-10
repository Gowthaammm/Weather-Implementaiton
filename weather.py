import math

# Hardcoded coefficients
a = 1
b = -5
c = 6

D = b**2 - 4*a*c

if D >= 0:
    x1 = (-b + math.sqrt(D)) / (2*a)
    x2 = (-b - math.sqrt(D)) / (2*a)
    print(f"Roots are: {x1} and {x2}")
else:
    print("Complex roots")
