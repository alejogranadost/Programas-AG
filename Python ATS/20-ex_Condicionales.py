#pedir 2 numero y decir cual es par.
n1 = int(input('Ingrese el primer numero: '))
n2 = int(input('Ingrese el segundo numero: '))

if n1 % 2 == 0:
    print(f'El primer numero {n1}es par. ')
else:
    print(f'El primer numero {n1}es impar. ')

if n2 % 2 == 0:
    print (f'El Segundo numero {n2}es par. ')
else:
    print(f'El segundo numero es {n2}impar. ')