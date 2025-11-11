print("Lista das cidades")
lista_cidades = []

print("Escreva os nomes das cidades que você deseja adicionar.")
print("Quando você acabar com a sua lista ou não tem mais o que fazer, digite 'fim'.")

while True:
    cidade = input("Digite o nome de uma cidade: ")
    if cidade.lower() == 'fim' or cidade == '':
        break
    lista_cidades.append(cidade)

print(lista_cidades)
print("\n⬐ Lista das cidades adicionadas ⬎")
for cidade in lista_cidades:
    print(f" ➟ {cidade}")
    