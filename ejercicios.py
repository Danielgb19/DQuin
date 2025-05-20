# #carrito de compra
# # Este programa simula un carrito de compras en un supermercado 2.0 
# # pide un nombre y luego le da la bienvenida al supermercado 

# # nombre = input("ingrese su nombre: ")
# # print(f"bienvenido {nombre} al supermercado 2.0")

# # def agregar_carrito():
   
# #     global carrito 
# #     while True:
        
# #         op=int(input("ingrese una opcion \n -manjar(1) $3000 \n -cholate(2) $5000 \n -nutella(3) $8000 \n -salir (4) \n --> "))
# #         match op:
# #             case 1 :
# #                 print("usted lleva manjar ")
# #                 carrito+=3000
# #             case 2 :
# #                 print("usted lleva chocolate ")
# #                 carrito+=5000
# #             case 3 :
# #                 print("usted lleva nutella ")
# #                 carrito+=8000
# #             case 4:
# #                 print("saliendo del menu ")
# #                 break

# #             case _:
# #                 print("opcionn invalida")

# # carrito=0
# # def boleta(nombre): 
# #     print(f"hola {nombre} le mostrare su boleta ")
# #     print(f"su total de compra es {carrito} ")

# # def boleta_iva(nombre):
# #     print(f"hola {nombre} su boleta con iva es: ")
# #     print(f"su boleta con iva es:{round(carrito*1.19)} ")


# # while True:

# #     op=int(input (''' ingrese una opcion
# #         -carrito (añadir al carro productos ) (1)
# #         -boleta (2)
# #         -boleta con iva (total) (3)
# #         -salir (4)
# #         --> '''))

# #     match op: 
# #         case 1 :
# #             print("carrito de compra, escoja los productos que llevara ")
# #             agregar_carrito()
# #         case 2 :
# #             print("boleta ")
# #             boleta(nombre)
# #         case 3 : 
# #             print("boleta iva : ")
# #             boleta_iva(nombre)
# #         case 4 :
# #             print("saliendo del menu...")
# #             break
            
# #         case _:
# #             print("opcion invalida, por favor intente de nuevo")

# ##########################################################################################################

# # pida al usuario cantidad de alumnos 
# # pida notas por cada alumno 
# # promediar a cada alumno 
# # y mostrar si aprueba o reprueba 
# # bonus, mostrar promedio de todos los alumnos ingresados 

# # cantidad_alumnos = int(input("ingrese la cantidad de alumnos que desea promediar "))
# # suma_prom=0

# # for i in range (cantidad_alumnos):

# #     print(f"alumno {i+1}")   
# #     suma_prom=0 
# #     notas=int(input("ingrese la cantidad de notas del alumno "))
# #     for j in range(notas): 
# #         print(f"notas {j+1} >")
# #     sum_notas=float(input("ingrese sus notas que desea promediar "))    
# #     suma_prom = sum_notas/cantidad_alumnos
# #     if suma_prom >= 4.0 :
# #         print ("usted reprobo la materia ")
# #     elif suma_prom < 4.0:
# #         print ("FELICIDADES!! Usted aprobo la materia ")

# #############################################################################################################
#aqui vemos como try y axcept funcionan base al error es decir si escribes algun numero con letras 
#te arroja el error pero el programa no se caera.

# while True:
#     try:
#         op=float(input("ingrese un numero ->"))
#         break
#     except:
#         print("debe ingresar solo numeros ")
################################################################################################################
# mandamos una cantidad de perros a cazar y 

# import time
# import random

# while True:
#     try:
#         perros=int(input("ingrese la cantidad de perros > "))
#         break
#     except ValueError:
#         print("!ERROR! debes ingresar un numero entero ")
    
# resumen=[]
# for i in range(perros):
#     print(f"han salido a casar estos perros :{perros} ")
#     i+1
    
#     print(f"el perro numero {i+1} salio a cazar conejos ")
#     conejo=random.randint(1,10)
#     if conejo<=3:
#         print(f"el perro numero: {i} se queda sin filete" )
#         resumen.append(f"el perro {i+1} el perro no cumplio ")
#     elif conejo>=4:
#         print(f"el perro numero: {i} cumplio con la caza " )
#         resumen.append(f"el perro {i+1} el perro cumplio ")

# print( "\nresumen:")
# for r in resumen:
#     time
#     print(r)

###################################################################################################################
#try
#lavado de autos
#crear un menupara lavar autos 
#match 
#1.-cursar pago del lavado 
#2.- ver ventas diarias 
#3.-salir 
#el lavado tiene 3 niveles
# while true  
#1.-full $15000, 2.-standart $10000, 3.- basico $7000.
#el mostrar las ventas diarias, debe mostrar la 
#cantidad de autos que han ingresado y el monto total
#recaudado. tambien debe mostrar el monto mas alto pagado 
#except