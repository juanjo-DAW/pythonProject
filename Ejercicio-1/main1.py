import funcions
TEXTO_1 = "Introduce un numero entre 10 y 5000: "
TEXTO_2 = "El teu nombre és: "

def main():

    num = funcions.validate(TEXTO_1)
    while num == -1:
        num = funcions.validate(TEXTO_1)
    print(TEXTO_2, num)

if __name__ == '__main__':
    main()