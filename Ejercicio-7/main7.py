import funcions
TEXTO_1 = "La media es: "
TEXTO_2 = "La nota más grande es: "
TEXTO_3 = "La nota más pequeña  es: "
TEXTO_4 = "Las notas ordenadas son: "

def main():

    x = funcions.tamano()
    lst = funcions.rellenar_lst(x)
    printar = funcions.print_lst(lst)
    mitjana = funcions.mitjana_lst(lst, x)
    maximo, minimo = funcions.nota_max_min(lst, x)
    lst_ordenada = funcions.ordenar_lst(lst, x)

    print(TEXTO_1, mitjana)
    print(f"{TEXTO_2}{maximo} \n{TEXTO_3}{minimo}")
    print(TEXTO_4, lst)

if __name__ == '__main__':
    main()
