import funcions

def main():

    num = int(input("Introdueix un valor:\n"))
    while (num == -1):
        num = funcions.validate()
    print("El teu nombre és: ",num)

if __name__ == '__main__':
    main()
