pg = 0
for i in range(1, 11):
    a = int(input(f"Donner le nombre n°{i} :"))
    if a > pg:
        pg = a
print(pg, "est le plus grand nombre")
