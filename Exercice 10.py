z = 2
p = True
while p == True:
    n = z
    s = 0
    z = z + 1
    for i in range(1, n // 2):
        if (n % i) == 0:
            s = s + i
            if s == n:
                print(s)