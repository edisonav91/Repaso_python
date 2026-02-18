solicitar_numero = int(input('Ingrese su numero:'))
if solicitar_numero > 0:
    print(f'Es numero {solicitar_numero} positivo')
elif solicitar_numero < 0:
    print(f'El numero {solicitar_numero} es negativo')
else:
    print('es cero')