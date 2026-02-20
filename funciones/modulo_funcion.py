from funciones import saludar 

print('***Modulos y funciones en python***')

 #1. llamamos a la funcion
argumento = input('Ingrese palabra o frase deseada: ')
valor_devuelto = saludar(argumento)
print(f'Valor devuelto de la funcion: {valor_devuelto}')

def saludar(parametro):
    print(f'mensaje recibido {parametro}')
    return 'Aca termina la funcion gracias'

# Modulos basicamente es definir funciones y tambien variables y podemos utilizarlas desde otro archivo
#Ademas de reutlizar codigo y limpiar el codigos