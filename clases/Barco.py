from clases import Conventions
from clases import Case
from itertools import product, repeat
from random import choice
from juego import HORIZONTAL, ORIENTACIONES


instances = []
casillas_ocupadas = set()

# performance / legibilidad:
num_lineas = Conventions.tablero_num_lineas
num_columnas = Conventions.tablero_num_columnas
num2l = Conventions.generar_num_linea
num2c = Conventions.generar_num_columna


#  Clase que representa un barco
def __init__(self, longitud):
    self.longitud = longitud
    self.orientacion = choice(ORIENTACIONES)
    self.tocado = False
    self.hundido = False

def orientar(self):
    if self.orientacion == HORIZONTAL:
        rang = choice(range(num_lineas))
        primero = choice(range(num_columnas + 1 - longitud))
        letra = num2l(rang)
        cifras = [num2c(x) for x in range(primero, primero + longitud)]
        self.casillas = {Case.instances[l + c]
                            for l, c in product(repeat(letra, longitud), cifras)}   
             
    else:
        rang = choice(range(num_columnas))
        primero = choice(range(num_lineas + 1 - longitud))
        cifra = num2c(rang)
        letras = [num2l(x) for x in range(primero, primero + longitud)]
        # Crear el barco
        self.casillas = {Case.instances[l + c]
                            for l, c in product(letras, repeat(cifra, longitud))}
        
    return self.casillas    


def instanciar(self):
    for existente in instances:
        if self.casillas.intersection(existente.casillas):
            # break relativo al "for existente in barcos:"
            break
        else:
            # Agregar el barco en el contenedor de barcos
            instances.append(self)
            # Informar la casilla que contiene un barco.
            for casilla in self.casillas:
                casilla.contiene_barco = True
            # Agregar estas casillas a las casillas ocupadas :
            casillas_ocupadas.update(self.casillas)
            # break relativo al "for existente in barcos:"
            break
    else:
        # break relativo al "while True:"
        return
    
@classmethod   
def generar_barcos(self):
    while True:
        self.longitud = choice(Conventions.barcos_longitud)
        self.orientacion = choice(ORIENTACIONES)
        self.tocado = False
        self.hundido = False
        self.horizontal()
        self.instanciar()
        if len(instances) == len(Conventions.barcos_longitud):
            break

