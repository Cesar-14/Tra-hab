import numpy as np
import matplotlib.pyplot as plt
from scipy.io.wavfile import write

frecuencia_muestreo = 44100.0
frecuencia = 450.0
duracion  = (1 / frecuencia) * 3
tiempos = np.linspace(0.0,duracion,int(duracion * frecuencia_muestreo))
amplitud = np.iinfo(np.int16).max

# f(t) = A sin(2pi t)
data = amplitud * np.sin(2.0 * np.pi * frecuencia * tiempos)

fig, ejes = plt.subplot(1,2)

plt.figure()
ejes[0,0].plot(tiempos,data)
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

ejes[0,3].plot(frecuencias, np.abs(pasa_bajas), label="Filtro pasabajas")
ejes[0,3].legend()
# plt.show()
ejes[0,2].plot(tiempos,pasa_bajas_data, label="Audio pasabajas")
ejes[0,2].legend()


ciclos_rectangular = frecuencia * tiempos
fracciones_rectangular, enteros_rectangular = np.modf(ciclos_rectangular)
data_rectangular = (
    amplitud * np.sign(
        fracciones_rectangular - fracciones_rectangular.mean())
    )

ejes[1,0].plot(tiempos,data_rectangular)


transformada_rectangular = np.fft.rfft(data_rectangular)
frecuencias_rectangular = np.fft.rfftfreq(cantidad_muestras, periodo_muestreo)

ejes[1,1].plot(frecuencias_rectangular, np.abs(transformada_rectangular))

pasa_bajas_rectangular = transformada.copy()
pasa_bajas_rectangular[frecuencias_rectangular > frecuencia] *= 0

ejes[1,3].plot(frecuencias_rectangular, np.pasa_bajas_rectangular)

pasa_bajas_data_rectangular = np.fft.irfft(pasa_bajas_rectangular)

ejes[1,2].plot(tiempos, pasa_bajas_data_rectangular)


plt.show()