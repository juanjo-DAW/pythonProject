import funcions
TEXTO_1 = "Introduce la base de la potencia:  "
TEXTO_2 = "Introduce el exponente de la potencia:  "
TEXTO_3 = "El resultado de la potencia es: "

def main():
    x = funcions.validarint(TEXTO_1)
    y = funcions.validarint(TEXTO_2)
    p = funcions.potencia(x,y)
    print(TEXTO_3,p)

if __name__ == '__main__':
    main()