idade = int(input("Digite sua idade: "))
if idade >= 0 and idade <= 11:
    classificacao = "Criança"
elif idade >= 12 and idade <= 18:
    classificacao = "Adolescente"
elif idade >= 19 and idade <= 24:
    classificacao = "Jovem"
elif idade >= 25 and idade <= 40:
    classificacao = "Adulto"
elif idade >= 41 and idade <= 60:
    classificacao = "Meia Idade"
elif idade > 60:
    classificacao = "Idoso"
else:
    classificacao = "Idade inválida"
print(f"Classificação etária: {classificacao}")
