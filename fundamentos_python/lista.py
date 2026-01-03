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
