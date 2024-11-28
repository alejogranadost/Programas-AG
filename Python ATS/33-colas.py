# Colas. ex: fi-fo (first input - first output.)

cola = ['Maria', 'Alejandro', 'Jose', 'Mario']
# Agregamos elementos al final de la cola.
cola.append('Karla')
cola.append('Flor')

print(cola)

#Sacando elementos por el principio.
n = cola.pop(0)
print(f'Atendiendo a {n}')

n = cola.pop(0)
print(f'Atendiendo a {n}')
print(cola)