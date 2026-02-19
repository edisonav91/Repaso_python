print('***Manejo de set o conjuntos en python***')

# Es un conjunto de datos no ordenados y no se puyede repetir sus elementos

conjunto = {'Karla', 1000, 'Edison', 'Karla', True, 100}

# print(conjunto)

#No se pueden modificar elementos

for interar in conjunto:
    pass
   # print(conjunto, end = ('  '))

numero_buscar = 800

if numero_buscar == 100:
    print(f'Numero que buscabas {numero_buscar} si esta...')
else:
    print(f'Numero a buscar {numero_buscar} no esta')

largo = len(conjunto)
print(f"La cantidad de elementos en mi set es: {largo}") # Length = largo en ingles len()

# Eliminar un elemento del set

conjunto.remove('Edison')
print(conjunto)

# Agregar un nuevo elemento

conjunto.add('Anderson')
print(conjunto)