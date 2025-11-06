from datetime import datetime, timedelta

def calcular_valor(tempo):
    total_minutos = tempo.total_seconds() / 60
    total_horas = total_minutos / 60

    if total_horas >= 8:  # Considera como diária
        return 60.00
    else:
        horas_completas = int(total_horas)
        minutos_restantes = total_minutos - (horas_completas * 60)

        valor = horas_completas * 12.00
        # Cada fração de 15 minutos custa R$3
        fracoes = (minutos_restantes // 15)
        if minutos_restantes % 15 != 0:
            fracoes += 1
        valor += fracoes * 3.00
        return valor


def estacionamento():
    print("=== SISTEMA DE ESTACIONAMENTO ===\n")

    placa = input("Digite a placa do veículo: ").upper()

    data_entrada = input("Digite a data de entrada (dd/mm/aaaa): ")
    hora_entrada = input("Digite a hora de entrada (hh:mm): ")

    data_saida = input("Digite a data de saída (dd/mm/aaaa): ")
    hora_saida = input("Digite a hora de saída (hh:mm): ")

    entrada = datetime.strptime(f"{data_entrada} {hora_entrada}", "%d/%m/%Y %H:%M")
    saida = datetime.strptime(f"{data_saida} {hora_saida}", "%d/%m/%Y %H:%M")

    tempo_permanencia = saida - entrada
    valor_total = calcular_valor(tempo_permanencia)

    horas, resto = divmod(tempo_permanencia.total_seconds(), 3600)
    minutos, _ = divmod(resto, 60)

    print("\n===== TICKET DE ESTACIONAMENTO =====")
    print(f"Placa do veículo: {placa}")
    print(f"Entrada: {entrada.strftime('%d/%m/%Y %H:%M')}")
    print(f"Saída:   {saida.strftime('%d/%m/%Y %H:%M')}")
    print(f"Tempo de permanência: {int(horas)}h {int(minutos)}min")
    print(f"Valor total: R$ {valor_total:.2f}")
    print("====================================")


if __name__ == "__main__":
    estacionamento()
