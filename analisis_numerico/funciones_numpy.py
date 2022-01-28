import numpy as np

# Formas de crear arreglos

# Con una lista de python
datos = np.array([1,2,3])
# print(datos)

# Con una lista multidimensional de python
datos = np.array([[1,2], [3,4]])
# print(datos)

# Con constantes

# Ceros
datos = np.zeros((5,3))
# print(datos)

# Unos
datos = np.ones((4,3))
# print(datos)
# print(datos.dtype)

# Constantes arbitrarias
datos = np.ones((4,3)) * 3.5
datos = np.full((4,3), 3.5)

datos = np.empty((4,3))
datos.fill(7.4)


# secuencias incrementales en base al incremento
# Arrange excluye el stop y siempre incluye el start
# Si no se especifica start es 0 y step es 1
datos = np.arange(15)
# arrange(Start, Stop, Step)
datos = np.arange(10,15,0.5)
# print(datos)

# Secuencias incrementales en base al numero de elementos
# Siempre se incluyen el start y el stop
# Start, Stop, Numero de elementos
datos = np.linspace(0,10,11)

# print(datos)
# print(datos.shape)

# Secuencias logaritmicas
# 10**0     10**2      5 elementos
# 1         100        5
datos = np.logspace(0,2,5)
print(datos)
print(datos.shape)


# Meshgrid
x = np.array([1,2,3,4,5])
y = np.array([6,7,8])

XX, YY = np.meshgrid(x,y)

# print(XX)
# print(XX.shape)
# print(YY)
# print(YY.shape)

# Crear arreglos con propiedades de otros
datos = np.ones_like(XX)
datos = np.zeros_like(XX)
datos = np.full_like(XX, 3.5)
# print(datos)

# Matrices
# Identidad
datos = np.identity(4)
# print(datos)

# Eye
datos = np.eye(4, k=-1)
print(datos)