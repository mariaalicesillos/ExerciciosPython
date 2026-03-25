vend = int (input("Funcionário, digite seu ID: "))
cp = int (input("Funcionário, informe o código da peça: "))
pre= float (input("Funcionário, informe o preço da peça: "))
qtd = int (input("Funcionário, informe quantas peças foram compradas: "))
fin = pre * qtd
por= 0.05 * fin
print("Seu Id: ", vend)
print("Código da peça: ", cp)
print("Preço unitário: ", pre)
print("Quantidade de peças: ", qtd)
print("Valor final:", fin )
print("Sua comissão é de:", por)