# cual es el mayor de 3 numero.

n1 = float(input('Ingrese el valor de n1: '))
n2 = float(input('Ingrese el valor de n2: '))
n3 = float(input('Ingrese el valor de n3: '))

if n1 > n2 > n3 or n1 > n3 > n2:
    print(f'n1 {n1}, es mayor. ')
elif n2 > n1 > n3 or n2 > n3 > n1:
    print(f'n2 {n2}, es mayor. ')
else:
    print(f'n3 {n3}, es mayor. ')