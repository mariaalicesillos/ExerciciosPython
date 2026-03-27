wei = float (input("digite seu peso em KG:"))
hei = float (input("digite sua altura em metros:"))
imc = wei / hei **2
if imc <18.5:
    print("você está abaixo do peso normal!")
elif imc >18.5 and imc <= 24.9:
    print("você está com o peso normal")
elif imc> 25 and imc <= 29.9:
    print("você está com excesso de peso")
elif imc > 30 and imc <= 34.9:
    print("você está com obesidade classe I")
elif imc > 35 and imc <= 39.9:
    print("você está com obesidade classe II")
else:
    print ("você está com obesidade classe III")