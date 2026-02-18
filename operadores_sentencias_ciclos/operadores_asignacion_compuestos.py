print('*** Operadores de asignación compuestos ***')    
a, b = 10, 15
print(f'Valor inicial de a: {a}')
print(f'Valor inicial de b: {b}')

#Operadosr compuesto de suma +=
a += b
print(f'Valor de a después de a += b: {a}')

#Operador compuesto de resta -=

a = 10 # Reiniciamos el valor de a para la siguiente operación
a -= b
print(f'Valor de a después de a -= b: {a}')

#Operador compuesto de multiplicación

a = 10 # Reiniciamos el valor de a para la siguiente operación
a *= b
print(f'Valor de a después de a *= b: {a}') 

#operador compuesto de división

a = 10 # Reiniciamos el valor de a para la
b = 5 # Cambiamos el valor de b para evitar división por cero 
a /= b
print(f'Valor de a después de a /= b: {a}')