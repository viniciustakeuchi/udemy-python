num = int(input('Digite um número: '))

lambda_par = lambda x: x % 2 == 0
if lambda_par(num):
    print(f'O número {num} é par.')
else:    
    print(f'O número {num} é ímpar.')