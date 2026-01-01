# IF e Else - testes básicos

numero = int(input('Digite um numero: '))

if numero == 10:
    print('Acertou o número')
else:
    print('Errou!')

# Verificao de maior de menor de idade

idade = int(input('Digite a sua idade: '))

if idade >= 18:
    print('maior de idade')
else: 
    print('menor de idade')
    
# Sistema de Notas de um aluno

nota = float(input('Qual foi a sua nota no exame: '))

if nota >= 7:
    print('Você foi aprovado!')
elif nota >=5:
    print('Você está de recuperação')
else:
    print('Você foi reprovado!')
    
# Credencias com if e else

usuario = input('Digite o seu usuário: ')
senha = input('Digite a sua senha: ')
if usuario == 'Admin' and senha == '123admin':
    print('Sucesso! Login Permitido')
else:
    print('Login não autorizado, verifique o usuário ou senha')

# Permite o acesso para maiores de 18 anos só que se você tiver mais do que 16 e for autorizado pelos pais, voce vai receber uma mensagem acesso liberado com autorizaçaõ dos pais se nao acesso negado

idade = int(input('Digite a sua idade: '))
autorizacao = input('Você tem autorização dos pais (y/n)? ')

if idade >= 18:
    print('Você está autorizado para acessar a plataforma!')
elif idade >=16 and autorizacao == 'y':
    print('Acesso liberado com autorização dos pais')
else:
    print('Acesso Negado!')