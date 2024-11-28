#ingresar una vocal e identificar si es o no.
vocal = input('Ingresar una vocal: ').lower()

if vocal == 'a' or vocal == 'e' or vocal == 'i' or vocal == 'o' or vocal == 'u':
    print('Es una vocal.')
else:
    print('No es una vocal. ')