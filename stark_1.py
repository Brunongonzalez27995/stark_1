from data_stark import *
from funciones import *

def mostrar_superheroe_mas_fuerte():
    mas_fuerte = calcular_maximo_minimo_lista(lista_personajes, "fuerza", "maximo")
    mostrar_diccionario(mas_fuerte, "identidad", "peso")

def mostrar_superheroe_mas_bajo():
    mas_bajo = calcular_maximo_minimo_lista(lista_personajes, "altura", "minimo")
    mostrar_diccionario(mas_bajo, "nombre", "identidad")

def mostrar_peso_promedio_masculino():
    lista_masculinos = []
    for heroe in lista_personajes:
        if heroe["genero"] == "M":
            lista_masculinos.append(heroe)
    promedio = calcular_promedio_lista(lista_masculinos, "peso")
    mostrar_promedio("peso en los superheroes másculinos", promedio, "kg.")

def mostrar_fuerza_promedio_mayor_a_femenino():
    lista_femeninas = []
    lista_heroes_mas_fuertes = []

    for heroe in lista_personajes:
        if heroe["genero"] == "F":
            lista_femeninas.append(heroe)
    promedio_fuerza_femenina = calcular_promedio_lista(lista_femeninas, "fuerza")

    for heroe in lista_personajes:
        if float(heroe["fuerza"]) > promedio_fuerza_femenina:
            mostrar_diccionario(heroe, "nombre", "peso")
