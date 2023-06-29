"""escribe un programa que calcule el sueldo de un empleado basándose en la cantidad de horas y muestre
por pantalla el resultado, considerando lo siguiente:

a. si trabajo más de 120hs por mes, la hora tiene un valor de $1500.

b. si trabajo entre 80 y 120hs por mes, la hora tiene un valor de $1300.

c. si trabajo menos de 80 horas por mes, la hora tiene un valor de $1100"""

#Ingreso de datos
horas_de_trabajo = int(input("ingrese la cantidad de horas trabajadas en el mes: ")) #horas que trabajo el empledo en el mes

#Calculo de horas trabajadas mayores a 120
if horas_de_trabajo > 120:
    valor_por_hora = 1500 * horas_de_trabajo
    print("Su suedo es de $", valor_por_hora)

#Calculo de horas trabajadas mayores a 80 hasta 120

elif 80 <= horas_de_trabajo <= 120:  
    valor_por_hora = 1300 * horas_de_trabajo
    print("Su sueldo es de $", valor_por_hora)
    
#Calculo de horas trabajadas menores a 80
elif horas_de_trabajo < 80:
    valor_por_hora = 1100 * horas_de_trabajo
    print("Su sueldo es de $", valor_por_hora)


