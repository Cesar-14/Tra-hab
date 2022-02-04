import numpy as np

data = np.arange(0,11)
indice = 7

print(data)

print("indice 0: ") + str(data[0] )
print("indice 3: ") + str(data[3] )

# Index out of bounds
# print("indice 16: " + str(data[16]) )

# Si usamos variables en los indices
# Tienen que ser int (numero entero)
# Puede ser negativo
print("Indice 'indice': " + str(data[int(indice)] ))

# Si usamos negativos se recorre en reversa
# Comenzando desde el -1
print("Indice -1: " + str(data[-1]))
print("Indice -7: " + str(data[-7]))

# Out of bounds
# print("Indice -16: " + str(data[-16]))

# Rangos [m:n]
# m se excluye
# n se excluye
# Rango siempre regresa un arreglo
print("Indice [0:5]:" + str(data[0:5]))
# Me regresa un arreglo vacio
print("Indice [1:1]:" + str(data[1:1]))

print("Indice [1:2]:" + str(data[1:2]))

# Si no le doy rangos validos me regresa vacio
print("Indice [4:1]:" + str(data[4:1]))
# No existe el indice 11, pero no marca error
# porque nunca intenta acceder a el
print("Indice [1:11]:" + str(data[1:11]))
# Si se sale de los limites, no marca error,
# solo te regresa hasta donde puede
print("Indice [1:16]:" + str(data[1:16]))
# Estos si son validos, aunque sean negativos
# la n (2do datos del rango) siempre es excluyente
print("Indice [1:-1]:" + str(data[1:-1]))
print("Indice [1:-3]:" + str(data[1:-3]))

# El 3er parametro del rango es el "step"
print("Indice [1:-1:2]: " + str(data[1:-1:2]))

# Los parametros de los rangos, son opcionales
# si se omite el primero (m) lo toma como el primer elemento
print("Indice [:5]: " + str(data[:5]) )
# si se omite el segundo (n) lo toma como el ultimo elemento
print("Indice [2:]:" + str(data[2:]))
print("Indice [-6:]:" + str(data[-6:]))
# Si se omiten ambos parametros (m y n) lo toma como
# desde el primero hasta el ultimo
# Solo se completa el step
print("Indice [::2]:" + str(data[::2]))
# Si los valores del step son negativos
# Primero invierte el arreglo
print("Indice [::-1]:" + str(data[::-1]))
print("Indice [::-2]:" + str(data[::-2]))

elemento = data[5]
elemento = 7
# data[5] = 7
print("elemento: " + str(elemento))
print("data: " + str(data))

# Se modifica un segmento obtenido por rango de un ndarray
# Tambien se ve modificado el ndarray original
segmento = data[1:6:2]
print("segmento: " + str(segmento))
segmento[0] = 24
print("segmento modificado:  " + str(segmento))
print("data: " + str(data))

# Si se modifica el ndarray original
# tambien se ve modificado el segmento
data[5] = 48
print("data: " + str(data))
print("segmento: " + str(segmento) )