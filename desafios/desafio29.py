def potencia(base, expoente):
    return base ** expoente

num_base = int(input("Digite a base: "))
num_expoente = int(input("Digite o expoente: "))
if not num_expoente > 0:
    num_expoente = 2

resultado = potencia(num_base, num_expoente)
print(f'{num_base} elevado a {num_expoente} é {resultado}.')