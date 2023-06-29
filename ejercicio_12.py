"""Escribe un programa que permita ingresar las edades de las personas, hasta que el usuario decida no 
hacerlo más, y muestre, al final, un promedio de las edades ingresadas y el total de personas ingresadas"""


contador_personas = 0
suma_edades = 0
persona = 1

#Ingreso de edad de las personas
while persona == 1:
    ingreso_edad = input("Ingrese la edad de una persona (Escriba listo para detenerse): ")
    
    if ingreso_edad == "listo": #Escribiendo "listo" y presionando "enter" el usuario decide cuando finalizar
        persona = 0
    else:
        edad = int(ingreso_edad)
        suma_edades = suma_edades + edad #acumulador
        contador_personas = contador_personas + 1 #contador

if contador_personas > 0: 
    promedio = suma_edades / contador_personas #Promedio de edades
    print("Promedio de edades:", promedio)

print("Total de personas ingresadas:", contador_personas)