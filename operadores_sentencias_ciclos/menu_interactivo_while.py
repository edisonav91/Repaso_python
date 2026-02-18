print ('***Menu interactivo con while***')

print('Sistema de administracion de cuentas ***')

salir = False
while not salir: #Logica de negacion, mientras no se cumpla la condicion de salir, el programa seguira ejecutandose
    print(f'''Menu:
        1. Crear cuanta
        2.Eliminar cuenta
        3. salir''')
    opcion = int(input('Escoge una opcion: '))
    if opcion ==1:
        print('Creando tu cuenta...\n')
    elif opcion ==2:
        print('Eliminando cuenta...\n')
    elif opcion == 3:
        print('Saliendo del sistema.Vuelva pronto... \n')
        salir = True
    else:
        print('Opcion invalida, selecciona otra opcion... \n')