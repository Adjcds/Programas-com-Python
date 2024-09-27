# Programa de Cálculo de IMC
# Este programa calcula o Índice de Massa Corporal (IMC) de uma pessoa com base no peso e altura.
# A lógica do programa envolve:
# 1. Solicitar o peso da pessoa em quilogramas (kg).
# 2. Solicitar a altura da pessoa em metros (m).
# 3. Calcular o IMC usando a fórmula: IMC = peso / (altura ** 2).
# 4. Exibir o resultado do IMC e a classificação correspondente:
#    - Abaixo do peso: IMC < 18.5
#    - Peso ideal: 18.5 ≤ IMC < 25
#    - Sobrepeso: 25 ≤ IMC < 30
#    - Obesidade: 30 ≤ IMC < 40
#    - Obesidade mórbida: IMC ≥ 40
# 5. Perguntar se o usuário deseja calcular o IMC novamente.

def calcular_imc():
    while True:
        try:
            peso = float(input('Quanto você pesa? (kg) '))
            altura_cm = float(input('Quanto você mede? (cm) '))  # Alterado para cm
            altura = altura_cm / 100  # Converter cm para metros
            
            # Verifica se os valores são válidos
            if peso <= 0 or altura <= 0:
                print("Peso e altura devem ser maiores que zero. Tente novamente.")
                continue
            
            imc = peso / (altura ** 2)
            print(f'Seu IMC é {imc:.2f}')
            
            if imc < 18.5:
                print('Você está abaixo do peso!')
            elif imc < 25:
                print('Você está no seu peso ideal.')
            elif imc < 30:
                print('Você está com sobrepeso.')
            elif imc < 40:
                print('Você está obeso.')
            else:
                print('Você está com obesidade mórbida.')
            
            # Pergunta se o usuário deseja fazer outro cálculo
            continuar = input('Deseja calcular outro IMC? (s/n) ').lower()
            if continuar != 's':
                break

        except ValueError:
            print('Por favor, insira valores numéricos válidos.')

calcular_imc()
