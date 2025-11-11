INSUMOS_POR_MARMITA = {
    "arroz": 100,
    "feijao": 50,
    "carne": 25,
    "salada": 10
}

estoque = {
    "arroz": 5000,
    "feijao": 2500,
    "carne": 1000,
    "salada": 400
}

def calcular_marmitas_possiveis():
    """Calcula quantas marmitas podem ser feitas com o estoque atual"""
    return min(estoque[item] // INSUMOS_POR_MARMITA[item] for item in INSUMOS_POR_MARMITA)

def vender_marmita(qtd=1):
    """Realiza a venda de marmitas, atualizando o estoque"""
    global estoque
    marmitas_possiveis = calcular_marmitas_possiveis()
    
    if qtd > marmitas_possiveis:
        print(f"❌ Não é possível vender {qtd} marmitas. Só dá pra fazer {marmitas_possiveis}.")
        return

    for item in INSUMOS_POR_MARMITA:
        estoque[item] -= INSUMOS_POR_MARMITA[item] * qtd

    print(f"✅ {qtd} marmita(s) feita(s) com sucesso!")
    mostrar_estoque()

def mostrar_estoque():
    """Exibe o estoque atual e quantas marmitas ainda podem ser feitas"""
    print("\n📦 Estoque atual:")
    for item, qtd in estoque.items():
        print(f" - {item.capitalize()}: {qtd} g")
    print(f"🍱 Marmitas possíveis com o estoque: {calcular_marmitas_possiveis()}\n")

mostrar_estoque()

vender_marmita(5)
vender_marmita(10)
