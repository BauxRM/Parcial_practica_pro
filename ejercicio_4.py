"""Escribe un programa que calcule el promedio final de una materia, basado en 3 notas de parciales, 
indicando por pantalla si el alumno aprobó o debe recursar la materia (se aprueba con 6)"""

#Ingreso de datos
alumno = 1
acumulador_nota = 0
contador = 0

while alumno <= 3:
    nota = float(input("Ingrese la nota del alumno: "))
    alumno = alumno + 1
    
    #En el caso de que el usuario se equivoque
    if nota < 0 :
        print("¡ERROR! La nota debe ser entre 0 y 10")
        alumno = alumno - 1 
    elif nota > 10 :
        print("¡ERROR! La nota debe ser entre 0 y 10")
        alumno = alumno - 1 
    else:
        acumulador_nota = acumulador_nota + nota

promedio = acumulador_nota / 3 #Promedio del total de notas
    
if promedio >= 6:
    print("¡EL alumno aprobo la materia! su promedio es de: ", promedio)
else:
    print("¡El alumno desaprobo la materia! su promedio es de: ", promedio)

