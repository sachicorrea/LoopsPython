import math
import funciones_ciclos as fc

# Free motion algorithm
altura = int(input("Enter a positive integer as building's height in meters: "))
fc.simulador_caida_libre(altura)

# Generations algorithm
generacion = int(input("Ingrese un número entero positivo de generaciones a evaluar: "))
fc.generador_generaciones(generacion)

# triangle with numbers pattern
pisos = int(input("Enter natural number for triangle's rows: "))
fc.constructor_triangulos(pisos)
