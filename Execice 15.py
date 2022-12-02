a = int(input("Give a :"))
i = 0
while a != 0:
    z = (a % 10) * (10)
    a //= 10
    i = z + a
print(i)
