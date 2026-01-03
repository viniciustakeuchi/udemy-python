usuario = {
    'nome': 'Vinícius',
    'idade': 22,
    'Departamento': 'TI',
}
#Modificando o valor do dicionario
usuario['idade'] = 30
usuario['Cidade'] = 'São Paulo'

print(usuario)

#Pedindo as infos para o usuário no dicionário
aluno = {
    'nome': input('Nome do Aluno'),
    'idade': int(input('idade do Aluno')),
    'nota': float(input('nota do Aluno'))
}

print(f'O {aluno['nome']}, tem {aluno['idade']} e tirou {aluno['nota']}  no exame')

# Outro exemplo
profissional = {
    'nome': input('Digite o seu nome: '),
    'idade': int(input('Digite a idade: ')),
    'profissão': input('Digite sua profissão: ')
}

print(f'O {profissional['nome']} tem {profissional['idade']} anos e sua profissão é {profissional["profissão"]}')