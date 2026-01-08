from funcoes import saudacao, soma, verificar_maioridade

saudacao('Vinícius')
print(soma(2,10))

idade = int(input('Digite a sua idade: '))

print(f'Maior de Idade' if verificar_maioridade else 'Menor de Idade')