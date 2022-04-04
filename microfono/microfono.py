import numpy as np
import matplotlib.pyplot as plt
import sounddevice as sd
from scipy.io.wavfile import write

# Formato de audio
frecuencia_muestreo = 44100
canales = 1
profundidad_bits = 'float64'

duracion = 5.3

grabacion = sd.rec(
    int(duracion * frecuencia_muestreo), # Total de frames (muestras) a grabar
    samplerate=frecuencia_muestreo, # Frecuencia de muestreo 
    channels=canales,               # Cantidad de canales
    dtype=profundidad_bits )        # Profundidad de bits (tipo de dato)

print("Comienza grabación")
sd.wait()
print("Grabación completa")

tiempos = np.linspace(0.0, duracion, len(grabacion) )

print("Shape: " + str(grabacion.shape))
print("dtype: " + str(grabacion.dtype))

sd.play(grabacion, frecuencia_muestreo)
print("Comienza reproducción")

sd.wait()
print("Reproducción completa")
grabacion_formato = (grabacion * np.iinfo(np.int16).max).astype(np.int16)
write("grabacion.wav", frecuencia_muestreo, grabacion_formato)

transformada = np.fft.rfft(grabacion[:,0])
frecuencias = np.fft.rfftfreq(len(transformada), 1.0 / frecuencia_muestreo)

print("Grabacion shape: " + str(grabacion[:,0].shape))
print("Transformada shape: " + str(transformada.shape))
print("Frecuencias shape: " + str(frecuencias.shape))

frecuencia_fundamental = frecuencias[transformada.argmax()]

print("Frecuencia fundamental: " + str(frecuencia_fundamental))

fig, ejes = plt.subplots(1,2)

ejes[0].plot(tiempos, grabacion[:,0])
ejes[1].plot(frecuencias,np.abs(transformada))
plt.show()