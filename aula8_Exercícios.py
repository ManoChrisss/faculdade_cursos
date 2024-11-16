nome = str(input("Qual seu nome? "))
sobrenome = (input('Sobrenome, por favor: '))
idade = int(input(f"{nome}, Qual sua idade?"))
ano_nascimento = 2024 - idade
maior_de_idade = idade >= 18
altura_metros = float(input(f"{nome}, qual sua altura?"))
 

print("Agora vamos as suas informações:")
print("------------------------")
print('Nome:', nome)
print(f"Sobrenome: {sobrenome}")
print(f"Idade: {idade}")
print(f"Ano de nascimento: {ano_nascimento}")
if idade >= 18:
    print(f"{nome}, você é maior de idade")
else:
    print(f"{nome}, você é menor de idade")
print(f"Altura: {altura_metros}")


    