#Bucle for
'''
for i in [1,2,3,4,5]:
    print('Hola mundo')
'''

'''
coleccion = [1,2,3,4,5]
for i in coleccion:
    print('Hola mundo')
'''
'''
coleccion = [1,2,3,4,5]
for i in coleccion:
    print(f'Elemento; {i}')
'''
'''
coleccion = {'Alejo':22,'Maria':23,'Jose':45, 'Luis':12}

for i in coleccion:
    print(f'{Elemento; {i}}')
'''
'''
coleccion = {'Alejo':22,'Maria':23,'Jose':45, 'Luis':12}

for i in coleccion:
    print(f'{coleccion[i]}')
'''
'''
coleccion = {'Alejo':22,'Maria':23,'Jose':45, 'Luis':12}

for i in coleccion:
    print(f'{i} -> {coleccion[i]}') 
'''
'''
#La mejor manera de mostar clave y valor de un diccionario.
coleccion = {'Alejo':22,'Maria':23,'Jose':45, 'Luis':12}

for clave,valor in coleccion.items():
    print(f'{clave} -> {valor}') 

coleccion = {'Alejo':22,'Maria':23,'Jose':45, 'Luis':12}
'''
'''
coleccion = 'Alejandro'
for i in coleccion:
    print(f'{i}') 
'''
# Si quiero que muestre las letras del nombre sin saltar de linea:
coleccion = 'Alejandro'
for i in coleccion:
    print(f'{i}' , end='-') 