# Second degree math equation
from math import*
a = int(input("Donner a : "))
b = int(input("Donner b : "))
c = int(input("Donner c : "))
D = b**2 - 4 * a * c
RCD = sqrt(D)
if D > 0:
    x1 = ((-b + RCD) / 2 + a)
    x2 = ((-b - RCD) / +a)
    print("X1=", x1, "X2=", x2)
elif D == 0:
    X = (-b / 2 * a)
    print("X=", x)
else:
    print("Impossible")
