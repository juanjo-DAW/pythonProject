# Ejercicio 1-El projecte en que estàs treballant requereix que l’usuari introdueixi un valor natural entre 10 i 5000 (inclosos) i, en cas que no ho faci, li torni a demanar que introdueixi el nombre (fins a un màxim de 3 cops). Implementa aquesta funció de validació.


# Valida si es un número natural.
def validate():
    num = int(input("Introduce un número natural: "))
    while num < 1:
        num = int(input("Introduce un número natural: "))
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