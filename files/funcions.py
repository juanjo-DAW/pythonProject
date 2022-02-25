TEXTO_1 = "Introdueix una frase:"

# 1-Funció per llegir un fitxer.
def file_read(fname):
    f = open(fname)
    print(f.read())
    f.close()

# 2-Funció per escriure desde teclat un text a un fitxer i permet llegir-lo despres.
def file_add_txt(fname):
    f = open(fname, "a+")
    str = input(TEXTO_1)
    while len(str) > 100:
        str = input(TEXTO_1)
        f.write(str)
    print(f.read())
    f.close()

