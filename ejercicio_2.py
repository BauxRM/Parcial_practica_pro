"""Escribe un programa que calcule el área y el perímetro de un cuadrado y muestre los resultados (indicando
cuál es cuál) por pantalla."""

#Ingreso de datos.
lados_del_cuadrado = int(input("Ingrese el valor de los lados del cuadrado: "))

#Calculo 
area = lados_del_cuadrado * 2 #Resultado del area

perimetro = lados_del_cuadrado * 4 #Resultado del perimetro

print("El cuadrado tiene un area de", area, "y un perimetro de", perimetro)