def saudacao(nome):
    print(f'Olá, {nome}')

nome = input('Digite o seu nome')
saudacao(nome)

def somar(num1, num2):
    return num1 + num2

num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))

total = somar(num1, num2)
print(total)

