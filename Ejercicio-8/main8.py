import funcions
TEXTO_1 = "El resultado de la potencia es: [%d]"

def main():
    x = funcions.validate()
    y = funcions.validate()
    p = funcions.potencia(x,y)
    print(p)

if __name__ == '__main__':
    main()