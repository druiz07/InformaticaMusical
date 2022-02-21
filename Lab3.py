#LAB 3
#EJER 1
# reproductor con Chunks
#%%
import numpy as np         # arrays    
import sounddevice as sd   # modulo de conexión con portAudio
import soundfile as sf     # para lectura/escritura de wavs
import kbhit
import basicGenerators as bas               # para lectura de teclas no bloqueante
import format_tools as ft
import math
from scipy import signal

CHUNK = 2048
SRATE = 44100
# leemos wav en array numpy (data)
# por defecto lee float64, pero podemos hacer directamente la conversion a float32
# data, SRATE = sf.read('piano.wav',dtype="float32")


# # informacion de wav
# print("\n\nInfo del wav ",SRATE)
# print("  Sample rate ",SRATE)
# print("  Sample format: ",data.dtype)
# print("  Num channels: ",len(data.shape))
# print("  Len: ",data.shape[0])


class Osc:
    # constructura de la clase
    def __init__(self, frec = 1):
        self.frec = frec
        self.actChunk = 0
    # método suma
    def next(self):
      iniSample = self.actChunk*CHUNK
      endSample = (self.actChunk + 1)*CHUNK
      tempArray = np.zeros(CHUNK, dtype=np.float32)
      i = 0
      while(i < CHUNK):
        tempArray[i] = np.sin(((2*math.pi/SRATE)*(iniSample + i))*self.frec)
        i += 1
      self.actChunk += 1
      return tempArray
    def changeFrec(self, newFrec):
        self.frec += newFrec

bloque = np.arange(CHUNK, dtype=np.float32)
# abrimos stream de salida
stream = sd.OutputStream(
    samplerate = SRATE,            # frec muestreo 
    blocksize  = CHUNK,            # tamaño del bloque (muy recomendable unificarlo en todo el programa)
    channels   = len(bloque.shape),
    dtype = np.float32
    )  # num de canales

# arrancamos stream
stream.start()


# En data tenemos el wav completo, ahora procesamos por bloques (chunks)
# bloque = np.arange(CHUNK,dtype=data.dtype)
numBloque = 0
kb = kbhit.KBHit()
c= ' '

vol = 1.0
nSamples = CHUNK 
print('\n\nProcessing chunks: ',end='')
osc = Osc(440)
# termina con 'q' o cuando el último bloque ha quedado incompleto (menos de CHUNK samples)
while c!= 'q' and nSamples==CHUNK: 
    # numero de samples a procesar: CHUNK si quedan sufucientes y si no, los que queden
    bloque = osc.next()
    print(bloque)
    bloque = ft.toFloat32(bloque)
    bloque *= vol
    # lo pasamos al stream
    stream.write(bloque) # escribimos al stream

    # modificación de volumen 
    if kb.kbhit():
        c = kb.getch()
        if (c=='v'): vol= max(0,vol-0.05)
        elif (c=='V'): vol= min(1,vol+0.05)
        print("Vol: ",vol)

    numBloque += 1
    print('.',end='')


print('end')
stream.stop()

# %%
