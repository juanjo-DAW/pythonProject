# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def main():
    num1 = int(input("Introdueix el número que comença l'interval: "))
    num2 = int(input("Introdueix el número que acaba l'interval: "))
    num3 = int(input("Introdueix el valor dels que números que contará: "))

    while num1 > num2:
        print("Error torna a introduir els teus valors:")
        num1 = int(input("Introdueix el número que comença l'interval: "))
        num2 = int(input("Introdueix el número que acaba l'interval: "))
    while num3 == 0:
        num3 = int(input("Introdueix el valor dels nombres que contará:"))

    for x in range(num1, num2, num3):
        print(x)

if __name__ == '__main__':
    main()
