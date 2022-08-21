#Escreva um algoritmo que liste os primeiros 50 números pares.

nums = 0
nmb = 0

while nums < 50:
    if nmb%2 == 0:
        print(nmb)
        nums += 1

    nmb += 1
print(f"Esses são os {nums} primeiros números pares.")

