"""
Mario necesita ayuda para calcular el promedio de horas en 20 días laborables que trabajó en el mes,
pero la información viene en minutos.
Detalles: Une el resultado obtenido con horas por días.
Ejemplos: <hr />
Entrada: Total de minutos: 7200
Salida: 6 horas por días <hr />
Entrada: Total de minutos: 10000
Salida:8 horas por días
MARIO: 13400m/mes

def hours_calculator(minu):
    hours=minu/60
    h_perday=hours/days
    return int(h_perday)
days=int(input("Cuantos dias trabaja al mes"))
minutes=int(input("Cuantos minutos le dieron?"))
print("Mario trabaja",hours_calculator(minutes),"horas por día aprox")

Muralla china y la Luna
La famosa muralla china tiene 11 000 m de largo, de 5 a 8 metros de altura y 6 metros en la parte inferior, 
hasta 5 metros la parte superior. Tiene 67 torres de vigilancia y se encuentra a 980 metros sobre el nivel del mar.
La luna es el único satélite natural de la Tierra. Con un diámetro ecuatorial de 3476 Km, 
es el quinto satélite más grande del sistema solar. Está a una distancia 384,400 Km del planeta tierra.
¿Cuántas murallas chinas necesitaríamos para darle la vuelta completa a la luna?
¿Cuántas torres de vigilancias tendría en total la muralla alrededor de la luna?
Pista: Haya la circunferencia
Detalles: Imprime el resultado en consola, cada uno en líneas diferentes.

chiness_wall=11000/1000
moon_diameter=3476
cant_walls=moon_diameter/chiness_wall
print("¿Cuántas murallas chinas necesitaríamos para darle la vuelta completa a la luna?",
"Necesitaríamos unas",int(cant_walls),"Murallas chinas")
print("¿Cuántas torres de vigilancias tendría en total la muralla alrededor de la luna?",
"Tendría unas",int(cant_walls*67),"Torres en la Luna")
"""
DISTANCE_WALL = 11  # en Km
TOWERS = 67
DIAMETER = 3476  # Km

total_distance = DIAMETER * 3.14
total_walls = total_distance // DISTANCE_WALL
total_towers = total_walls * TOWERS

print('Se necesita {} muralla'.format(int(total_walls)))
print('Total de torres: ', int(total_towers))