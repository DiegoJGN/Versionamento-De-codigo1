from datetime import datetime
import math

PRECO_HORA = 12.00
PRECO_FRACAO_15_MIN = 3.00
PRECO_DIARIA = 60.00
MINUTOS_FRACAO = 15
MINUTOS_HORA = 60
HORAS_DIARIA = 24

def calcular_valor_permanencia(tempo_permanencia_minutos):
    """Calcula o valor total a ser pago com base no tempo de permanência em minutos."""
    
    if tempo_permanencia_minutos <= 0:
        return 0.00
    
    if tempo_permanencia_minutos >= HORAS_DIARIA * MINUTOS_HORA:
        num_diarias = math.ceil(tempo_permanencia_minutos / (HORAS_DIARIA * MINUTOS_HORA))
        valor_total = num_diarias * PRECO_DIARIA
        return valor_total

    num_fracoes = math.ceil(tempo_permanencia_minutos / MINUTOS_FRACAO)
    
    valor_total = num_fracoes * PRECO_FRACAO_15_MIN
    
    if valor_total > PRECO_DIARIA:
        return PRECO_DIARIA
        
    return valor_total

def formatar_tempo(minutos):
    """Formata o tempo de permanência em dias, horas e minutos."""
    dias = minutos // (HORAS_DIARIA * MINUTOS_HORA)
    minutos_restantes = minutos % (HORAS_DIARIA * MINUTOS_HORA)
    
    horas = minutos_restantes // MINUTOS_HORA
    minutos_finais = minutos_restantes % MINUTOS_HORA
    
    tempo_formatado = ""
    if dias > 0:
        tempo_formatado += f"{dias} dia{'s' if dias > 1 else ''}, "
    if horas > 0 or (dias == 0 and minutos_finais > 0): 
        tempo_formatado += f"{horas} hora{'s' if horas != 1 else ''} e {minutos_finais} minuto{'s' if minutos_finais != 1 else ''}"
    elif dias == 0 and minutos_finais == 0:
        tempo_formatado = "0 minutos"
        
    return tempo_formatado.strip().rstrip(',')

def registrar_entrada():
    """Solicita e registra os dados de entrada do veículo."""
    print("\n--- Registro de Entrada ---")
    
    while True:
        placa = input("Digite a placa do veículo: ").strip().upper()
        if placa:
            break
        print("Placa não pode ser vazia. Tente novamente.")

    while True:
        try:
            data_hora_str = input("Digite a data e hora de entrada (DD/MM/AAAA HH:MM): ")
            data_hora_entrada = datetime.strptime(data_hora_str, "%d/%m/%Y %H:%M")
            break
        except ValueError:
            print("Formato de data e hora inválido. Use o formato DD/MM/AAAA HH:MM. Tente novamente.")
            
    return {'placa': placa, 'entrada': data_hora_entrada}

def processar_saida(dados_entrada):
    """Solicita os dados de saída, calcula o tempo e o valor, e imprime o ticket."""
    placa = dados_entrada['placa']
    data_hora_entrada = dados_entrada['entrada']
    
    print(f"\n--- Saída do Veículo Placa: {placa} ---")
    
    while True:
        try:
            data_hora_str = input("Digite a data e hora de saída (DD/MM/AAAA HH:MM): ")
            data_hora_saida = datetime.strptime(data_hora_str, "%d/%m/%Y %H:%M")
            
            if data_hora_saida <= data_hora_entrada:
                print("A data/hora de saída deve ser posterior à data/hora de entrada. Tente novamente.")
                continue
                
            break
        except ValueError:
            print("Formato de data e hora inválido. Use o formato DD/MM/AAAA HH:MM. Tente novamente.")

    permanencia = data_hora_saida - data_hora_entrada
    
    tempo_permanencia_minutos = int(permanencia.total_seconds() / 60)
    
    valor_total = calcular_valor_permanencia(tempo_permanencia_minutos)

    tempo_formatado = formatar_tempo(tempo_permanencia_minutos)
    
    print("\n" + "="*40)
    print("         TICKET DE ESTACIONAMENTO")
    print("="*40)
    print(f"Placa do Veículo: {placa}")
    print("-" * 40)
    print(f"Entrada: {data_hora_entrada.strftime('%d/%m/%Y %H:%M')}")
    print(f"Saída:   {data_hora_saida.strftime('%d/%m/%Y %H:%M')}")
    print("-" * 40)
    print(f"Tempo de Permanência: {tempo_formatado}")
    print("-" * 40)
    print(f"Valor Total a Pagar: R$ {valor_total:.2f}")
    print("="*40 + "\n")

def main():
    print("### Sistema de Estacionamento - Cálculo de Tarifa ###")
    print("\n--- Tarifas ---")
    print(f"R$ {PRECO_HORA:.2f} por hora")
    print(f"R$ {PRECO_FRACAO_15_MIN:.2f} por fração de 15 minutos")
    print(f"R$ {PRECO_DIARIA:.2f} por diária (24 horas)")
    
    dados_carro = registrar_entrada()
    
    processar_saida(dados_carro)

if __name__ == "__main__":
    main()