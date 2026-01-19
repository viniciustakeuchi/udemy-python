# lista, exemplos simples de criação e manipulação
frutas = ['Abacate', 'Banana', 'Maça', 'Morango']
print(frutas[0]) # posição do primeiro item, começa com índice 0
frutas.append('Pêssego') # adicionar algum item na lista
print(frutas)
frutas.remove('Pêssego') # removendo item 
print(frutas)
print(len(frutas)) # tamanho da lista usando funçao len()

#programa de gerenciamento de tarefas
tarefas = []

tarefas.append('Estudar Python com IA')
tarefas.append('Ler um artigo sobre IA')
tarefas.append('Responder Emails')

i = 0
for tarefa in tarefas:
    i+=1
    print(f'Tarefa {i}: {tarefa}')


lista1 = [1, 2, 3, 4, 5, 6, 7, 8]
item1, item2, item3, item4, *outros = lista1
print(item1)
print(item2)
print(item3)
print(item4)
print(outros)

valores = [10, 20, 30, 1, 40]
soma = 0
for i in valores:
    soma += i
    if soma > 100:
        print(f'Ultrapassou o valor permitido, o número que parou foi {i}.')
        break
    print(soma)

cor_cliente = input('Digite a cor desejada')
cores = ['amarelo', 'verde', 'azul', 'vermelho']
if cor_cliente.lower() in cores:
    print('Em estoque!')
else: 
    print('Não temos essa cor em estoque')

# Set
list1 = [10, 20, 30, 40, 50]
list2 = [10, 20, 60, 70]

num1 = set(list1)
num2 = set(list2)

print(num1 | num2) # Union: unifica os resultados e tira os repetidos
print(num1 - num2) # Pega o num1 e tira o que tem de igual no num2 
print(num1 ^ num2) # Simmetric Difference: Os valores únicos de cada um, mas sem repetir os numeros
print(num1 & num2) # AND: O que é duplicado entre as listas
print(len(num1))
print(len(num1))

print(type(num1))
list3 = set([1, 2, 3, 4, 5, 6])
s1 = {1, 2, 3, 4, 5, 6}

print(list3)
print(s1)
    
    