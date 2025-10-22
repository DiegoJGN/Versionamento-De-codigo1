print("⬐Lista das cidades adicionadas⬎")
lista_cidades = []

print("Escreva os nomes das cidades que você deseja adicionar.")
print("Quando você acabar com a sua lista ou não tem mais o que fazer, digite 'final'.")

while True:
    cidade = input("Digite o nome de uma cidade: ")
    if cidade.lower() == 'final' or cidade == '':
        break
    lista_cidades.append(cidade)

print(lista_cidades)
print("\nLista das cidades adicionadas:")
for cidade in lista_cidades:
    print(f" ⮕ {cidade}")
