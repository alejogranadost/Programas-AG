#convertir de Celsius a Fahrenheit y viseversa
grados = input('Ingrese los grados: ')
grados_float = float(grados)
celsius_fahrenheit = input('Si es Celsius "C", si es Fahrenheit "F": ')
celsius_fahrenheit_upper = celsius_fahrenheit.upper()
if celsius_fahrenheit_upper == ('C'):
    print ((grados_float * 9/5) + 32 , 'Fahrenheit.')
elif celsius_fahrenheit_upper == ('F'):
    print ((grados_float -32 ) * 5 /9 , 'Celsius.')
else:
    print('No has ingresado un valor correcto.')
