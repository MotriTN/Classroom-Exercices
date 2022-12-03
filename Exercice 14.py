a = int(input('Donner a :'))
b = int(input('Donner b :'))
i = 1
while i <= a and i <= b:
    if a % i == 0 and b % i == 0:
        PGCD = i
    i += 1
print(f"Le PGDC de {a} et {b} est {PGCD}")