''' 
Muito utilizado com Listas
Aplicar uma função a um Iterable, por item. (list, tuple, dic etc.)
'''



# def multi(x):
 #   return x * 2
#lista2 = map(lambda x: x * 2, lista1)
lista1 = [1, 2, 3, 4]
print(list(map(lambda x: x * 2, lista1)))

lista2 = [10, 20, 30, 40, 50]
print(list(map(lambda x: x + 10, lista2)))

lista3 = [2, 3, 4, 5]
print(list(map(lambda x: x ** 2, lista3)))



