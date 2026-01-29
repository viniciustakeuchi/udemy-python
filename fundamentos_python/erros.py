# Erros 
# Excelentes para testes
# Não realiza o 'stop' no programa
# Mensagens customizadas quando encontra um erro

try:
    letras = ['a', 'b', 'c']
    print(letras[3])
except IndexError:
    print('Index não existe')

try: 
    valor = int(input('Digite o valor do seu produto: '))
    print(type(valor))
except ValueError:
    print('Favor digitar um valor em números')
finally:
    print('Codigo OK')
# else:
#     print('usuario digitou um valor correto!')
#     resultado = valor * 2
#     print(resultado)