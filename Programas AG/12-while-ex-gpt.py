"""Ejercicio: Juego de adivinanza
Crea un programa en Python que:

Pida al usuario adivinar un número secreto entre 1 y 100.
Use un bucle while para permitir al usuario seguir intentando 
hasta que adivine correctamente.
Dé pistas al usuario después de cada intento indicando 
si el número secreto es mayor o menor que el número introducido.
Felicite al usuario cuando adivine el número y muestre cuántos intentos 
le tomó.
"""

import random
i = random.randint(1,100)
intentos = 0 #Para iniciar la cuenta desde 0

#se imprime el valor solo para hacer testing.
#print(f'{i}')
#pedimos que ingrese un valor entre el rango asignado al numero aleatorio.

while True:
    adivino = input('Ingresa un número entre 1 y 100: ').strip()

    if adivino.isdigit():
        #print(f'Ingresaste {adivino}') 
        break
    else:
        print('No ingresaste un valor valido. ')

adivino = int(adivino)
while i != adivino:
    intentos += 1
    if adivino < 1 or adivino > 100:
        print('Número incorrecto. ')
        #print('Ingresa un valor entre 1 y 100. ')
    elif adivino < i :
        print('El numero es mayor. ')
    elif adivino > i :
        print('El numero es menor. ')
    while True:
        adivino = input('Ingresa un número entre 1 y 100: ')
        
        if adivino.isdigit():
            #print(f'Ingresaste {adivino}') 
            #adivino = int(adivino)
            break
        else:
            print('No ingresaste un valor valido. ')
    adivino = int(adivino)
# Mensaje de felicitación por encontrar el valor
print(f'Lo encontraste el numero era {i}')
#se pone condicional para escritura correcta del singular o plural de ves o veces en intentos.
if intentos + 1 == 1:
    print('Lo intentaste 1 ves.')
else:
    print(f'Lo intentaste {intentos + 1} veces.')