"""Escribe un programa que solicite y muestre por pantalla nombre, apellido y edad de una cantidad de 
personas ingresada por el usuario."""

#Ingreso de datos
cantidad_personas = int(input("Ingrese la cantidad de personas: "))
contador = 0

while contador < cantidad_personas:
    contador = contador + 1
    print("Persona", contador)
    
#Datos ingresados por el usuario
    nombre = input("Ingrese el nombre: ")
    apellido = input("Ingrese el apellido: ")
    edad = int(input("ingrese la edad: "))
    
    if edad < 0 :
        print("¡ERROR!")
        contador = contador - 1 
        
    elif edad >= 0 :
        print("- Nombre: ", nombre)
        print("- Apellido: ", apellido)
        print("- Edad: ", edad)