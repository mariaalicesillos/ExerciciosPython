nj = str (input("Jogador, digite o seu nome: "))
sj = float (input("jogador, digite o seu salário em R$: "))
if sj <= 100:
    asj = sj + 0.2 * sj
    print (nj, " , seu novo salário é de R$: ", asj)
elif sj > 100 and sj <= 5000:
        asj = sj + 0.1 * sj
        print (nj, " , seu novo salário é de R$: ", asj)
else: 
    asj = sj + 0.05 * sj
    print (nj, " , seu novo salário é de R$: ", asj)

    