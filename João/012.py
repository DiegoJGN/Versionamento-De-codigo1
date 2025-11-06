# Sistema simples de controle de Marmitex

# Quantidade de insumos usados por marmita (em gramas)
ARROZ_POR_MARMITA = 100
FEIJAO_POR_MARMITA = 50
CARNE_POR_MARMITA = 25
SALADA_POR_MARMITA = 10

# Estoque inicial (em gramas)
estoque_arroz = 5000
estoque_feijao = 2500
estoque_carne = 1500
estoque_salada = 1000

def marmitas_possiveis():
    """Calcula quantas marmitas podem ser feitas com o estoque atual."""
    return min(
        estoque_arroz // ARROZ_POR_MARMITA,
        estoque_feijao // FEIJAO_POR_MARMITA,
        estoque_carne // CARNE_POR_MARMITA,
        estoque_salada // SALADA_POR_MARMITA
    )

print("=== SISTEMA DE CONTROLE DE MARMITEX ===")

while True:
    print("\n📦 Estoque atual:")
    print(f"Arroz:  {estoque_arroz} g")
    print(f"Feijão: {estoque_feijao} g")
    print(f"Carne:  {estoque_carne} g")
    print(f"Salada: {estoque_salada} g")
    print(f"\nCom o estoque atual, é possível fazer {marmitas_possiveis()} marmitas.")

    opcao = input("\nQuantas marmitas foram vendidas? (ou digite 'sair' para encerrar): ")

    if opcao.lower() == "sair":
        print("Encerrando o sistema... Até logo!")
        break

    try:
        qtd = int(opcao)

        if qtd <= 0:
            print("⚠️ Digite um número positivo!")
            continue

        if qtd > marmitas_possiveis():
            print("⚠️ Estoque insuficiente para essa quantidade de marmitas.")
            continue

        # Atualiza o estoque
        estoque_arroz -= ARROZ_POR_MARMITA * qtd
        estoque_feijao -= FEIJAO_POR_MARMITA * qtd
        estoque_carne -= CARNE_POR_MARMITA * qtd
        estoque_salada -= SALADA_POR_MARMITA * qtd

        print(f"✅ {qtd} marmita(s) feita(s) com sucesso!")

    except ValueError:
        print("⚠️ Digite um número válido.")
