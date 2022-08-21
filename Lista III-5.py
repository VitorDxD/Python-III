#Escreva um algoritmo que liste, em ordem decrescente, todos os números
#impares que existem entre 1 e 100.

nmb = 100
nums = 0

while nmb > 0:
    if nmb%2 != 0:
        print(nmb)
        nums += 1
    nmb -= 1
print(f"Esses são os {nums} números impares decrescentes entre 1 e 100.")
