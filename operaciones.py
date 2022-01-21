import numpy as np

data1 = np.array([1,2,3], dtype=np.float64)
data2 = np.array([1,2,3], dtype=np.complex128)

data3 = data1 + data2

print(data3)
print("Dtype: " + str(data3.dtype))
print("Dtype: " + str(data2.dtype))
print("Dtype: " + str(data1.dtype))

raiz_cuadrada = np.sqrt(np.array([-1, 0, 1], dtype=np.complex128))
print(raiz_cuadrada)
print("Dtype raiz_cuadrada: " + str(raiz_cuadrada.dtype))

data  = np.array([1,2,3], dtype=np.complex128)
print(data)
print(str(data.real) + "Dtype: " + str(data.real.dtype))
print(str(data.imag) + "Dtype: " + str(data.imag.dtype))