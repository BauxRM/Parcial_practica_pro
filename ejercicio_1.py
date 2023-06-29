"""Escribe un programa que calcule la edad que cumplió o debe cumplir este año la persona, basado en el
año de nacimiento."""

#Ingreso de datos

#AÑo de nacimiento de la persona
ano_de_nacimiento = int(input("Ingrese el año de nacimiento: "))

#Año lectivo
ano_lectivo = int(input("Ingrese el año lectivo: "))

#Calculo de edad de la persona
edad = ano_lectivo - ano_de_nacimiento

print("Este año esta persona cumplio", edad, "años")
