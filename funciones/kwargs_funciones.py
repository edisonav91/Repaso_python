print('***Argumentos variables***')
# *args aguments -> tupla
# **kwargs -> keiword arguments, Argumentos en forma de llave

def superheroe_superpoderes(nombre, *args, **kwargs):
    print(f'Superhero: {nombre} - {args} Mas información. {kwargs}')

# Mandar a llamar la funcion

superheroe_superpoderes('Spiderman', 'Instinto aracnido',
                        edad=34, empresa='Marbelle')
superheroe_superpoderes('Iroman', 'Armadura', 'Playboy', edad=45)