senha = "malithales"
i = 1
while i < 4:
    digiSenha = str(input("Digite sua senha: "))
    if digiSenha == senha:
        print("Acesso permitido")
        break
    elif i < 3:
        print("Acesso negado")
    else:
        print("Conta Bloqueada")
    i+=1