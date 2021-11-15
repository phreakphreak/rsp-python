# # Tarea 3

# #   #+SPDX-License-Identifier: CC-BY-SA-4.0
# # Problema 1
# # Imagina que te has mudado a una nueva ciudad. Enfrente de tu casa
# #   pasan dos autobuses que te pueden llevar al trabajo, uno pasa cada
# #   hora a la hora y el otro pasa cada hora pero no a la hora exacta. Es
# #   decir, el primero pasa a las 6am, 7am, 8am, …  y el otro a las
# #   $(6+x)$ am, $(7+x)$ am, $(8+x)$ am, …, donde $x$ es un número positivo y
# #   constante. Desafortunadamente no sabes el valor de $x$ Suponiendo que
# #   $x$ es una cantidad distribuida uniformemente al azar, ¿Cuál es el
# #   promedio de espera si algún visitante decide salir a esperar el camión
# #   “cuando sea”?

# #   Tomado de Digital dice - Computational Solutions to practical
# #     probability problems de Paul J. Nahin

# # Solución
# import random

# tiempo_promedio_espera = {}

# NUM_SIMULACIONES = 500_000
# AUTOBUSES_A_SIMULAR = 10

# for NUM_AUTOBUSES in range(1, AUTOBUSES_A_SIMULAR):
#     tiempo_total_espera = 0

#     for _ in range(NUM_SIMULACIONES):
#         llegadas_autobuses = [0]   # El autobús que llega cada hora
#         for _ in range(NUM_AUTOBUSES-1):  # Para tener número_autobuses
#             llegadas_autobuses.append(random.random())

#         llegada_pasajero = random.random()   # A qué hora llegas a la parada del autobús

#         autobuses_ordenados = sorted(llegadas_autobuses)   # Ordenamos de menor a mayor

#         if llegada_pasajero > llegadas_autobuses[-1]:  # Llegó luego del último autobús
#             tiempo_espera = 1 - llegada_pasajero
#         else:
#             for llegada_autobus in autobuses_ordenados:
#                 if llegada_pasajero < llegada_autobus:
#                     tiempo_espera = llegada_autobus - llegada_pasajero
#                     break

#         tiempo_total_espera = tiempo_total_espera + tiempo_espera

#     tiempo_promedio_espera[NUM_AUTOBUSES] = (tiempo_total_espera/NUM_SIMULACIONES) * 60 # En minutos

# print(tiempo_promedio_espera)

# Problema 2
# Modifica el código de RPS para incluir a Lizard y a Spock

#   Scissors cuts Paper
#   Paper covers Rock
#   Rock crushes Lizard
#   Lizard poisons Spock
#   Spock smashes Scissors
#   Scissors decapitates Lizard
#   Lizard eats Paper
#   Paper disproves Spock
#   Spock vaporizes Rock
#   (and as it always has) Rock crushes Scissors
#   From the big bang theory wiki

# Problema 3
# Modifica RPSLS para que juegue la computadora entre si un número $N$ de juegos entre sí.
# Solución
import random

# Decidimos si el jugador_1 gana
def ganador(jugador_1, jugador_2):
    if (jugador_1 == 'tijera'  and jugador_2 == 'papel'  ) or \
       (jugador_1 == 'papel'   and jugador_2 == 'piedra' ) or \
       (jugador_1 == 'piedra'  and jugador_2 == 'lagarto') or \
       (jugador_1 == 'lagarto' and jugador_2 == 'spock'  ) or \
       (jugador_1 == 'spock'   and jugador_2 == 'tijera' ) or \
       (jugador_1 == 'tijera'  and jugador_2 == 'lagarto') or \
       (jugador_1 == 'lagarto' and jugador_2 == 'papel'  ) or \
       (jugador_1 == 'papel'   and jugador_2 == 'spock'  ) or \
       (jugador_1 == 'spock'   and jugador_2 == 'piedra' ) or \
       (jugador_1 == 'piedra'  and jugador_2 == 'tijera' ):
        print("Gana")
    elif jugador_1 == jugador_2:
        print("Empata")
    else:
        print("Perdió")

def estrategia_azar(opciones):
    return random.choice(opciones)

def estrategia_constante():
    return 'piedra'

def torneo(numero_de_juegos, estrategia_1, estrategia_2):
    # Opciones
    opciones = ['piedra', 'papel', 'tijera']

    for juego in range(numero_de_juegos):
        jugador_1 = estrategia_1(opciones)
        jugador_2 = estrategia_2()
        ganador(jugador_1, jugador_2)

if __name__ == '__main__':
    torneo(numero_de_juegos = 100, estrategia_1=estrategia_azar, estrategia_2=estrategia_constante)

# Otras maneras de escribir las reglas
# Diccionarios
import random

reglas = {
    'piedra'  : ['lagarto', 'tijera' ],
    'papel'   : ['piedra' , 'spock'  ],
    'tijera'  : ['papel'  , 'lagarto'],
    'lagarto' : ['spock'  , 'papel'  ],
    'spock'   : ['tijera' , 'piedra' ]
}

def ganador(jugador_1, jugador_2):
    if jugador_2 in reglas[jugador_1]:
        print("Gana")
    elif jugador_1 == jugador_2:
        print("Empata")
    else:
        print("Pierde")

