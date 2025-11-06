from datetime import datetime, timedelta

# Tabela de preços
VALOR_HORA = 12.00
VALOR_FRACAO = 3.00  # a cada 15 minutos
VALOR_DIARIA = 60.00

# Dicionário para armazenar carros
carros = {}

def registrar_entrada():
    placa = input("Digite a placa do carro: ").upper()
    if placa in carros:
        print("⚠️ Esse carro já está estacionado.")
        return
    entrada = datetime.now()
    carros[placa] = entrada
    print(f"✅ Entrada registrada para {placa} às {entrada.strftime('%d/%m/%Y %H:%M:%S')}")

def registrar_saida():
    placa = input("Digite a placa do carro que vai sair: ").upper()
    if placa not in carros:
        print("⚠️ Nenhum registro encontrado para essa placa.")
        return

    entrada = carros.pop(placa)
    saida = datetime.now()
    tempo = saida - entrada

    # Calcula o valor
    valor = calcular_valor(tempo)

    # Imprime o ticket
    print("\n===== TICKET DE ESTACIONAMENTO =====")
    print(f"Placa: {placa}")
    print(f"Entrada: {entrada.strftime('%d/%m/%Y %H:%M:%S')}")
    print(f"Saída:   {saida.strftime('%d/%m/%Y %H:%M:%S')}")
    horas, resto = divmod(tempo.seconds, 3600)
    minutos = resto // 60
    print(f"Tempo total: {tempo.days} dia(s), {horas}h {minutos}min")
    print(f"Valor a pagar: R$ {valor:.2f}")
    print("====================================\n")

def calcular_valor(tempo: timedelta):
    total_minutos = tempo.total_seconds() / 60

    # Se passou de 12h, cobra diária
    if total_minutos >= 12 * 60:
        dias = (tempo.days + 1) if tempo.seconds > 0 else tempo.days
        return dias * VALOR_DIARIA

    horas = int(total_minutos // 60)
    minutos_restantes = total_minutos % 60

    valor = horas * VALOR_HORA

    # Cobra frações de 15 min (até completar a hora)
    fracoes = (minutos_restantes + 14) // 15  # arredonda para cima
    valor += fracoes * VALOR_FRACAO

    # Valor máximo não pode ultrapassar a diária
    return min(valor, VALOR_DIARIA)

# Programa principal
while True:
    print("\n=== SISTEMA DE ESTACIONAMENTO ===")
    print("1 - Registrar entrada")
    print("2 - Registrar saída")
    print("3 - Listar carros no pátio")
    print("0 - Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        registrar_entrada()
    elif opcao == "2":
        registrar_saida()
    elif opcao == "3":
        if not carros:
            print("🚗 Nenhum carro no estacionamento.")
        else:
            print("Carros no pátio:")
            for placa, hora in carros.items():
                print(f"- {placa} (entrada às {hora.strftime('%H:%M:%S')})")
    elif opcao == "0":
        print("Encerrando o sistema... Até mais!")
        break
    else:
        print("Opção inválida.")
