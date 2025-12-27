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
	med = mediana(datos)
	desviacion = []

	for i in datos:
		desviacion.append(abs(i-med))

	return mediana(desviacion)


def moda(datos):
	"""
calcula la moda (valor más repetido) de los datos
	"""
    con =  {}

	for i in con:
		if i in con:
			con[i] +=1
		else:
			con[i] = 1

	return max(con, key=con.get) # esto permite no tener errores y contar correctamente lo que se busca para la moda

def rango(datos):
	"""
calcula el rango de los datos
	"""
	ma = max(datos)
	mi = min(datos)

	return ma-mi


def varianza(datos):
	"""
calcula la varianza de los datos
	"""
	suma = 0
	mm = media(datos)





































