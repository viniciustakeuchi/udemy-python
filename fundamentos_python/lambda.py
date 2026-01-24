# Função pequena sem nome
# Pode ter vários argumentos mas somente uma expressão
# Muito utilizada dentro de outras funções
# Código mais clean

def somar(x):
    func2 = lambda x: x + 10
    return func2(x) + 10
print(somar(2))

#Função lambda
somar10 = lambda x, y: x + y + 10
print(somar10(2, 4))