snacks = [
    {'id':0, 'nombre':'Papas', 'precio':30}, 
    {'id':1, 'nombre':'Refresco', 'precio':50}, 
    {'id':2, 'nombre':'Sandwish', 'precio':120}
]

#lista de productos
productos = []

print('***Maquina de Snacks***')

print('Lista de productos')
print('Snacks disponibles: ')
for snack in snacks:
    print(f"\t ID: {snack['id']} "
          f" -> {snack['nombre']} "
          f" - Precio  {snack['precio']}  " )

def maquina_snacks(snacks, productos):
    salir = False
    while not salir:
        print(f'''***Maquina de Snacks***
        1. Comprar snacks
        2. Mostrar Ticket
        3. Salir''')
        opcion = int(input('Selecciones una opción: '))
        if opcion == 1:
            comprar_producto(snacks, productos)
        elif opcion == 2:
            mostrar_ticket(productos)
        elif opcion == 3:
            print("Regresa pronto")
            salir = True
        else: print("Opcion invalida, selecciona otra opcion...\n")
            
def comprar_producto(snacks, productos):
    id_snack = int(input('Que snack quieres (id)?:'))
    productos.append(snacks[id_snack])
    print(f'Snack agregado {snacks[id_snack]}')

def mostrar_ticket(productos):
    ticket = f'\t***Ticket de venta***'   
    total = 0
    for producto in productos:
        ticket += f'\n\t-{producto['nombre']} - ${producto['precio']}'   
        total += producto['precio']
    ticket += f'\n\tTOTAL -> ${total}'
    print(ticket)

# LLamar o invocar 
maquina_snacks(snacks, productos)
    
