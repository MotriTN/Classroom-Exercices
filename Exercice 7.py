m = int(input("Donner le mois : "))
while m > 13 or + m == 0:
    m = int(input("Donner le mois : "))
else:
    if m in [3, 4, 5]:
        print("Spring !")
    elif m in [6, 7, 8]:
        print("Summer !")
    elif m in [9, 10, 11]:
        print("Autmn !")
    elif m in [12, 1, 2]:
        print("Winter !")
