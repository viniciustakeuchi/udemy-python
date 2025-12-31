num1 = 10
num2 = 10

# Isso é igual a isso? '==' Verifica tipo também.
print(num1 == num2)
# Pergunta se isso é diferente '!=' (exclamação + igual)
print(num1 != num2)
# É maior que?
print(num1 > num2)
# É menor que?
print(num1 < num2)
# É maior ou igual?
print(num1 >= num2)
# É menor ou igual?
print(num1 <= num2)

# Exercício: programa para identificar se é maior ou menor de idade com operadores lógicos
# Para digirir a pessoa tem que ser igual ou maior que 18 anos de idade e ter carteira de motorista

idade = int(input('Digite a sua idade: '))
carteira = True
verificador = idade >= 18 and carteira

print(verificador)

