
usuario = input('Digite o seu usuário: ')
senha = input('Digite a sua senha: ')
login_valido = usuario == 'Admin' and senha == '123admin'

print(f'Login Permitido: {login_valido}')