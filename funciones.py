def mostrar_menu(key_0:str, key_1:str, key_2:str, key_3:str, key_4:str, key_5:str) -> str:
    menu = input("Ingrese una opción: \nA.{0}\nB.{1}\nC.{2}\nD.{3}\nE.{4}\nF.{5}\n".format(key_0, key_1, key_2, key_3, key_4, key_5))
    return menu

''' Ésta función muestra un menú de 6 opciones de A hasta F, recibiendo como parametro los mensajes
que deberá mostrar'''

def es_numero(cadena:str):
    try:
        float(cadena)
        return True
    except ValueError:
        return False
    
'''Ésta funcion ROBADA verifica si el str que se le pasa es un número.'''

def mostrar_diccionario(diccionario: dict, *claves: str):
    for clave in claves:
        if clave in diccionario:
            valor = diccionario[clave]
            if es_numero(valor):
                valor = "{:.2f}".format(float(valor))
            print("{0}: {1}".format(clave, valor))

'''Función que imprime un diccionario con multiples claves que se deben pasar en los parametros, corroborara si el 
str que se le pasa es un número, en dicho caso lo hará un flotante y lo mostrará con 2 decimales.'''

def mostrar_lista(lista:list, *claves:str):
    if len(lista) > 0:
        for elemento in lista:
            mostrar_diccionario(elemento, *claves)
    else:
        print("La lista está vacía")

'''Función que verifica si una lista está vacía, en caso de no estarlo, la recorre y muestra sus valores recurriendo
a la función mostrar_diccionario, de lo contrario, imprime un mensaje que la lista está vacía.'''


def calcular_maximo_minimo_lista(lista:list, clave:str, tipo:str) -> dict:
    retorno = -1
    if((type) == type(list) and type(clave) == (str) and len(lista) > 0):
        max_min = lista[0]
        for elemento in lista:
            if tipo == "minimo" and elemento[clave] < max_min[clave]:
                max_min = elemento
            if tipo == "maximo" and elemento[clave] > max_min[clave]:
                max_min = elemento
        retorno = max_min
    return retorno

'''Ésta función calcula el máximo o el mínimo de un elemento en una lista, recibe como parametros la lista,
la clave y el tipo (maximo o minimo) en caso de que la lista se encuentre vacia devolverá un -1.'''

def calcular_promedio_lista(lista:list, clave:str) -> float:   
    suma = 0
    retorno = False
    if lista != []:
        for elemento in lista:
            elemento[clave] = float(elemento[clave])
            suma += elemento[clave]
            promedio = suma / len(lista)
            retorno = promedio
    return  retorno

def mostrar_promedio(clave_0:str, promedio:float, clave_2:str):
    print("El promedio de {0} es {1:.2f} {2}".format(clave_0, promedio, clave_2))

'''Esta función calcula un promedio de una lista, recibiendo como parametros la lista y la clave.'''
