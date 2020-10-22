"""
Ejercicio 02

finanzas personales (ingresos y egresos)

hacer un programa python para consola que le permita al usuario:

1. iniciar un proyecto de finanzas personales con cuenta a 0.00
2. dar opcion para registrar un ingreso o un egreso
3. si es un ingreso sumarlo a la cuenta
4. si es un egreso restarlo a la cuenta
5. verficar que si es un egreso y la cuenta esta a 0.0 debe aparecer
    el monto en negativo.
6. poder generar un reporte de todos los ingresos
7. poder generar un reporte de todos los egresos
8. poder generar un reporte de todas las transacciones (ingresos y egreso)
9. poder generar un reporte solo de el total de la cuenta

restricciones del ejercicio:
el proyecto finanzas debe ser una clase, un ingreso debe ser una clase
y un egreso debe ser una clase tambien.

"""

from Class import (ProyectoFinanzas, Ingresos, Egresos)

result1 = 0.0
resultIngresoT = []
resultEgresoT = []

while True:
    print("Bienvenido a su Programa de Finanzas")
    print("1. Monto que desea ingresar")
    print("2. Monto que desea egresar")
    print("3. Ingresos efectuados")
    print("4. Egresos efectuados")
    print("5. Reporte transacciones: ingresos y egresos")
    print("6. Saldo de la cuenta")
    print("0. Abandonar el Programa de Finanzas")
    selection = int(input("Seleccione una opcion "))
    
    if selection==1:
        #Ingresar el valor del monto que se desea depositar
        Ingreso = float(input("Monto que desea ingresar $"))
        #Lista ingresos efectuados
        resultIngresoT.append(Ingreso)
        #Metodo Class
        Ingreso1 = Ingresos(Ingreso)
        resultIngreso = Ingreso1.sumIngresos()
        #Suma del monto a la cuenta 
        result1 = result1+resultIngreso
        print(f"El saldo de la cuenta es de $ {result1}")

    elif selection==2:
        #Ingresar el valor del monto que se desea retirar
        Egreso = float(input("Monto que desea egresar $"))
        #Lista egresos efectuados 
        resultEgresoT.append(Egreso)
        #Metodo Class
        Egreso1 =  Egresos(Egreso)
        resultEgreso = Egreso1.nuevoEgreso()
        #Suma del monto a la cuenta 
        result1 = result1+resultEgreso
        print(f"El saldo de la cuenta es de $ {result1}")

    elif selection==3:
        #Para obtener el reporte de ingresos 
        for iterator in resultIngresoT:
            print(iterator)

    elif selection==4:
        #Para obtener el reporte de egresos 
        for iterator in resultEgresoT:
            print(iterator)
    
    elif selection==5:
        #Para obtener el reporte de transacciones de ingresos y egresos
        print("Reporte de ingresos")
        for iterator in resultIngresoT:
            print(iterator)
        print("Reporte de egresos")
        for iterator in resultEgresoT:
            print(iterator)     

    elif selection==6:
        #Para obtener el saldo total de la cuenta
        print(f"La cuenta tiene un saldo total de ${result1}")

    elif selection==0:
        #Para salir del programa 
        break