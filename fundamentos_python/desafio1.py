# Desafio: desenvolver um código que calcula quantos dias o produto dura se a pessoa usar X porçoes por dia.
porcao_total = int(input('Quantas porções o produto tem no total? '))
porcao_dia = int(input('Quantas porções por dia você vai consumir? '))

qt_dias = porcao_total / porcao_dia

# brincando com casas decimais com f-string...
# mostrando 0 casas decimais da variável qt_dias, usando :[n°casas].f exemplo: 10 dias
print(f'O produto será consumido por {qt_dias:.0f} dias')
# mostrando 0 casas decimais da variável qt_dias, transformando em int
print(f'O produto será consumido por {int(qt_dias)} dias')







