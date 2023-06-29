"""Del punto anterior, y considerando que durante 12 meses el empleado trabajó las mismas cantidades de
horas, escribe un programa que calcule el descuento anual a realizarse, considerando:
a. Si el sueldo anual es mayor a $2.000.000, el descuento es del %5.
b. Si el sueldo anual esta entre $1.000.000 y $2.000.000, debe aplicarse un descuento del %3.
c. Si el sueldo anual es menor a $1.000.000, debe aplicarse un descuento del %1.
d. El programa debe mostrar el salario anual bruto, el monto anual de bonificaciones, el monto anual
a descontarse y las horas trabajadas en todo el año."""

#ingreso de datos

#horas que trabajo el empledo en el mes
horas_de_trabajo = int(input("ingrese la cantidad de horas trabajadas en el mes: ")) 

#calculo de horas trabajadas mayores a 120.
if horas_de_trabajo > 120:
    valor_por_hora = 1500
    bonificacion_18 = (valor_por_hora * horas_de_trabajo) * 0.18
    sueldo_bruto = valor_por_hora * horas_de_trabajo
    sueldo_neto = sueldo_bruto + bonificacion_18
    sueldo_bruto_anual = sueldo_bruto * 12
    bonificacion_anual = bonificacion_18 * 12 #Calculo de bonificacion 
    descuento_anual = (sueldo_bruto_anual + bonificacion_anual) * 0.05 #Calculo de descuento anual.
    horas_anuales = horas_de_trabajo * 12
    print("Usted tiene un total de", horas_anuales, "horas anuales trabajadas")
    print("Su sueldo bruto anual es de $", sueldo_bruto_anual)
    print("Con una bonificacion anual de $", bonificacion_anual)
    print("Se le descontara de su sueldo anual una suma de $",descuento_anual)
    
#calculo de horas trabajadas mayores e iguales a 80 y menores e iguales a 120.
elif 80 <= horas_de_trabajo <= 120: 
    valor_por_hora = 1300
    bonificacion_15 = (valor_por_hora * horas_de_trabajo) * 0.15
    sueldo_bruto = valor_por_hora * horas_de_trabajo
    sueldo_neto = sueldo_bruto + bonificacion_15
    sueldo_bruto_anual = sueldo_bruto * 12
    bonificacion_anual = bonificacion_15 * 12 #Calculo de bonificacion anual.
    descuento_anual = (sueldo_bruto_anual + bonificacion_15) * 0.03 #Calculo de descuento anual.
    horas_anuales = horas_de_trabajo * 12
    print("Usted tiene un total de", horas_anuales, "horas anuales trabajadas")
    print("Su sueldo bruto anual es de $", sueldo_bruto_anual)
    print("Con una bonificacion anual de $", bonificacion_anual)
    print("Se le descontara de su sueldo anual una suma de $", descuento_anual)

#calculo de horas trabajadas menores a 80.
elif horas_de_trabajo < 80:
    valor_por_hora = 1100
    bonificacion_13 = (valor_por_hora * horas_de_trabajo) * 0.13
    sueldo_bruto = valor_por_hora * horas_de_trabajo
    sueldo_neto = sueldo_bruto + bonificacion_13
    sueldo_bruto_anual = sueldo_bruto * 12
    bonificacion_anual = bonificacion_13 * 12 #Calculo de bonificacion anual 
    descuento_anual = (sueldo_bruto_anual + bonificacion_anual) * 0.01 #Calculo de descuento anual.
    horas_anuales = horas_de_trabajo * 12
    print("Usted tiene un total de", horas_anuales, "horas anuales trabajadas")
    print("Su sueldo bruto anual es de $", sueldo_bruto_anual)
    print("Con una bonificacion anual de $", bonificacion_anual)
    print("Se le descontara de su sualdo anual una suma de $", descuento_anual)