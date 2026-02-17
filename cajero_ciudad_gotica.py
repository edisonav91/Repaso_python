print('***Cajero automatico de ciudad Gotica')
saldo = 1000 #Saldo inicial
salir = False
while not salir:
    print(f'''Operaciones que puedes realizar
        1. Consultar saldo
        2. Retirar 
        3. depositar
        4. Salir''')
    opcion = int(input('Escoge una opcion:'))
    if opcion == 1:
        print(f'Su saldo es: {saldo}')
    elif opcion == 2:
        retirar = float(input('Ingrese el saldo a retirar: '))
        # Validacion    
        if retirar <= saldo:
            saldo -= retirar
            print(f'Su saldo actual es : {saldo}')
    elif opcion == 3:
        deposito = float(input('Ingrese el monto a depositar: '))
        saldo += deposito
        print(f'Su saldo actual es : {saldo}')
    elif opcion == 4:       
        salir = True
        print('Saliendo del sistema, Vuelva pronto...')
    else:
        print(f'Opcion invalida seleccione otra...')



        
    
