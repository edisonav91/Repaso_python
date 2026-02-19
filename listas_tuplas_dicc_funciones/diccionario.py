print('***Manejode diccionarios***')

# Un diccionario almacena los elementos en forma de 
# clave: valor, ademas no se pueden duplicar sus elementos

diccionario = {'nombre':'Edison', 
               'apellido':'Alvarez',
               'edad':'34',  # Este valor se omite
               'edad': '35'} # Nos quedamos con el ultimo valor definido
print(diccionario)

#Acceder a elementos

print(f' nombre: {diccionario ["nombre"]}')
print(f' apellido: {diccionario ["apellido"]}')
print(f' edad: {diccionario.get("edad")}')

# El largo de un diccionario o cantidad de elementos

print(f'Largo del diccionario: {len(diccionario)}')

#Agregar nuevos elementos

diccionario['Telefono'] = 3012545151

print(f'Diccionario actualizado: {diccionario}')

# Obtener la lista de las llaves del diccionario

print(f' Listado de las llaves de diccionario: {diccionario.keys()}')

# Obtener la lista de los valores del diccionario

print(f'Lista de los valores de diccionario: {diccionario.values()}')

#Obtener los elementos del diccionario (items)

print(f'Recuperar los elemntos de un diccionario: {diccionario.items()}')

#Revisar si una llave existe

llave_buscar = 'nom'

if llave_buscar in diccionario:
    print(f'La llave a buscar {llave_buscar} si esta')
else:
    print(f'La llave {llave_buscar} no esta')

# Modificar el valor de una llave

diccionario['edad'] = '36'
print(diccionario)

#Eliminar un elemnto del diccionario pop()

diccionario.pop('nombre')
print(diccionario)

# recorrer las llaves

for llave in diccionario.keys():
    print(llave, end = (' ') )

# Recorrer los valores de value()
print()
for valores in diccionario.values():
    print(valores, end = (' '))

# Recorre los elementos del diccionario como una tupla
print()
for (llave, valor) in diccionario.items():
    print(f'Llave {llave} y valor {valor}')

# Limpiar diccionario clear()

diccionario.clear()
print(diccionario)