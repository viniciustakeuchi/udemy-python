# função simples, saudação
def saudacao(nome, idade):
    print(f'Hello World! Meu nome é {nome} e tenho {idade} anos')
    
saudacao('Vini', 22)
saudacao('Roger', 43)
saudacao('Julia', 20)

# soma
def soma(num1, num2):
    return num1 + num2

num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))
total = soma(num1,num2)
print(f'O resultado da soma de {num1} + {num2} é: {total} ')

# desconto
def calcular_desconto(preco, porcentagem):
    return preco - (preco * porcentagem / 100)

preco = float(input('Qual é o preço do produto? '))
porcentagem = float(input('Qual o desconto a ser aplicado? '))
preco_final = calcular_desconto(preco, porcentagem)
print(f'O preço do produto com desconto é de R${preco_final:.2f}')