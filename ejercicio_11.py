""" Escribe un programa que muestre los números del 1 al 10. Además, el programa debe mostrar:
a. Si es número es par o impar.
b. Cuanto es la suma total de todos los números mostrados.
c. Cuanto es la suma total de todos los números pares mostrados.
d. Cuanto es la suma total de todos los números impares mostrados."""

#Ingreso de datos
suma_total = 0
numeros_pares = 0
numeros_impares = 0
numero = 1

# While para mostrar los números del 1 al 10
while numero <= 10:
    print("Número:", numero)
    
    # Verífica si es par o impar
    if int(numero / 2) * 2 == numero:
        print("Es un número par")
        numeros_pares = numeros_pares + numero  # Agrega el número a la suma de los pares
    else:
        print("Es un número impar")
        numeros_impares = numeros_impares + numero  # Agrega el número a la suma de los impares
    
    # Agrega el número a la suma total
    suma_total = suma_total + numero
    
    # Incremento del contador
    numero = numero + 1

#Muestra en pantalla las sumas totales
print("Suma total:", suma_total)
print("Suma total de pares:", numeros_pares)
print("Suma total de impares:", numeros_impares)