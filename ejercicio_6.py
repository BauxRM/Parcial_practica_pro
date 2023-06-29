"""Del punto anterior, calcular y mostrar por pantalla el sueldo bruto, el monto a bonificar y el sueldo neto
(bruto + bonif), considerando:
a. Si trabajo más de 120hs, la bonificación es de %18
b. Si trabajo entre 80 y 120 horas, la bonificación es de %15
c. Si trabajo menos de 80 horas, la bonificación es de %13."""

#Cngreso de datos
horas_de_trabajo = int(input("ingrese la cantidad de horas trabajadas en el mes: ")) #horas que trabajo el empledo en el mes.

#Calculo de horas trabajadas mayores a 120.
if horas_de_trabajo > 120:
    valor_por_hora = 1500
    bonificacion_18 = (valor_por_hora * horas_de_trabajo) * 0.18 #Calculo de bonificacion.
    sueldo_bruto = valor_por_hora * horas_de_trabajo
    sueldo_neto = sueldo_bruto + bonificacion_18
    print("Su sueldo bruto es de $", sueldo_bruto)
    print("Con una bonificacion de $", bonificacion_18)
    print("Su sueldo neto es de $",sueldo_neto)
    
    
#Calculo de horas trabajadas mayores e iguales a 80 y menores e iguales a 120.
elif 80 <= horas_de_trabajo <= 120:  
    valor_por_hora = 1300
    bonificacion_15 = (valor_por_hora * horas_de_trabajo) * 0.15 #Calculo de bonificacion.
    sueldo_bruto = valor_por_hora * horas_de_trabajo
    sueldo_neto = sueldo_bruto + bonificacion_15
    print("Su sueldo bruto es de $", sueldo_bruto) 
    print("Con una bonificacion de $", bonificacion_15)
    print("Su sueldo neto es de $", sueldo_neto)

#Calculo de horas trabajadas menores a 80.
elif horas_de_trabajo < 80:
    valor_por_hora = 1100
    bonificacion_13 = (valor_por_hora * horas_de_trabajo) * 0.13 #Calculo de bonificacion.
    sueldo_bruto = valor_por_hora * horas_de_trabajo
    sueldo_neto = sueldo_bruto + bonificacion_13
    print("Su sueldo es de $", sueldo_bruto)
    print("Con una bonificacion de $", bonificacion_13)
    print("Su sueldo neto es de $", sueldo_neto)