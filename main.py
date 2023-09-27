from stark_1 import *

while True:
    opcion = mostrar_menu("Mostrar lista de personajes.", "Mostrar la identidad y el peso del superhéroe con mayor fuerza.", "Nombre e identidad del superhéroe más bajo.", "Peso promedio de los superhéroes masculinos.", "Nombre y peso de los superhéroes los cuales su fuerza supera a la fuerza promedio de todas las superheroinas.", "Salir de la aplicación")
    if opcion == "A" or opcion == "a":
        mostrar_lista(lista_personajes, "nombre", "identidad", "empresa", "altura", "peso", "genero", "color_ojos", "color_pelo", "fuerza", "inteligencia")
    elif opcion == "B" or opcion == "b":
        mostrar_superheroe_mas_fuerte()
    elif opcion == "C" or opcion == "c":
        mostrar_superheroe_mas_bajo()
    elif opcion == "D" or opcion == "d":
        mostrar_peso_promedio_masculino()
    elif opcion == "E" or opcion == "e":
        mostrar_fuerza_promedio_mayor_a_femenino()
    elif opcion == "F" or opcion == "f":
        print("Gracias por usar Stark_1 app.")
        break
    else:
        print("Introduce una opción valida.")

'''{ 
&quot;nombre&quot;: &quot;Howard the Duck&quot;,
&quot;identidad&quot;: &quot;Howard (Last name unrevealed)&quot;,
&quot;empresa&quot;: &quot;Marvel Comics&quot;,
&quot;altura&quot;: &quot;79.349999999999994&quot;,
&quot;peso&quot;: &quot;18.449999999999999&quot;,
&quot;genero&quot;: &quot;M&quot;,
&quot;color_ojos&quot;: &quot;Brown&quot;,
&quot;color_pelo&quot;: &quot;Yellow&quot;,
&quot;fuerza&quot;: &quot;2&quot;,
&quot;inteligencia&quot;: &quot;average&quot;
},

Recorrer la lista imprimiendo por consola todos los datos de cada superhéroe
B. Recorrer la lista y mostrar la identidad y el peso del superhéroe con mayor
fuerza (MÁXIMO)
C. Recorrer la lista y mostrar nombre e identidad del superhéroe más bajo
(MÍNIMO)
D. Recorrer la lista y determinar el peso promedio de los superhéroes
masculinos (PROMEDIO)
E. Recorrer la lista y mostrar nombre y peso de los superhéroes (cualquier
género) los cuales su fuerza supere a la fuerza promedio de todas las
superhéroes de género femenino  '''