print('***Operador or en Python***')
condicion_1 = False
condicion_2 = False
# El operador or solo devuelve positivo si alguna de las condiciones es verdadera
#Aplicamos el operador or para evaluar ambas condiciones
resultado = condicion_1 or condicion_2
print(f'Resultado {condicion_1} or {condicion_2}  es = {resultado}')

# Camilo quiere asistir a si hijo a verlo jugar 
descanso = False
vacaciones = True
if descanso or vacaciones:
    print('Camilo va a asistir al juego de su hijo')
elif descanso:
    print('Camilo va a asistir al juego de su hijo')
elif vacaciones:
    print('Camilo va a asistir al juego de su hijo')
else:
    print('Camilo no va a asistir al juego de su hijo')