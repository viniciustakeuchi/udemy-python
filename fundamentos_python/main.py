from funcoes import saudacao, soma, verificar_maioridade

saudacao('Vinícius')
print(soma(2,10))

idade = int(input('Digite a sua idade: '))

if verificar_maioridade(idade):
    print('Você é maior de idade :) ')
else:
    print('Você é menor de idade')