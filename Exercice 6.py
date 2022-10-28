k = int(input("Donner K : "))
while not k > 0:
    k = int(input("Donner K : "))
pai = 0
imp = 0
while k != 0:
    x = k % 10
    if x % 2 == 0:
        pai += 1
    else:
        imp += 1
    k = k // 10
print("il ya", pai, "nombre paire et", imp, "nombre impaire")
