"""Escribe un programa solicite y muestre por pantalla el nombre, apellido y edad de 5 personas"""

#Ingreso de datos
persona = 1

while persona <= 5:
    
    #Acumulador
    persona = persona + 1 
    
    #Datos de la persona
    nombre = input("Ingrese el nombre: ") 
    apellido = input("Ingrese el apellido: ")
    edad = int(input("Ingrese la edad: "))
    
    # En caso de que el usuario ingrese numero negativo
    if edad < 0 :
        print("¡ERROR!")
        persona = persona - 1
        
    elif edad >= 0 :      
        print("- Nombre: ", nombre) 
        print("- Apellido: ", apellido)
        print("- Edad: ", edad)
    
   