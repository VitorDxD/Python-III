#Escreva um algoritmo que escreva a tabuada de multiplicação dos números entre
#1 e 10.
nums = 0

for x in range(11):
    for y in range(11):
        print(f" {x} x {y} = {x * y} ")
        nums += 1

        if nums == 11:
            print("====================")
            nums = 0
