#carrito de compra
# Este programa simula un carrito de compras en un supermercado 2.0 
# pide un nombre y luego le da la bienvenida al supermercado 

# nombre = input("ingrese su nombre: ")
# print(f"bienvenido {nombre} al supermercado 2.0")

# def agregar_carrito():
   
#     global carrito 
#     while True:
        
#         op=int(input("ingrese una opcion \n -manjar(1) $3000 \n -cholate(2) $5000 \n -nutella(3) $8000 \n -salir (4) \n --> "))
#         match op:
#             case 1 :
#                 print("usted lleva manjar ")
#                 carrito+=3000
#             case 2 :
#                 print("usted lleva chocolate ")
#                 carrito+=5000
#             case 3 :
#                 print("usted lleva nutella ")
#                 carrito+=8000
#             case 4:
#                 print("saliendo del menu ")
#                 break

#             case _:
#                 print("opcionn invalida")

# carrito=0
# def boleta(nombre): 
#     print(f"hola {nombre} le mostrare su boleta ")
#     print(f"su total de compra es {carrito} ")

# def boleta_iva(nombre):
#     print(f"hola {nombre} su boleta con iva es: ")
#     print(f"su boleta con iva es:{round(carrito*1.19)} ")


# while True:

#     op=int(input (''' ingrese una opcion
#         -carrito (añadir al carro productos ) (1)
#         -boleta (2)
#         -boleta con iva (total) (3)
#         -salir (4)
#         --> '''))

#     match op: 
#         case 1 :
#             print("carrito de compra, escoja los productos que llevara ")
#             agregar_carrito()
#         case 2 :
#             print("boleta ")
#             boleta(nombre)
#         case 3 : 
#             print("boleta iva : ")
#             boleta_iva(nombre)
#         case 4 :
#             print("saliendo del menu...")
#             break
            
#         case _:
#             print("opcion invalida, por favor intente de nuevo")

# pida al usuario cantidad de alumnos 
# pida notas por cada alumno 
# promediar a cada alumno 
# y mostrar si aprueba o reprueba 
# bonus, mostrar promedio de todos los alumnos ingresados 

cantidad_alumnos = int(input("ingrese la cantidad de alumnos que desea promediar "))
suma_prom=0

for i in range (cantidad_alumnos):

    print(f"alumno {i+1}")   
    suma_prom=0 
    notas=int(input("ingrese la cantidad de notas del alumno "))
    for j in range(notas): 
        print(f"notas {j+1} >")
    sum_notas=float(input("ingrese sus notas que desea promediar "))    
    suma_prom = sum_notas/cantidad_alumnos
    if suma_prom >= 4.0 :
        print ("usted reprobo la materia ")
    elif suma_prom < 4.0:
        print ("FELICIDADES!! Usted aprobo la materia ")

