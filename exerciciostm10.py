soma = 0.0 
print("Digite as 3 notas")
for i in range (3):
    notas = float (input(f"número{i+1}:"))
    soma += notas
    media = soma /3.0
if media >= 8 :
        print ("sua média é A")
elif media >= 5 and media <8:
        print(" sua média é B")
else:
        print(" sua média é C")
