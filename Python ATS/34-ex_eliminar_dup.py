#Escriba una lista donde tenga elementos repetidos y por ultimo mostrar la lista.

'''
lista = [1,2,3,4,5,5,6,7,4,3,2,1]
#convertirla en conjunto, para eliminar los elementos duplicados.
conjunto = set(lista)
#el conjunto se devuelve a lista
lista = list(conjunto)

print(conjunto)
'''

lista = [1,2,3,4,5,5,6,7,4,3,2,1]

lista = list(set(lista))

print(lista)