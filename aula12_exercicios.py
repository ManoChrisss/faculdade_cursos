nome = str(input("Qual seu nome? "))
altura = float(input("Qual sua altura?  "))
peso = float(input("Qual seu peso? "))
imc = peso / (altura ** 2)

print(f"{nome}, seu IMC é {imc:.2f}.")

if imc < 18.5:
    print("Você está abaixo do peso.")
elif 18.5 <= imc < 24.9:
    print("Seu peso está normal.")
elif 25 <= imc < 29.9:
    print("Você está com sobrepeso.")
elif 30 <= imc < 34.9:
    print("Obesidade grau I.")
elif 35 <= imc < 39.9:
    print("Obesidade grau II.")
else:
    print("Obesidade grau III ou mórbida.")
