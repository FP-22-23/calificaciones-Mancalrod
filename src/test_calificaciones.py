from calificaciones import *
def main():
    aciertos= lee_entero("Dame tus aciertos: ")
    errores= lee_entero("Dame tus errores: ")
    total_respuestas= lee_entero("Dame el total de respuestas correctas del test: ")
    nota= calcula_nota_cuestionario(aciertos,errores,total_respuestas)
    print("Tu nota es: ",nota)

if __name__ == "__main__":
    main()