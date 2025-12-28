import math

def limpiar_nan(datos): #para no tener problemas con los NaN creo esta funcion
	"""
devuelve una lista sin Nans
	"""
	datos_l = []

	for i in datos:
		if i ==i:
			datos_l.append(i)

	return datos_l


def promedio(datos):
	"""
calcula el promedio de datos
	"""
	datos = limpiar_nan(datos)
	if len(datos) ==0:
		return float("nan")
	
    suma = 0
    for i in datos:
		suma+=i
    return suma/len(datos)


def mediana(datos):
	"""
calcula la mediana de los datos
	"""
	datos = limpiar_nan(datos)
	if len(datos) ==0:
		return float("nan")
	
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
	datos = limpiar_nan(datos)
	
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
	datos = limpiar_nan(datos)
	if len(datos) ==0:
		return float("nan")
	
	ma = max(datos)
	mi = min(datos)

	return ma-mi


def varianza(datos):
	"""
calcula la varianza de los datos
	"""
	datos = limpiar_nan(datos)
	if len(datos) ==0:
		return float("nan")
		
	suma = 0
	mm = media(datos)

	for i in datos:
		suma+=(i-mm)**2

	return suma/len(datos)


def des_estandar(datos):
	"""
calcula La desviaciÓn estandar de los datos
	"""
	datos = limpiar_nan(datos)
	if len(datos) ==0:
		return float("nan")
		
	return math.sqrt(varianza(datos))


def precentil(datos,p):
	"""
calcula el precentil (p) ignora los NaN
	"""
	datos = limpiar_nan(datos)
	if len(datos) ==0:
		return float("nan")

	d_o= sorted(datos)
	n = len(d_o)

	k = (n-1)*p/100
	f =int(k)
	g = f+1

	if g >= n:
		return d_0[f]

	else:
		return d_o[f] + (k-f)*(d_0[g]-d_o[f])


def rang_intq(datos):
	q1 = precentil(datos,25)
	q3 = precentil(datos,75)

	return q3-q1
	

































