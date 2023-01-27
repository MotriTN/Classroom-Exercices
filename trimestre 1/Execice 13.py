r = int(input("donner le nombre des notes entre 10 et: "))
z = 0
for i in range(1, r + 1):
    a = int(input(f"Donner la note n°{i} :"))
    z = z + a
print("le moyen est:", z / r)