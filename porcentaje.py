ingresos = int(input("ingrese su cantidad de ingreso "))
nivel_educacional = input("ingrese su nivel educacional \n 1) Basico \n 2) Media \n 3) Superior \n --> ")
nacionalidad= input("ingrese su nacionalidad \n A.- CHILENO \n B.- EXTRANJERO \n --> ").upper()

if  500_000 <= ingresos <= 1_000_000 :
    ingresos += 300_000
elif  1_000_000 < ingresos <= 1_500_000: 
    ingresos += 600_000
elif  1_500_001 < ingresos <= 2_000_000:
    ingresos += 900_000

if (nacionalidad.upper()== "A" ):
    ingresos += 300_000 
elif (nacionalidad.upper() == "B"):
    ingresos += 0

if nivel_educacional == "1":
    ingresos *= 1
elif nivel_educacional == "2":
    ingresos *= 1.3
elif nivel_educacional == "3":
    ingresos *= 1.5



print("su puntaje de credito es --> =", ingresos )