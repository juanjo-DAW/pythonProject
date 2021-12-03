# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def main():
    lst = list()
    codilst = list()
    tflst = list()
    edadlst = list()
    contactolst = list()
    # valorlst = list()
    i = 0


    registres = int(input("Introdueix el nombre de valors del teus registres: "))
    while registres < 1:
        registres = int(input("Introdueix el nombre de valors del teus registres: "))

    for x in range(registres):
        nom = input("Introdueix el teu Nom:")
        cognom1 = input("Introdueix el teu 1r cognom: ")
        cognom2 = input("Introdueix el teu 2r cognom: ")
        codi = cognom1[:2] + cognom2[:2] + nom[:2]
        lst.append(codi)
        codilst.append(codi)

        telefon = input("Introdueix el teu número de telèfon: ")
        while len(telefon) < 9 or len(telefon) > 9:
            telefon = input("Introdueix el teu número de telèfon: ")
        lst.append(telefon)
        tflst.append(telefon)

        edad = int(input("Introdueix la teva edad: "))
        while edad < 1 or edad > 123:
            edad = int(input("Introdueix la teva edad: "))
        lst.append(edad)
        edadlst.append(edad)

        contacte = int(input("Introdueix si és un contacte nou o no: "))
        while contacte < 0 or contacte > 1:
            contacte = int(input("Introdueix si és un contacte nou o no: "))
        lst.append(contacte)
        contactolst.append(contacte)

        # valor = input("Introdueix la paraula YES o NO: ")
        # if valor[:1] == 'y':
        #     print('y')
        # else:
        #     print('n')
        # lst.append(valor)
        # valorlst.append(valor)

    while i < len(codilst):
       print("\t",codilst[i],"\t",tflst[i],"\t",edadlst[i],"\t",contactolst[i],)
       i += 1


if __name__ == '__main__':
    main()