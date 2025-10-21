cidades = []
for i in range(len(cidades)):
    nome = input(f"Digite o nome da {i+1}ª cidade: ")
    CLOSE = "SAIR"
    if CLOSE == nome:
        break
    else:
        cidades.append(nome) 
    print("Lista atualizada de cidades:", cidades) 