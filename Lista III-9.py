'''
Escreva um algoritmo que leia uma quantidade indefinida de números inteiros
positivos e exiba o seguinte resumo quando o usuário digitar 0:
a. Soma de todos os números;
b. Soma e a quantidade de todos os números pares;
c. Soma e a quantidade de todos os números impares.
'''

somaGeral = 0
somaPar = 0
qntdPar = 0
somaImpar = 0
qntdImpar = 0

num = int(input("Digite um número: "))

while num != 0:
    if num % 2 == 0:
        somaPar += num
        qntdPar += 1

    else:
        somaImpar += num
        qntdImpar += 1
    somaGeral += num

    num = int(input("Digite um número: "))

print(f"A soma geral é: {somaGeral}")
print(f"A soma impar é: {somaImpar}")
print(f"A soma par é: {somaPar}")
print(f"A quantidade de pares é: {qntdPar}")
print(f"A quantidade de impares é: {qntdImpar}")


