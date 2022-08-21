'''
Dizemos que um número X é múltiplo do número Y quando o resto da divisão
de X/Y é 0. Com essa informação, faça um algoritmo que exiba todos os
múltiplos de 3 que existem entre 0 e 50.
'''

for i in range(0,51):
    if i % 3 == 0:
        print(i)
