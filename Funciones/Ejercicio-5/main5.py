import funcions
TEXTO_1 = "Introdueix el primer valor:"
TEXTO_2 = "Introdueix el segon valor:"
TEXTO_3 = "Estos son los valores sin intercambiar"
def main():

    a,b = int(input(TEXTO_1)), int(input(TEXTO_2))
    funcions.intercambia(a,b)
    print(TEXTO_3,a,b)

if __name__ == '__main__':

    main()