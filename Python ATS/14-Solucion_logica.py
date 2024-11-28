'''a = float(input('Ingrese valor de a: '))
b = float(input('Ingrese valor de b: '))

solucion = ((3+5*8) < 3 and ((-6/3)*4+2 < 2)) or (a>b)
print(f'El resultado es: {solucion}')

a1 = float(input('Ingrese el valor de a: '))
b1 = float(input('Ingrese el valor de b: '))

a2 = b1
b2 = a1

print(f'El nuevo valor de a es: {a2}, y el nuevo valor de b es: {b2}')
'''
a = float(input('Ingrese el valor de a: '))
b = float(input('Ingrese el valor de b: '))

a, b = b, a
print(f'El nuevo valor de a es: {a}, y el nuevo valor de b es: {b}')