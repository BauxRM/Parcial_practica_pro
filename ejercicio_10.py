"""Escribe un programa que calcule el promedio general de una clase."""

#Ingreso de datos
alumnos = int(input("Ingrese la cantidad de alumnos: "))

contador = 0
acumulador_de_notas = 0

while contador < alumnos:
    contador = contador + 1
    
#Datos ingresados por el usuario
    nota = float(input("ingrese la nota: "))

#En caso de que la persona se equivoque al escribir la nota
    if nota < 0 :
        print("¡ERROR! La nota debe ser entre 0 y 10")
        contador = contador - 1 
    elif nota > 10 :
        print("¡ERROR! La nota debe ser entre 0 y 10")
        contador = contador - 1 
    else:
        acumulador_de_notas = acumulador_de_notas + nota

        promedio_general = acumulador_de_notas / alumnos 

#Muesta en pantalla
print("El promedio general de la clase es de:", promedio_general)       
