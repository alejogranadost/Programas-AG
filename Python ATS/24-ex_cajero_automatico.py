#un cajero que simule un saldo inicial de 1000 opciones, ingresar dinero, retirar, mostrar disponible, salir.
saldo = 1000

accion = input('Escoge la opcion que deseas: \n(I) Ingresar dinero. \n(R) Retirar dinero. \n(M) Mostrar saldo. \n(S)Salir. \n').upper()
if accion == 'I':
    ingresar = float(input('Monto a ingresar: '))
    saldo = saldo + ingresar
    print(f'Su monto es: {saldo}')
elif accion == 'R':
    retirar = float(input('Monto a retirar: '))
    saldo = saldo - retirar
    print(f'Su monto es: {saldo}')
elif accion == 'M':
    print(f'Su monto es: {saldo}')
elif accion == 'S':
    print('Hasta una proxima. ')
else:
    print('La opcion no es valida. ')