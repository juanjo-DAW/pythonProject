# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def main():

    Nom = input("Introdueix el teu Nom:")
    Cognom1 = input("Introdueix el teu 1r cognom: ")
    Cognom2 = input("Introdueix el teu 2r cognom: ")

    print("El teu codi és: ", Cognom1[:2] + Cognom2[:2]+Nom[:2])

if __name__ == '__main__':
    main()
