print('***Listas en python***')

nombres = ['Carla', 'Juan', 'Laura']
#print(F'Lista de nombres = {nombres}')

# Tambien podemos tener una lista heterogenea con diferentes tipos de datos

lista_heterogenea = [100, False, 'Edison']
#print(lista_heterogenea)

# Interar o leer cada elemento de la lista
for nombre in nombres:
    #print(nombre, end = ' ') # end = '' para qeu imprima en la misma linea

# Lista de numeros

    numeros = [100, 200, 300, 400, 500]

 #Recuperar valore de indice de una lista

#print(numeros [1])

#print(f' Indice numero 3 de la lista es: {numeros[3]}')


# Modificar los indices de una lista 

numeros[0] = 1000
numeros[1] = 1000

# Preguntar si un valor existe en mi lista
numero = 400
#if numero in numeros:
    #print(f'El numero {numero} si esta en la lista')
#else:
    #print('No existe numero en la lista')

    # Recuperar el indice de un elemento de la lista

#indice = numero.index(numero) # para buscar la posicion del elemento de la lista

numeros = [100, 200, 300, 400, 500]

#valores_recuperados = numeros [:3]

#print(f'numeros recuerdos son {valores_recuperados}') # Recuperar valores de una lista

#Otra forma de recuperar una sublista, colocando el indice inicial

#valores_recuperados = numeros[3:]

#Realiarf una copia 

#copia_lista = numeros[:]        
#print(copia_lista)

# Metodos de listas

largo_lista = len(numeros)
#print(largo_lista)

#agregar un nuevo elemento append. Agrega el nuevo elemento al final

numeros.append(600)

#print(numeros)

# Insertar un valor en indice indicado

numeros.insert(4, 700)
print(f'lista con el nuevo valor {numeros}')

# Eliminar un elemento de la lista utlizaremos remove()

numeros.remove(700)
print(f'Lista con elemento removido 700 = {numeros}')

# Concatenar listas 

lista_concatenada = numeros + lista_heterogenea

print(f'Litas unidas o concatenadas es = {lista_concatenada}')

# Eliminar por indice de una lista

del numero[2]
print(numero)

#Eliminar lista completa

numeros[:] = []

# Eliminar por completo la variable

del numeros
print(numeros)