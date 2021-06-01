""" Modulo Ciclos
    Funciones para practicas con ciclos
    Santiago Correa Restrepo
    Mayo 29-2021 """

# Definición de Funciones
#======================================================================
#          E S P A C I O    D E    T R A B A J O     A L U M N O
# ====================================================================

def simulador_caida_libre(altura):
  # Free fall motion function
  # Gravity en m/s2
  g = 9.8 
  # Total height for free fall motion in meters
  dt = 0  

  if altura > 0:
    for t in range(0, 100):
      # Free fall distance equation
      d = 0.5 * g * (t**2)
      dt = dt + d

      if dt <= altura:
        print("Time (s): ", t)
        print("Interval of falling in meters : ", d)
        print("Total distance of free fall motion: ", dt)
  else:
    print("Building's height must be greater than zero")

# Total of members from every generation function
def generador_generaciones(generacion):
  y = 1
  # Loop to evaluate total number of people by generation
  for generacion in range(0, 5):
    if generacion > 0:
      y *= 2
    else:
      y = 1

    print("Generation", generacion, "is formed by", y, "people")

# Function to generate a triangle with numbers
def constructor_triangulos(pisos):
  start = 1
  if pisos > 0:
    for i in range(pisos):
      for j in range(i+1):
          print(start, '', end = '')
          start += 1
      print('')
  else:
    print("Number of rows must be a natural number and greater than zero")

def constructor_tableros(longitud):
  #TODO Comentar código
  #TODO Implementar la función
  return "No implementada aún"