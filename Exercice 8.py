n1 = int(input("Donner Un nombre n1 : "))
n2 = int(input("Donner Un nombre n2: "))
d = (input("Donner Un operateur : "))
match d:
    case "+":
        print(n1 + n2)
    case "-":
        print(n1 - n2)
    case "*":
        print(n1 * n2)
    case "/":
        print(n1 / n2)
    case _:
        print ("opérateur invalide")
