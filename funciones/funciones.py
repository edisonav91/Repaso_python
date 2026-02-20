print('***Manejo de funciones***')

# 1. Definir la funcion notacion de snake o serpiente

def saludar(parametro):
    print(f'mensaje recibido {parametro}')
    return 'Aca termina la funcion gracias'

# 2. LLamar a la función
argumento = input('Ingrese palabra o frase deseada: ')
valor_devuelto = saludar(argumento)
print(f'Valor devuelto de la funcion: {valor_devuelto}')

saludar(argumento)
# saludar('Saludos') # Reutiolizar una llamada a una fumncion
# saludar('Edison')

