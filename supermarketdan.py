# supermarketdan.py
# Este programa simula un carrito de compras en un supermercado.    


def agregar_carrito():
   
    global carrito 
    while True:
        
        op=int(input("ingrese una opcion \n -manjar(1) $3000 \n -cholate(2) $5000 \n -nutella(3) $8000 \n -salir (4) \n --> "))
        match op:
            case 1 :
                print("usted lleva manjar ")
                carrito+=3000
            case 2 :
                print("usted lleva chocolate ")
                carrito+=5000
            case 3 :
                print("usted lleva nutella ")
                carrito+=8000
            case 4:
                print("saliendo del menu ")
                break

            case _:
                print("opcionn invalida")

carrito=0
def boleta():
    print(f"su total de compra es {carrito} ")

def boleta_iva():
    print(f"su boleta con iva es:{round(carrito*1.19)} ")


while True:

    op=int(input (''' ingrese una opcion
        -carrito (añadir al carro productos ) (1)
        -boleta (2)
        -boleta con iva (total) (3)
        -salir (4)
        --> '''))

    match op: 
        case 1 :
            print("carrito de compra, escoja los productos que llevara ")
            agregar_carrito()
        case 2 :
            print("boleta ")
            boleta()
        case 3 : 
            print("boleta iva : ")
            boleta_iva()
        case 4 :
            print("saliendo del menu...")
            break
            
        case _:
            print("opcion invalida, por favor intente de nuevo")