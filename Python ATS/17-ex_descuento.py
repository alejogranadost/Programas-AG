#tienda ofrece 15% de descuento.
valor = float(input('Ingrese el valor del articulo: $'))
descuento = valor * 0.15
precio_final = valor - descuento
print(f'El valor del articulo es: ${valor}')
print(f'El descuento es: ${descuento:.2f}')
print(f'El valor final es: ${precio_final:.2f}')