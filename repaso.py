from turtle import shape
import numpy as np
#ndarray

data = np.array([ [1,2], 
                  [3,4], 
                  [5,6],
                  [7,8] ], dtype=np.float64)

# data = np.array([1,2,3,4])

print(data)
print("Tipo de dato: " + str(type(data)))
print("Shape: " + str(data.shape))
print("Size: " + str(data.size))
print("Ndim: " + str(data.ndim))
print("Nbytes: " + str(data.nbytes))
print("Dtype: " + str(data.dtype))

# data = np.array(data, dtype=np.int64)
data = data.astype(np.int64)
print("Dtype modificado: " + str(data.dtype))

#int8, int16, int32, int64
#uint8, uint16, uint32, uint64
#Bool
#float8, float16, float32, float64
#complex64, complex128, complex256