n = int(input("n="))
m = int(input("m="))
while not n > 0 and m > 0:
    n = int(input("n="))
    m = int(input("m="))
s1 = 0
s2 = 0
for i in range(1, n):
    if (n % i) == 0:
        s1 = s1 + i
for i in range(1, m):
    if (m % i) == 0:
        s2 = s2 + i
if s1 == m and s2 == n:
    print("amicaux")
else:
    print("non amicaux")