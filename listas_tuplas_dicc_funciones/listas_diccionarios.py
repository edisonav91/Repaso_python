print("***Listas y diccionarios en python***")

personas = [ {'nombre':'Edison','apellido':'Alvarez', 'edad':'34'}, 
           {'nombre': 'Anderson','apellido':'Alvarez', 'edad':'34'}]

print(personas)

#acceder a un diccionario a sus indices que son Anderson y Edison
print(personas[0])
print(personas[1])

#Acceder a un valor (llave) nombre del primer elemento

print(personas[0].get('nombre'))

# Vamos a recorre cada elemnto de la lista (Cada elemento es un diccionario

for contador, persona in enumerate(personas):
    print(f'persona: {contador}: {persona.get('nombre')}')