# Ecrire un algorithme qui permet de saisir un Entier N et caluculer son factoriel
N = int(input("Donner un entier à factoriser : "))
S = 1
for i in range(1, N + 1):
    S = S * i
print("La Solution est :", S)
