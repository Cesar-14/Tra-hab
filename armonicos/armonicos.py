import numpy as np
import matplotlib.pyplot as plt
from scipy.io.wavfile import write

frecuencia_muestreo = 44100
frecuencia = 450
tiempos = np.linspace(0.0,1.0,frecuencia_muestreo)
amplitud = np.iinfo(np.int16).max

ciclos = frecuencia * tiempos

fracciones, enteros = np.modf(ciclos)
data = fracciones

data = fracciones - 0.5

data = np.abs(data)

data = data - data.mean()

alto, bajo = abs(max(data)), abs(min(data))
data = amplitud * data / max(alto, bajo)

plt.figure()
plt.plot(tiempos,data)
plt.show()

write("Triangulo.wav", frecuencia_muestreo, data.astype(np.int16))

cantidad_muestras = len(data)
periodo_muestreo = 1.0 / frecuencia_muestreo
transformada = np.fft.rfft(data)
frecuencias = np.fft.rfftfreq(cantidad_muestras, periodo_muestreo)

plt.figure()
plt.plot(frecuencias, np.abs(transformada))
# plt.show()

# Ejercicio Clase

# 1.- Obtener en Hz las frecuencias de los armonicos de la señal

print(frecuencias[transformada > 100000])
    
# 2.- Aplicarle un filtro pasabajas que solo deje pasar la Freq Fundamental y luego aplicarle una transformada inversa

pasa_bajas = transformada.copy()
pasa_bajas[frecuencias > frecuencia] *= 0

pasa_bajas_data = np.fft.irfft(pasa_bajas)

# graficarlas y crear un archivo wav para escucharlas

write("triangulo_pasabajas.wav", frecuencia_muestreo, pasa_bajas_data.astype(np.int16))

plt.plot(frecuencias, np.abs(pasa_bajas), label="Filtro pasabajas")
plt.legend()
plt.show()

plt.plot(tiempos,pasa_bajas_data, label="Audio pasabajas")
plt.legend()
plt.show()