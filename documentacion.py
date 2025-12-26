import math

def promedio(datos):
	"""
	calcula el promedio de datos
	"""
    suma = 0
    for i in datos:
	suma+=i
    return suma/len(datos)


def mediana(datos):
	"""
	calcula la mediana de los datos
	"""
    d_o=sorted(datos)
    n=len(d_o)
    medi= n//2 #la división tiene q ser un entero

    if n%2 == 0:
	return(d_o[medi-1]+d_o[medi])/2

    else:
	return(d_o[medi])


def desviacion_mediana_absoluta(datos):
	"""
	calcula la desviacion de la mediana absoluta
	"""

    



































