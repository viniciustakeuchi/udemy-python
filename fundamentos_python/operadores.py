numero1 = 10
numero2 = 5

# soma
print(numero1 + numero2)
# subtração
print(numero1 - numero2)
# multiplicação
print(numero1 * numero2)
#divisao
print(numero1 / numero2)
# divisao inteira
print(numero1 // numero2)
# resto da divisao
print(numero1 % numero2)
# potência
print(numero1 ** numero2)

# programa calculando desconto sob o produto
preço_total = float(input('Digite o valor do produto: '))
desconto = float(input('Digite o desconto que você deseja aplicar sob a compra: '))
print(f'O valor final do produto com o cupom de 10% aplicado é: R${preço_total - (preço_total * desconto / 100)}')


