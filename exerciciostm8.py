soma = 0
print("digite 5 números")

for i in range(5):
    num = float(input(f"número {i + 1}:"))
    soma += num
    print("soma dos 5 números:", soma)
    