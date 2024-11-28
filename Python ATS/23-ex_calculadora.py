#Crear una calculadora de suma, resta, multiplicacion o division.

n1 = float(input('Ingrese el n1: '))
n2 = float(input('Ingrese el n2: '))

operacion = input('Ingrese suma (s), resta (r), multiplicacion(m), division (d): ').lower()
if operacion == 's':
    suma = n1 + n2
    print(f'Suma = {suma:.2f}')
elif operacion == 'r':
    resta = n1 - n2
    print(f'Resta = {resta:.2f}')
elif operacion == 'm':
    multiplicacion = n1 * n2
    print(f'Multiplicaion = {multiplicacion:.2f}')
elif operacion == 'd':
    division = n1 / n2
    print(f'Division = {division:.2f}')
else:
    print('Opcion no disponible. ')