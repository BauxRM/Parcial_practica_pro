"""Escribe un programa que calcule la equivalencia a pesos de los dólares ingresados por pantalla. El 
programa debe preguntar el tipo de cambio a convertir (es decir, cuánto cotiza el dólar)"""

#Bienvenida
print("¡Hola! ¿Necesitas ayuda para cambiar tus dolares?")

#Ingreso de datos por el usuario
dolares = int(input("Ingrese la cantidad de dolares que quiere cambiar: "))
pesos = int(input("Ingrese el tipo de cambio al que quiere cambiar los dolares: "))

#Calculo de cambio de dolares a pesos
tipo_de_cambio = dolares * pesos
print("La equivalencia de sus dolares es de $", tipo_de_cambio, "pesos")
