n = int(input("Donner _un nombre n :"))
s = 0
for i in range(1, n // 2):
    if (n % i) == 0:
        s = s + i
print(s)
