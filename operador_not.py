print('***Operador NOT en Python***')
condicion_1 = True
resultado = not condicion_1
print(f'El resultado de not {condicion_1} es: {resultado}')

# El operador not invierte el valor de la condición, si es verdadera la convierte en falsa y viceversa

print('***Salir del sistema***')
salir = False
if not salir:
    print('El sistema sigue funcionando')
else:    print('El sistema se ha cerrado')