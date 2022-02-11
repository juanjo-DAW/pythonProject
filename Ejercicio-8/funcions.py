TEXTO_1 = "Estos son los valores intercambios:"
TEXTO_2 = "Introduce un numero del 1 al 50: "
# Ejercicio 1-El projecte en que estàs treballant requereix que l’usuari introdueixi un valor natural entre 10 i 5000 (inclosos) i, en cas que no ho faci, li torni a demanar que introdueixi el nombre (fins a un màxim de 3 cops). Implementa aquesta funció de validació.


# Valida si es un número natural.
def validarint(txt):
    num = int(input(txt))
    while num < 1:
        num = int(input(txt))
    return num

# Ejercicio 3-Donat un nombre enter introduït per teclat, dissenya un algoritme que calculi la seva equivalència en sistema binari (sense utilitzar arrays) i mostri el resultat per pantalla.

def binary(num):
    count = 1
    binario = 0
    while num != 0:
        rem = num % 2
        num = num // 2
        binario = binario + (rem * count)
        count = count * 10
    return binario

# Ejercicio 4-Implementa un programa que demani introduir 15 notes de 0 a 10 per teclat, calcula la mitjana d'aprovats i la mitjana dels suspesos i indica la quantitat d'aprovats i suspesos.

# Ejercicio 5-Implementa un programa que demani dos valors enters per teclat i intercanviï els seus valors.

def intercambia(a,b):

    a,b = b,a

    print(TEXTO_1,a,b)

# Ejercicio 6-Dissenya un algorisme que llegeixi des del teclat un valor enter i tot seguit mostri fins a quin punt de la seqüència ordenada de nombre positius (1, 2, 3, etc.) cal sumar per arribar al nombre més proper per sota d’aquest valor. Finalment, han de mostrar quina és la suma d’aquests nombres. Per exemple, si l’entrada és el nombre 12, el resultat és mostrar els nombres 0, 1, 2, 3 i 4, i la seva suma, que és 10, ja que si s’inclou el 5 ens passem de 12.

# Ejercicio 7-Donat el següent pseudocodi, implementa l'algoritme en C (aplicant el disseny modular), afegint les següents modificacions:
#                       Demani per teclat la dimensió de l'array (nombre natural entre 1 i 50 inclosos)
#                       Demani per teclat tants nombres enters com dimensió indicada. Els valors han de ser entre 0 i 10 (inclosos)
#                       Mostri per pantalla:
#                                           mitjana dels valors introduïts
#                                           valor mínim i màxim introduïts a l'array
#                                           l’array ordenat de manera ascendent
def tamaño():
    s = int(input(TEXTO_2))
    while (s < 1 or s > 50):
        s = int(input(TEXTO_2))
    return s

# Ejercicio 8-Dissenya una funció que, donats dos nombres naturals (x,y) retorni xy.

def potencia(x,y):
    t = x
    for i in range(y-1):
        t *= x
    return t

# Ejercicio 9-Dissenya un programa que demani per teclat un nombre en format binari (que no sigui més gran de 7 dígits, inclòs) i retorni el seu valor en base decimal.

# Ejercicio 10-Dissenya un programa de gestió de biblioteca, on s’ha de demanar:
#                   quants llibres es volen registrar
#                   per cada llibre, demanar:
#                                   títol del llibre
#                                   autor del llibre
#                                   editorial
#                                   data de publicació
#                                   unitats disponibles
#                                   usuari que l’ha agafat en prèstec
#                                   temps de préstec (en dies)

# Ejercicio 11-Dissenya un programa que inicialitzi proceduralment un array amb els 100 primers nombres parells (Nota: el 0 no és parell) i els mostri per pantalla.

# Ejercicio 12-Dissenya un programa que emani per teclat la dimensió de l'array (nombre natural entre 1 i 50 inclosos), que l’ompli per teclat amb valors naturals i mostri l’array ordenat de manera descendent.

# Ejercicio 13-Dissenya un programa que demani:
#              quants valors vol generar automàticament
#              entre quin rang els vol generar
#              mostri un menú amb les segúents opcions:
#                       ordenar aquests valors de manera ascendent
#                       ordenar aquests valors de manera descendent
#                       cercar un valor introduït per teclat

# Ejercicio 14-Dissenya un programa que generi una llista de valors aleatoris entre el 15 i el 200, demani un valor per teclat i informi per pantalla si aquest valor indicat es troba a la llista.

# Ejercicio 15-Implementeu en C el programa que resolgui el següent algoritme. Cal que definiu i inicialitzeu totes les variables que apareixen. No cal que demaneu dades a l'usuari. El valor de totes les variables el definiu vosaltres en el moment d'inicialitzar-lo. S'entén que si volem provar diferents casos el que farem serà canviar aquest valor inicial. Algoritme que ens ajudaria a triar les revolucions a la que hem de posar la rentadora, i ens informa de les revolucions i del temps de rentat.
