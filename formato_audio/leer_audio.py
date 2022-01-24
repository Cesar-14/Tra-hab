import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile

frecuencia_muestreo, muestras = wavfile.read("trompeta.wav")
print("frecuencia muestreo: " + str(frecuencia_muestreo))
print("Tipo de dato de arreglo de muestras: " + str(type(muestras)))
print("Dtype: " + str(muestras.dtype))
print("Shape: " + str(muestras.shape))

duracion = muestras.shape[0] / frecuencia_muestreo
print("Duración: " + "{:.2f}".format(duracion) + "seg")

print("FORMATO")
print("Frecuencia muestreo: " + str(frecuencia_muestreo))
prfundidad_bits = 32
if (muestras.dtype ==np.int16):
    profundidad_bits = 16
elif(muestras.dtype == np.unit8):
    profundidad_bits = 8

print("Profundidad de bits: " + str(profundidad_bits))

canales = 1
if (len(muestras.shape) > 1):
    canales = muestras.shape[1]
print("Cantidad canales: " + str(canales))

# Arreglo de tiempos
tiempos = np.linspace(0.0, duracion, muestras.shape[0])

# Dibujar grafica
plt.figure()
if canales == 1:
    plt.plot(tiempos, muestras, label ="Canal mono")
else:
    plt.plot(tiempos, muestras[:, 0], label = "Canal izquierdo")
    plt.plot(tiempos, muestras[:, 1], label = "Canal derecho")
plt.legend()
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud")
plt.show()