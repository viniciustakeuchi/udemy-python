carros = ['BMW X6', 'BMW i5', 'BMW i8']

carro_desejado = input('Qual carro que deseja comprar? ')

if carro_desejado in carros:
    print('Este carro está disponível')
else:
    print('Desculpe, este carro não está disponível')
