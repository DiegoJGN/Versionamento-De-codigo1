ano_nasc = int(input("Digite o ano do seu nascimento: "))

ano_atual = 2025

idade = (ano_atual - ano_nasc)

if idade >= 0 and idade <= 11:
    print("Criança")

elif idade >= 12 and idade <= 17:
    print("Adolescente")

elif idade >= 18 and idade <= 24:
    print("Jovem")

elif idade >= 25 and idade <= 40:
    print("Adulto")

elif idade >= 41 and idade <= 60:
    print("Meia idade")

else:
    print("Idoso")
