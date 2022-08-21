#Desenvolva uma calculadora para calcular o fatorial de um número inteiro
#positivo. Sabemos que o fatorial de um número é calculado pela multiplicação
#desse número por todos os seus antecessores até chegar no número 1. O fatorial
#do número 0 é 1.

num = int(input("Digite um número inteiro positivo: "))
var = num
fatorial = 1

while var > 0:
    fatorial = fatorial * var
    var -= 1

if num < 0:
    print("Isso não é um número positivo.")
elif num == 0:
    print("O fatorial de 0 é 1")
else:
    print(f"O fatorial de {num} é {fatorial}")

