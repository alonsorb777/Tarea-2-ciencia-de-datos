def promedio(datos):
    """
    calcula el promedio.
    """
    suma = 0
    for x in datos:
        suma += x
    return suma / len(datos)