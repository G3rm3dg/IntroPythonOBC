def año():
    num = int(input("A continucion Digite el año: "))
    if num % 4 == 0:
        print("\nel año es Biciesto\n")
    else:
        print("\nel año no es Biciesto\n")

#--EJECUCION--#
print("\nPROGRAMA PARA VERIFICAR SI UN AÑO ES BICIESTO \n")
año()
print("FIN DE LA EJECUCION")