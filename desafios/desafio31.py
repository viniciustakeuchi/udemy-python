def dobrar(n):
    return n * 2

def quadrado(n):
    return n ** 2

num = int(input("Digite um número: "))
print(f"O quadrado do dobro do número é: {quadrado(dobrar(num))}")
