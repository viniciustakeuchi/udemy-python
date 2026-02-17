# Cálculo do IMC

'''
Qual é a sua altura em cm: 
Qual é o seu peso em kg:
'''

#mensagem 
def mensagem(imc):
    print(f'Seu índice é: {imc:.2f}')

# Entrada de Dados do usuário
altura = float(input('Qual é a sua altura em cm: '))
peso = float(input('Qual é o seu peso em kg: '))
altura = altura / 100
imc = float(peso / (pow(altura, 2)))

mensagem(imc)
if imc < 18.5:
    print('Magreza')
elif 18.5 <= imc <= 24.9:
    print('Normal')
elif 25.0 <= imc <= 29.9:
    print('Sobrepeso')
elif 30.0 <= imc <= 39.9:
    print('Obesidade')
else:
    print('Obesidade Grave')





