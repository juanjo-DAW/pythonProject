# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def main():
    lst = list()
    i = 0
    j = 0
    k = 6
    registres = int(input("Introdueix el nombre de valors del teus registres: "))
    while registres < 1:
        registres = int(input("Introdueix el nombre de valors del teus registres: "))

    for x in range(registres):
        nom = input("Introdueix el teu Nom:")
        lst.append(nom)
        cognom1 = input("Introdueix el teu 1r cognom: ")
        lst.append(cognom1)
        cognom2 = input("Introdueix el teu 2r cognom: ")
        lst.append(cognom2)

        telefon = input("Introdueix el teu número de telèfon: ")
        while len(telefon) < 9 or len(telefon) > 9:
            telefon = input("Introdueix el teu número de telèfon: ")
        lst.append(telefon)

        edad = int(input("Introdueix la teva edad: "))
        while edad < 1 or edad > 123:
            edad = int(input("Introdueix la teva edad: "))
        lst.append(edad)

        contacte = int(input("Introdueix si és un contacte nou o no: "))
        while contacte < 0 or contacte > 1:
            contacte = int(input("Introdueix si és un contacte nou o no: "))
        lst.append(contacte)

    while i < registres:
        print( lst[j:k])
        i += 1
        j += 6
        k += 6


    # for x in range(registres):
    #     print("El teu codi és: ", cognom1[:2] + cognom2[:2] + nom[:2])

if __name__ == '__main__':
    main()