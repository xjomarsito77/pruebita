mes="""
BIENVENIDO A NUESTRO CALENDARIO VIRTUAL
SELECCIONE UN NUMERO DEL 1 AL 12 PARA IDENTIFICAR
                   SU MES.

"""
print(mes)
n=int(input("inserte el numero: "))

match n:
    case 1:
        print(f"{n} corresponde a Enero")
    case 2:
        print(f"{n} corresponde a Febrero")
    case 3:
        print(f"{n} corresponde a marzo")
    case 4:
        print(f"{n} corresponde a abril")
    case 5:
        print(f"{n} corresponde a mayo")
    case 6:
        print(f"{n} corresponde a junio")
    case 7:
        print(f"{n} corresponde a julio")
    case 8:
        print(f"{n} coresponde a agosto")
    case 9:
        print(f"{n} corresponde a septiembre")
    case 10:
        print(f"{n} corresponde a octubre")
    case 11:
        print(f"{n} correponde a noviembre")
    case 12:
        print(f"{n} corresponde a diciembre")
    case 13:
        main="""Espera, ¿Dijiste 13? Aquí tiene pa que me la bese, 
        entre más me la beses más me creces, busca un cura pa que me la rece, 
        y trae un martillo pa que me la endereces, por el chiquito se te aparece toas las veces 
        y cuando te estreses aquí te tengo este pa que te desestreses.
        """
        print(main)
    case _:
        print(f"{n} no se encuentra identificado ")
        