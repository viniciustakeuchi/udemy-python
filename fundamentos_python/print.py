# entrada de dados
nome = input('Digite o seu nome: ')
idade = int(input('Digite a sua idade: '))
print(type(idade))
fruta_favorita = input('Digite a sua fruta favorita: ')

# print com f-string 
print(f'Olá {nome}, daqui 10 anos você terá {idade + 10} de idade e sua fruta favorita é {fruta_favorita} eu imagino rs')

mensagem = 'Olá meu nome é Vinícius'
# Tudo minúsculo
print(mensagem.lower())
# Mostra o index
print(mensagem.find('V'))
# Muda a palavra
print(mensagem.replace('Vinícius', 'Roberto'))
nome = 'Ana'
mensagem2 = f'    Ola, meu nome é {nome}'

# Divide um string por lista de substrings 
print(mensagem2.split())
# Saída: ['Ola,', 'meu', 'nome', 'é', 'Ana']

# Remove os espaços do início
print(mensagem2.strip())







'''
Aqui eu posso escrever varias linhas de comentários
'''
