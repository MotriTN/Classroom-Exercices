# Ecrire un program qui permet de saisir un entier n et donné est ce qui il est primaire
n = int(input("Donner un nombre pour verifier: "))
d = 2
premier = True
while (premier == True) or n == d:
    if n % d == 0:
        premier = False
        print("ce nombre n'est pas premier")
    elif n == d:
        print("ce nombre est premier")
        premier = False
else:
    d = + 1
