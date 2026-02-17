num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

multiplicacao = lambda x, y: x * y
print(f'A multiplcação de {num1} e {num2} é: {multiplicacao(num1, num2)}')