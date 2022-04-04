from gc import callbacks
import sounddevice as sd
import numpy as np

periodo_muestreo = 1.0 / 44100

# print(sd.query_devices())
# 2 Entrada
# 3 Salida

# indata: arreglo de numpy con la info recopilada por la tarjeta de sonido a traves del dispositivo de entrada
# outdata: arreglo de numpy que se le envirá al dispositivo de salida por default, es un silencio (puros 0´s)
# frames: el numero de muestra que tiene indta
# time: el tiempo que se lleva haciendo el stream
# status: si ha habido algun error
def callback_stream(indata, outdata, frames, time, status):
    global periodo_muestreo
    data = indata[:,0]
    transformada = np.fft.rfft(indata)
    frecuencias = np.fft.rfft(frames, periodo_muestreo)
    # print(indata.shape)
    print(
        "Frecuencia fundamental: ",
        frecuencias[np.argmax(np.abs(transformada))]
    )
    # outdata[:] = indata

try:
    with sd.Stream(
        device=(2,4),  # Se eligen dispositivos (Entrada, Salida)
        blocksize=0,   # 0 es que la tarjeta de sonido decide el mejor tamaño, e
        samplerate=11025, # Frecuencia de muestreo
        channels=1, # canales
        dtype=np.int16, # Tipo de dato (profundidad de bits)
        latency='hight', # Latencia, que tanto tiempo pasa de entrada hasta la salida
        callback=callback_stream
    ):
        print('Presiona una tecla para salir')
        input()
except Exception as e:
    print(str(e))