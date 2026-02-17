# Ponto da carne

temperatura = int(input("Digite a temperatura da carne: "))

if temperatura < 48:
    print("Assar mais um pouco")
elif 48 <= temperatura < 54:
    print("Selada")
elif 54 <= temperatura < 60:
    print("Ao ponto para mal")
elif 60 <= temperatura < 65:
    print("Ao ponto")
elif 65 <= temperatura < 71:
    print("Ao ponto para bem")
elif temperatura >= 71:
    print('Bem passada')
else:
    print("Temperatura inválida")