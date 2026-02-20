print ('Regresar una tupla de valores desde una funcion')

#Definicion de la funcion

def persona_mayuscula(nombre, apellido, edad):
    print('Esta funcion va a regresar los valores en Mayusculas tupla()')
    return nombre.upper(), apellido.upper(), edad

# programa principal-desempaquetar la misma cantidad de valores que hay en la funcion
nombre, apellido, edad = persona_mayuscula('Anderson', 'Alvarez', 34)
print(f'Persona: nombre = {nombre} apellido = {apellido} edad = {edad}')