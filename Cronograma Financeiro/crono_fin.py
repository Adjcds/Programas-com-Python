# Programa de Planejamento Financeiro
# Este programa ajuda você a planejar suas finanças mensais considerando seu salário,
# despesas fixas (como faculdade, luz, e outros gastos essenciais) e quanto você gostaria de economizar.
# A lógica do programa envolve:
# 1. Definir seu salário mensal e suas despesas fixas.
# 2. Calcular suas despesas mensais totais, incluindo faculdade, luz e um valor extra para imprevistos.
# 3. Calcular o saldo disponível após deduzir essas despesas.
# 4. Projetar quanto você pode economizar até uma data futura, como julho de 2026, com base no saldo disponível.
# 5. Avaliar se o valor economizado será suficiente para cobrir seus objetivos, como habilitação
# e cursos de programação que você deseja fazer.
# O objetivo é fornecer uma visão clara de suas finanças e ajudar no planejamento para atingir
# seus objetivos e possiveis sonhos.

import time
from datetime import datetime

# obter dados do usuário
def obter_dados():
    salario_min = float(input("Digite o valor mínimo que você recebe por mês: R$ "))
    salario_max = float(input("Digite o valor máximo que você recebe por mês: R$ "))

    while True:
        try:
            num_despesas = int(input("Quantas despesas fixas você tem (ex: faculdade, luz)? "))
            if num_despesas < 0:
                print("O número de despesas deve ser um número inteiro positivo. Tente novamente.")
            else:
                break
        except ValueError:
            print("Por favor, insira um número inteiro válido para o número de despesas.")

    despesas = []
    for i in range(num_despesas):
        despesa = float(input(f"Digite o valor da despesa {i + 1}: R$ "))
        despesas.append(despesa)

    # reservado para imprevistos
    valor_imprevistos = float(input("Digite o valor que você reserva mensalmente para imprevistos: R$ "))

    objetivo = float(input("Qual é o valor total do seu objetivo (habilitação, cursos, etc.)? R$ "))

    while True:
        try:
            data_limite = input("Até qual data (formato Dia/Mês/Ano) você pretende atingir seu objetivo? ")
            data_limite = datetime.strptime(data_limite, "%d/%m/%Y")
            if data_limite <= datetime.now():
                print("A data deve ser futura. Insira uma data válida.")
            else:
                break
        except ValueError:
            print("Formato de data inválido. Por favor, insira a data no formato DD/MM/YYYY.")

    return salario_min, salario_max, despesas, valor_imprevistos, objetivo, data_limite

# calcular o saldo disponível mensal
def calcular_saldo(salario, despesas, valor_imprevistos):
    total_despesas = sum(despesas) + valor_imprevistos
    saldo = salario - total_despesas
    return saldo

# calcular o número de meses restantes até a data limite
def calcular_meses_restantes(data_limite):
    data_atual = datetime.now()
    # Calculando a diferença em dias e convertendo para meses
    dias_restantes = (data_limite - data_atual).days
    meses_restantes = dias_restantes // 30
    return meses_restantes

# Função para projetar a economia até a data limite
def calcular_economia_projetada(salario_min, salario_max, despesas, valor_imprevistos, data_limite):
    saldo_min = calcular_saldo(salario_min, despesas, valor_imprevistos)
    saldo_max = calcular_saldo(salario_max, despesas, valor_imprevistos)
    
    if saldo_min < 0:
        return 0, 0  # Não é possível economizar com saldo negativo
    
    meses_restantes = calcular_meses_restantes(data_limite)
    economia_min = saldo_min * meses_restantes
    economia_max = saldo_max * meses_restantes
    
    return economia_min, economia_max, meses_restantes

# Função principal
def main():
    print("Bem-vindo ao Planejador Financeiro!")
    salario_min, salario_max, despesas, valor_imprevistos, objetivo, data_limite = obter_dados()

    print("\nCalculando quanto você pode economizar mensalmente até sua data limite...")
    time.sleep(2)

    economia_min, economia_max, meses_restantes = calcular_economia_projetada(
        salario_min, salario_max, despesas, valor_imprevistos, data_limite
    )

    # Mostrar quanto tempo resta até o objetivo
    print(f"\nVocê tem {meses_restantes} meses até {data_limite.strftime('%d/%m/%Y')}.")
    
    # Exibir quanto pode ser economizado no intervalo de salário
    print(f"Com o salário mínimo de R$ {salario_min:.2f}, você poderá economizar aproximadamente R$ {economia_min:.2f}.")
    print(f"Com o salário máximo de R$ {salario_max:.2f}, você poderá economizar aproximadamente R$ {economia_max:.2f}.")
    
    # Avaliação da meta
    if economia_max >= objetivo:
        print("\nParabéns! Você conseguirá atingir sua meta dentro do prazo com seu planejamento financeiro.")
    else:
        print("\nHmm... parece que você não conseguirá atingir sua meta no prazo. Considere ajustar suas despesas ou aumentar sua renda.")

# Executando o programa
if __name__ == "__main__":
    main()
