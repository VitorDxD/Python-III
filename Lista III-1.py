#Desenvolva uma calculadora que obedeça às seguintes regras:
#a. O usuário deve informar dois números e qual operação deseja realizar
#    (soma, subtração, multiplicação ou divisão);
#b. O sistema deve validar os números recebidos para que não existam falhas
#    na sua execução. Exemplo: na operação de divisão, o divisor não pode
#    ser zero. Caso exista algum número inválido, o sistema deve retornar um
#    erro;
#c. Após executar a operação matemática, o sistema deve exibir o resultado
#    e informar qual operação foi realizada;
#d. Após a execução, o sistema deve perguntar se o usuário deseja realizar
#    uma nova operação matemática. Caso ele responda SIM, a aplicação
#    deve ser reiniciada.

erro = 0
perg = input("Deseja realizar uma operação? (SIM ou NÃO) ")

while perg == "sim" or perg == "SIM" or perg == "Sim":

    opera = input("Qual operação deseja realizar? ( + , - , . ou / ) ")

    if opera == ".":
        resultado = num1 * num2

    elif opera == "/":

        if num1 == 0 or num2 <= 0:
            erro = 1
            print("Não foi possivel realizar a operação.")
        else:
            resultado = num1 / num2

    elif opera == "-":
        resultado = num1 - num2

    elif opera == "+":
        resultado = num1 + num2

    else:
        erro = 1
        print("Ops... isso não é um sinal de operação matemática")


    if erro == 0:
        num1 = int(input("Digite um número: "))
        num2 = int(input("Digite outro número: "))


    if erro == 0:
        print(f"{num1} {opera} {num2} = {resultado}" )
    print("=========================================================")
    perg = input("Deseja realizar uma operação? (SIM ou NÃO) ")
