#Desenvolva um algoritmo que calcula a sequência de Fibonacci e exiba apenas
#os primeiros X elementos da sequência, onde X é um número inteiro positivo
#que deve ser informado pelo usuário. Sabemos que a sequência inicia com o
#número 1 e os elementos subsequentes são o resultado da soma dos seus dois
#antecessores.

qntd = int(input("Quantos números da sequência de Fibonacci você quer ver? "))
rep = 0
while qntd > 0:

    if rep == 0:
        num1 = 0
        num2 = 1
        rep += 1
        #Porque
    else:
        num1 = num2
        num2 = num3

    num3 = num1 + num2
    print(num1)

    qntd -= 1
