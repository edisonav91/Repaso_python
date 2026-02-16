print ('***Operador and en Python***')
condicion_1 = True
condicion_2 = True
#Aplicamos el operador and para evaluar ambas condiciones

resultado = condicion_1 and condicion_2

print(f'el resultado es : {resultado}')

# Si cualquiera de las condiciones es falsa el resultado será falso

# if else con operador and
llueve = False
nublado = False
if llueve and nublado:
    print('llevar paraguas e impermeable')
elif llueve:
    print('llevar paraguas')
elif nublado:
    print('Llevar impermeable')
else:
    print('No es necesario llevar nada')