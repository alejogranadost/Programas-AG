'''
Escriba un programa donde cree una lista con los siguientes personajes del señor de los anillos:
1 Nombre: Aragorn
Clase: Guerrero
Raza: Dunadan del Norte.

2 Nombre: Gandalf
Clase: Mago
Raza: Istar

3 Nombre: Legolas
Clase: Arquero
Raza: Elfo Sindar
'''

#Diccionario.
'''
personajes = {'Aragorn':['guerrero','Dunadan del Norte'],'Gandalf':['Mago','Istar'],'Legolas':['Arquero','Elfo Sindar']}

lista = list(personajes)

print(personajes)
'''

#Solucion ATS
personajes = [] #Creando una lista vacia.

p = {'Nombre':'Aragorn','Clase':'Guerrero','Raza':'Dunadan del Norte'}

personajes.append(p) # Agregamos a la lista el personaje

p = {'Nombre':'Gandalf','Clase':'Mago','Raza':'Istar'}

personajes.append(p)

p = {'Nombre':'Legolas','Clase':'Arquero','Raza':'Elfo Sindar'}

print(personajes)