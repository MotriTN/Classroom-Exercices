pg = 0
z = 0
for i in range(1, 11):
    a = int(input(f"Donner le nombre n°{i} :"))
    if a > pg:
        pg = a
        z = i
print(pg, "est le plus grand nombre, c'est le nombre n°,", z)
