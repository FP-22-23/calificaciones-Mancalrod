from calificaciones import *
def main():
    c1 = lee_real("Dame la nota del c1: ")
    c2= lee_real("Dame la nota del c2: ")
    c3= lee_real("Dame la nota del c3: ")
    prj= lee_real("Dame la nota del proyecto 1: ")
    ex= lee_real("Dame la nota del examen: ")
    cuatrimestre1= calcula_nota_cuatrimestre(c1,c2,c3,prj,ex)
    print("la nota del primer cuatrismestre: ", cuatrimestre1)
    c4 = lee_real("Dame la nota del cuestionario 4: ")
    c5= lee_real("Dame la nota del cuestionario 5: ")
    c6= lee_real("Dame la nota del cuestionario 6: ")
    prj2= lee_real("Dame la nota del proyecto 2: ")
    ex2= lee_real("Dame la nota del examen 2: ")
    cuatrimestre2= calcula_nota_cuatrimestre(c4,c5,c6,prj2,ex2)
    print("La nota de la evaluación continua es: ", (cuatrimestre1+cuatrimestre2)/2)

if __name__ == "__main__":
    main()