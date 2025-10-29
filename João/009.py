nome_completo = input("Digite seu nome completo: ")
partes_nome = nome_completo.split()
if len(partes_nome) >= 2:
    print(partes_nome[1])
else:
    print("Por favor, digite pelo menos nome e sobrenome.")