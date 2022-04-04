import numpy as np
import matplotlib.pyplot as plt
import sounddevice as sd

from scipy.io.wavfile import write

frecuencia_muestreo = 44100
canales = 1
profundidad_bits = 'float64'

duracion = 5

grabacion = sd.rec(
    int(duracion * frecuencia_muestreo), # Total de frames (muestras) a grabar
    samplerate = frecuencia_muestreo,    # Frecuencia de muestreo 
    channels = 1,                        # Cantidad de canales
    dtype = profundidad_bits )           # Profundidad de bits (tipo de dato)

print("Comienza grabación")
sd.wait()
print("Grabación completa")

tiempos = np.linspace(0.0, duracion, len(grabacion))

print("Shape: " + str(grabacion.shape))
print("Shape: " + str(grabacion.dtype))

sd.play(grabacion, frecuencia_muestreo)
print("Comienza reproduccion")
sd.wait()
print("Reproduccion completa")

grabacion_formato = (grabacion * np.iinfo(np.int16).max).astype(np.int16)

write("grabacion.wav", frecuencia_muestreo, grabacion_formato)

transformada = np.fft.rfft(grabacion[:,0])
frecuencias = np.fft.rfftfreq(len(grabacion[:, 0]), 1.0 / frecuencia_muestreo)

print("Grabacion shape: " + str(grabacion[:, 0].shape))
print("Transformada shape: " + str(transformada.shape))
print("Frecuencias shape: " + str(frecuencias.shape))

frecuencia_fundamental = frecuencias[transformada.argmax()]

if ((frecuencia_fundamental < 334.63) and (frecuencia_fundamental > 324.63)):
    print("La primer cuerda (E4) esta afinada")
if (frecuencia_fundamental == 335.23):
    print("La primer cuerda no esta muy bien afinada, debes soltarla más")
if (frecuencia_fundamental == 324.03):
    print("La primer cuerda no esta muy bien afinada, debes apretarla más")

if ((frecuencia_fundamental < 251.94) and (frecuencia_fundamental > 241.94)):
    print("La segunda cuerda (B3) esta bien afinada")
if (frecuencia_fundamental == 335.26):
    print("La segunda cuerda no esta muy bien afinada, debes soltarla más")
if (frecuencia_fundamental == 324.03):
    print("La segunda cuerda no esta muy bien afinada, debes apretarla más")

if ((frecuencia_fundamental < 201.00) and (frecuencia_fundamental > 191.00)):
    print("La tercer cuerda (G3) esta afinada")
if (frecuencia_fundamental == 201.60):
    print("La tercer cuerda no esta muy bien afinada, debes soltarla más")
if (frecuencia_fundamental == 191.60):
    print("La tercer cuerda no esta muy bien afinada, debes apretarla más")

if ((frecuencia_fundamental < 151.83) and (frecuencia_fundamental > 141.83)):
    print("La cuarta cuerda (D3) esta bien afinada")
if (frecuencia_fundamental == 152.43):
    print("La cuarta cuerda no esta muy bien afinada, debes soltarla más")
if (frecuencia_fundamental == 141.23):
    print("La cuarta cuerda no esta muy bien afinada, debes apretarla más")

if ((frecuencia_fundamental < 115.00) and (frecuencia_fundamental > 105.00)):
    print("La quinta cuerda (A2) esta afinada")
if (frecuencia_fundamental == 115.60):
    print("La quinta cuerda no esta muy bien afinada, debes soltarla más")
if (frecuencia_fundamental == 104.40):
    print("La quinta cuerda no esta muy bien afinada, debes apretarla más")

if ((frecuencia_fundamental < 87.41) and (frecuencia_fundamental > 77.41)):
    print("La sexta cuerda (E2) esta afinada")
if (frecuencia_fundamental == 88.01):
    print("La sexta cuerda no esta muy bien afinada, debes soltarla más")
if (frecuencia_fundamental == 76.81):
    print("La sexta cuerda no esta muy bien afinada, debes apretarla más")

print("Frecuencia fundamental: " + str(frecuencia_fundamental))

fig, ejes = plt.subplots(1,2)

ejes[0].plot(tiempos, grabacion[:, 0])
ejes[1].plot(frecuencias, np.abs(transformada))
plt.show()