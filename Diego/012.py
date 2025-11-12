nome_produto = input( "digite o nome do produto : ")
estoque_inicial = int(input("digite a qtd : "))
vendidas = int(input("digite a venda : "))

# Lógica para o cálculo
estoque_atual = estoque_inicial - vendidas
porcentagem_vendida = (vendidas / estoque_inicial) * 100
porcentagem_estoque = (estoque_atual / estoque_inicial) * 100

# Exibição dos resultados
print(f"Produto: {nome_produto}")
print(f"Estoque Inicial: {estoque_inicial}")
print(f"Vendidas: {vendidas}")
print(f"Estoque Atual: {estoque_atual}")
print("-" * 20)
print(f"Porcentagem Vendida: {porcentagem_vendida:.2f}%")
print(f"Porcentagem em Estoque: {porcentagem_estoque:.2f}%")

estoque_final_arroz = print(input(" digite a qtd de arroz :"))