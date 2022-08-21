#Escreva um algoritmo que leia dois números inteiros positivos e exiba_todo os
#números desse intervalo que quando divididos por 5 produzam resto igual a 0.

num1 = int(input("Digite um número: "))
num2 = int(input("Digite outro número: "))

for i in range(num1, num2):
    if i % 5 == 0:
        print(i)
