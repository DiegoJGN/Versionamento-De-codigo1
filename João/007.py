for i in range(3):
    nome = input(f"Digite o nome da {i+1}ª cidade: ")
    cidades.append(nome) 
    print("Lista atualizada de cidades:", cidades)  

while True:
    nome = input("Digite o nome de uma cidade (ou 'sair' para encerrar): ")
    
    if nome.lower() == 'sair':
        print("Programa encerrado.")
        break

    cidades.append(nome)
    
    print("Lista de cidades atualizada:")
    for cidade in cidades:
        print("-", cidade)