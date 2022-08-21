#Escreva um algoritmo para autenticar o aluno no portal da faculdade. O aluno
#deve informar seu login e sua senha. O sistema deve realizar as seguintes
#validações:
    #a. Se os dados estiverem corretos, o sistema deve exibir uma mensagem de
        #sucesso e encerrar a aplicação;
    #b. Caso os dados estejam incorretos, o sistema deve exibir uma mensagem
        #de erro e solicitar ao usuário que tente novamente;
    #c. O usuário só pode realizar duas tentativas de login. Caso ele erre as duas
        #vezes, informe que não foi possível fazer a autenticação e que o login
        #dele foi bloqueado. Após isso a aplicação deve ser encerrada;
    #d. O login correto é “aluno” e a senha é 123456.

login = "aluno"
senha = "123456"
logado = 0
tentativas = 0

print("==================================")
print("Bem-vindo ao portal da FAN!")


while logado == 0 and tentativas < 2:
    print("==================================")
    user = input("Login: ")
    password = input("Senha: ")

    if user == "aluno" and password == "123456":
        print("Logado com sucesso!")
        logado = 1

    else:
        tentativas += 1
        if tentativas < 2:
            print("Os dados estão incorretos! Tente novamente.")
        else:
            print("Limite de tentativas excedido. Usuário bloqueado.")
