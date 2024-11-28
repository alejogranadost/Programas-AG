'''Programa que tenga dos listas, cree las listas (sin repeticiones): 
1. Lista de palabras que aparecen en las dos listas.
2. lista de palabras que aparecen en la primera lista, pero no en la segunda.
3. lista de palabras que aparecen en la segunda lista, pero no en la primera.
4. lista de palabras que aparecen en ambas listas.
'''

''' MI SOLUCION!!!
lista1 = ['Alejo', 'Andrea', 'Manuel', 'Victoria']
lista2 = ['Oscar', 'Fabiola', 'Alejo', 'Andrea']

lista3 = list(set(lista1 + lista2))

print(f'La lista que incluye las dos listas: {lista3}')

lista4 = list(set(lista1))

print(f'La lista 1: {lista4}')

lista5 = list(set(lista2))

print(f'La lista 2: {lista5}')

lista6 = set(lista1)
lista7 = set(lista2)
#lista6 = lista1 & lista2
#print(type(lista7))
lista8 = lista6 & lista7
print(f'La lista de elementos comunes: {lista8}')

'''

#SOLUCION ATS

lista1 = [1,2,3,4,5,4,3,2,2,1,5]
lista2 = [4,5,6,7,8,4,5,6,7,7,8]

# Elimine los elementos repetidos de las listas.
a = set(lista1)
b = set(lista2)

union = list(a | b)
soloa = list(a - b)
solob = list(b - a)
interseccion = list( a& b)

print(f'Elementos de las dos listas: {union}')
print(f'Elementos de a: {soloa}')
print(f'Elementos de b: {solob}')
print(f'Elementos que comparten las listas: {interseccion}')
