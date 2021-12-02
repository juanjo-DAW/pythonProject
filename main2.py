# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def main():
    lst = list()
    registres = int(input("Introdueix el nombre de valors del teus registres: "))
    while registres < 1:
        registres = int(input("Introdueix el nombre de valors del teus registres: "))

    for x in range(registres):
        nom = input("Introdueix el teu Nom:")
        cognom1 = input("Introdueix el teu 1r cognom: ")
        cognom2 = input("Introdueix el teu 2r cognom: ")

        telefon = input("Introdueix el teu número de telèfon: ")
        while len(telefon) > 9 or len(telefon) < 9:
            telefon = input("Introdueix el teu número de telèfon: ")

        edad = int(input("Introdueix la teva edad: "))
        while edad > 123 or edad < 1:
            edad = int(input("Introdueix la teva edad: "))



    for x in range(registres):
        print("El teu codi és: ", cognom1[:2] + cognom2[:2] + nom[:2])


if __name__ == '__main__':
    main()