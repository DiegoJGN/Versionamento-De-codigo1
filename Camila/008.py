frutas = []
frutas.append(input("Digite o nome da fruta 1 : "))
frutas.append(input("Digite o nome da fruta 2 : "))
frutas.append(input("Digite o nome da fruta 3 : "))
frutas.append(input("Digite o nome da fruta 4 : "))
frutas.append(input("Digite o nome da fruta 5 : "))
print("\nFrutas na ordem definida:")
for i, fruta in enumerate(frutas):
    print(f"{i+1}º {fruta}")
