print ('***Manejo de tuplas***')

tupla = ('Karla', 'Juan', 'Laura')

# print(tupla)

# Tupla Heterogea

tupla_heterogenea = 100,
#print(tupla_heterogenea)

# Recorrer los elementos de una dupla
for elementos in tupla:
    pass
    # print(elementos, end=(' - '))

numeros = (100, 200, 300, 400, 500)
print(f'Para el indice cero el valor es = {numeros [-1]}') # Impresion 
print(f'Para el indice cero el valor es = {numeros [3]}') # Impresion 

numero_buscar = 800

if numero_buscar in numeros:
    print (numero_buscar)
else:
    print(f'Numero a buscar {numero_buscar} no se encuentra')