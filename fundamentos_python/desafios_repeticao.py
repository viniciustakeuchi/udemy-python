# Contagem de 1 a 10.

for i in range(1, 11):
    print(i)
    
# Números pares, de 0 a 20

for i in range(0, 21):
    if i % 2 == 0:
        print(i)
        
# Peça números ao usuário até ele digitar 0. Depois mostre o número de tentativas até digitar 0.
soma = 0
numero = -1         
while numero != 0:
    numero = int(input('Digite um número: '))
    soma += 1
    if numero == 0:
        print(f'Qt de tentativas até acertar: {soma}')

# Pedir o usuário um número e contar até o numero que ele digitou
numero = int(input('Digite um número: '))
soma = 0
while soma < numero:
    soma+=1
    print(soma)

# Contagem regressiva

numero = int(input('Digite um número: '))
while numero >= 0:
    print(numero)
    numero -=1
    
# Somar até passar de 100
    
soma = 0

while soma <= 100:
    numero = int(input("Digite um número: "))
    soma += numero

print("Soma final:", soma)

    
    
