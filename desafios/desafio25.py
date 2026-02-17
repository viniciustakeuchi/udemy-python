pais = {
    'Brasil': 'Brasília',
    'Argentina': 'Buenos Aires',
    'França': 'Paris',
    'Japão': 'Tóquio',
}

escolha = input('Digite o nome de um país: ')

if escolha in pais:
    print(f'A capital de {escolha} é {pais[escolha]}.')