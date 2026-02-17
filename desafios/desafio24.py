cidades = ('São Paulo', 'Rio de Janeiro', 'Belo Horizonte')

cidade_usuario = input('Digite o nome de uma cidade: ')

if cidade_usuario in cidades:
    print(f'{cidade_usuario} está na lista de cidades.')
else:
    print(f'{cidade_usuario} não está na lista de cidades.')