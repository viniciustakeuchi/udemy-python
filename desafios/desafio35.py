num = int(input("Digite um número para calcular o quadrado: "))
eleva_quadrado = lambda x: x ** 2
print(f"O quadrado de {num} é: {eleva_quadrado(num)}")

lista = [1, 2, 3, 4, 5]
for n in lista:
    quadrados = list(map(eleva_quadrado, lista))
    print(f"Os quadrados dos números na lista são: {quadrados}")
    break