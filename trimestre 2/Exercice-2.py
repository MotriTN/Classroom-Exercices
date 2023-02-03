ch1 = input("donner ch1: ")
ch2 = input("donner ch2: ")
while not (len(ch1) == len(ch2) and ch1 != ("")):
    ch1 = input("donner ch1: ")
    ch2 = input("donner ch2: ")
z = 0
for i in range(0, len(ch1)):
    if ch1[i] != ch2[i]:
        z += 1
print(f"la distance de hamming entre {ch1} et {ch2} c'est {z} ")
