import math

def limpiar_nan(datos): #para no tener problemas con los NaN creo esta funcion
    """
    devuelve una lista sin Nans
    """
    datos_l = []

    for i in datos:
    	if i == i:
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
    calcula la moda (valor que mas se repite) en datos
    """
    datos = limpiar_nan(datos)

    if len(datos) == 0:
        return float("nan")

    con = {} 

    for i in datos:
        if i in con:
            con[i] += 1
        else:
            con[i] = 1

    max_f = max(con.values())

    if max_f == 1:
        return float("nan")

    return max(con, key=con.get)


def rango(datos):
    """
    calcula el rango de datos (val_max-val_min) sin contar los nan
    """

    datos = limpiar_nan(datos)
    if len(datos) == 0:
        return float("nan")

    ma = max(datos)
    mi = min(datos)

    return ma - mi


def varianza(datos):
    """
    calcula la varianza de los datos
    """
    datos = limpiar_nan(datos)
    if len(datos) == 0:
        return float("nan")

    m = promedio(datos)
    suma = 0

    for i in datos:
        suma+=(i-m)**2

    return suma/len(datos)


def des_estandar(datos):
    """
    calcula la desviacion estandar de datos
    """
    datos = limpiar_nan(datos)
    if len(datos) == 0:
        return float("nan")

    return math.sqrt(varianza(datos)) #ya conocemos como calcular la varianza, no hay q hacerlo de nuevo


def precentil(datos,p):
    """
    calcula el precentil (p) ignora los NaN de la forma "nearest-rank" que creo que es la mas conveniente
    """
    datos = limpiar_nan(datos)

	datos = [float(x) for x in datos]
    if len(datos) == 0:
        return float("nan")

    if p < 0 or p>100:
        return float("nan")

    d_o = sorted(datos)
    n = len(d_o)

    k = math.ceil(p*n/100)-1
    return d_o[k]

def rang_intq(datos):
    """
    calcula el rango inter cuartil
    """
    q1 = precentil(datos,25)
    q3 = precentil(datos,75)

    return q3-q1

def covarianza(x,y):
	"""
	calcula la covarianza de dos variables
	"""
	n = len(x)
	px = promedio(x)
	py = promedio(y)

	suma = 0
	for xi, yi in zip(x,y):
		suma+= (xi-px) * (yi-py)

	return suma/n

def correlacion(x,y):
	"""
	calcula la correlacion segun la formula de Pearson
	"""
	return covarianza(x,y)/(des_estandar(x)*des_estandar(y))
	
