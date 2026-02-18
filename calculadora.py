print('***Calculadora reto python***')

salir = False

while not salir:
    print('''Operaciones que puede realizar
      1. Suma
      2. Resta
      3. Multiplicacion
      4. Division
      5. Salir''')

    opcion = int(input('Escoge una opcion...'))
    resultado = 0

    numero_1 = int(input('Ingrese su primer numero: '))
    numero_2 = int(input('Ingrese su segundo numero: '))

    if opcion == 1:
        resultado = numero_1 + numero_2
        print(f'Resultado de suma es: {resultado}')

    elif opcion == 2:
        resultado = numero_1 - numero_2
        print(f'El resultado de la resta es: {resultado}')

    elif opcion == 3:
        resultado = numero_1 * numero_2
        print(f'El resultado de la multiplicación es: {resultado}')

    elif opcion == 4:
        if numero_2 != 0:
            resultado = numero_1 / numero_2
            print(f'Resultado de división es: {resultado}')
        else:
            print('No se puede dividir entre 0')

    elif opcion == 5:
        salir = True
        print('Saliendo de la calculadora, vuelva pronto...')

    else:
        print('Opcion equivocada...')

    
    
    
