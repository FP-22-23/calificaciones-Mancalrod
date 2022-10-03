
def calcula_nota_cuestionario(aciertos,errores, respuestas_totales):
    return (aciertos/respuestas_totales - errores/(50-respuestas_totales))*10

def lee_entero(mensaje):
    return int(input(mensaje))
    
def lee_real(mensaje):
    return float(input(mensaje))

def calcula_nota_cuatrimestre(c1,c2,c3,prj,ex):
    res=10.0
    if prj <5:
        res= 3.0
    else:
        res= 0.1*(c1+c2+c3)+0.1*prj+0.6*ex
    return res
def calcula_nota_evaluacion_continua(c1,c2):
    res= 10.0
    if c1<4 or c2<4:
        res=4.0
    else:
        res= (c1+c2)/2
    return res





