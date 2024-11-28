#Conjuntos, se ponen entre {}
#conjunto = set()
#si no le ponemos el set al conjunto VACIO!!!, python se puede confundir y pensar que es un diccionario.
#No puede tener valores duplicados
#conjunto = {1,2,3,'hola',4,56}
'''
conjunto.add(5)
conjunto.discard(3)
#conjunto.clear()


print(conjunto)
'''
# Conjuntos parte 2

a = {1,2,3}
b = {3,4,5}



#c = a | b Union del conjunto.
#c = a & b  Interseccion
#c = a - b  Diferencia y muestra el resultado de a
#c = b - a Diferencia y muestra el resultado de b
#c = a ^ b  Diferencia simetrica.

c = {1,2,3,4,5}
print(a.issubset(c))