# Crie um programa que receba o peso e a altura de uma pessoa e calcule o Índice de Massa Corporal (IMC). O programa deve classificar o IMC da pessoa de acordo com a tabela a seguir:
# Abaixo do peso: IMC < 18.5
# Peso normal: 18.5 ≤ IMC < 25
# Sobrepeso: 25 ≤ IMC < 30
# Obesidade: IMC ≥ 30

peso = float(input("Digite o peso: "))
altura = float(input("Digite a altura: "))
imc = peso / (altura ** 2 )

if imc < 18.5:
    classificacao =  " Abaixo do peso"
elif imc < 25:
    classificacao = "Peso normal"
elif imc < 30:
    classificacao = "sobre peso"
else:
    classificacao = "Obesidade"

    print("IMC:" , round(imc, 2))
    print("classificacao:" , classificacao)
    