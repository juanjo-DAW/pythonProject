import funcions
TEXTO_1 = "El resultado de la suma es: "
def main():

    x = funcions.introducir_val()
    resultado = funcions.secuencia(x)
    print(TEXTO_1, resultado)

if __name__ == '__main__':
    main()