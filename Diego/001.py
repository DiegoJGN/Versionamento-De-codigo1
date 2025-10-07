ano_nasc = int(input("Digite o ano do seu nascimento: "))

ano_atual = 2025

idade = (ano_atual - ano_nasc)

if idade <18:
    print("Menor de idade")

else:
    print("Maior de idade")