# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def main():

    frase = "Practica els problemes de list comprehensions per a ser més Pythonic!"
    vocals = [x for x in frase if x not in 'aàäAÀÄeèéëEÈÉËiíïIÍÏoòóöOÒÓÖuúüUÚÜ']
    string = "".join(vocals)
    print(string)

if __name__ == '__main__':
    main()