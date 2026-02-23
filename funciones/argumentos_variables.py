print('***Argumentos variables***')

def superheroe_superpoderes(nombre, *args):
    print(f'Superheroe: {nombre} - {args}')

# Mandar a llamar la funcion

superheroe_superpoderes('Spiderman', 'Instinto aracnido', 'Teleraña', 'Trepador')
superheroe_superpoderes('Iroman', 'Armadura', 'Playboy', 'Millonario')