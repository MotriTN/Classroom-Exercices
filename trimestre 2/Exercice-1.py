ch = input("Donner ch: ")
while not ((ch != "") and (len(ch) % 2) == 1):
    ch = input("Donner ch: ")
if ch[::1] == ch[::-1]:
    print("this number is palindrome")
    l = ["o", "i", "y", "e", "a", "u"]
    d = 0
    for i in range(0, len(ch)):
        if ch[i] in l:
            d += 1
    print("le nombre de voyelles c'est ", d)
else:
    z = 0
    for j in range(0, len(ch)):
        z += ord(ch[j])
    print("le poids de ", ch, " est ", z)
