import funcions
TEXTO_1 = "Introduce un numero:"
def main():
    num = funcions.validarint(TEXTO_1)
    bin = funcions.binary(num)
    print(bin)

if __name__ == '__main__':
    main()