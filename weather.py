import math

with open('input.txt', 'r') as file:
    for line in file:
        try:
            a, b, c = map(float, line.strip().split())
            print(f"\nEquation: {a}x² + {b}x + {c} = 0")
            D = b**2 - 4*a*c
            if D > 0:
                x1 = (-b + math.sqrt(D)) / (2*a)
                x2 = (-b - math.sqrt(D)) / (2*a)
                print(f"Real Roots: {x1:.2f}, {x2:.2f}")
            elif D == 0:
                x = -b / (2*a)
                print(f"One Real Root: {x:.2f}")
            else:
                real = -b / (2*a)
                imag = math.sqrt(-D) / (2*a)
                print(f"Complex Roots: {real:.2f} ± {imag:.2f}i")
        except ValueError:
            print("Invalid line, skipping.")
