#LAB 3
#EJER 1
# reproductor con Chunks
#%%
from re import A
from black import Enum
import numpy as np         # arrays    
import sounddevice as sd   # modulo de conexión con portAudio
import soundfile as sf     # para lectura/escritura de wavs
import kbhit
import basicGenerators as bas               # para lectura de teclas no bloqueante
import format_tools as ft
import math
from scipy import signal
import enum

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

#EJER 2
# reproductor con Chunks
#%%
from re import A
from black import Enum
import numpy as np         # arrays    
import sounddevice as sd   # modulo de conexión con portAudio
import soundfile as sf     # para lectura/escritura de wavs
import kbhit
import basicGenerators as bas               # para lectura de teclas no bloqueante
import format_tools as ft
import math
from scipy import signal
import enum
import matplotlib.pyplot as plt
CHUNK = 2048
SRATE = 44100
class Osc:
    class Shape(enum.Enum):
        sin = 0
        square = 1
        triangle = 2,
        saw = 3

    # constructura de la clase
    def __init__(self, frec = 1, shape = Shape.sin):
        self.frec = frec
        self.actChunk = 0
        self.type = shape
    # método suma
    
    def next(self):
        # dicc = {
        #     1: self.nextSin(),
        #     2: self.nextSquare(),
        #     3: self.nextSaw(),
        #     4: self.nextTriangle()
        # }
        # dicc.get(self.type, error)()
        if(self.type == 0):
            return self.nextSin()
        elif(self.type == 1):
            return self.nextSquare()
        elif(self.type == 2):
            return self.nextTriangle()
        elif(self.type == 3):
            return self.nextSaw()
       

    def nextSin(self):
        iniSample = self.actChunk*CHUNK
        endSample = (self.actChunk + 1)*CHUNK
        tempArray = np.zeros(CHUNK, dtype=np.float32)
        i = 0
        while(i < CHUNK):
            tempArray[i] = np.sin(((2*math.pi/SRATE)*(iniSample + i))*self.frec)
            i += 1
        self.actChunk += 1
        return tempArray
    def nextSquare(self):
        iniSample = self.actChunk*CHUNK
        endSample = (self.actChunk + 1)*CHUNK
        tempArray = np.zeros(CHUNK, dtype=np.float32)
        i = 0
        while(i < CHUNK):
            tempArray[i] = np.sin(((2*math.pi/SRATE)*(iniSample + i))*self.frec)
            if(tempArray[i] >= 0): 
                tempArray[i] = 1 
            else:
                tempArray[i] = -1
            i += 1
        self.actChunk += 1
        return tempArray
    def nextTriangle(self):
        iniSample = self.actChunk*CHUNK
        endSample = (self.actChunk + 1)*CHUNK
        tempArray = np.zeros(CHUNK, dtype=np.float32)
        i = 0
        while(i < CHUNK):
            tempArray[i] = 2*math.pi*np.arcsin(
                np.sin(((2*math.pi/SRATE)*(iniSample + i))*self.frec))
            i += 1
        self.actChunk += 1
        return tempArray
    def nextSaw(self):
        iniSample = self.actChunk*CHUNK
        endSample = (self.actChunk + 1)*CHUNK
        tempArray = np.zeros(CHUNK, dtype=np.float32)
        i = 0
        while(i < CHUNK):
            tempArray[i] = 2*math.pi*np.arctan(
                np.tan(((2*math.pi/SRATE)*(iniSample + i))*self.frec))
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

osc = Osc(1, 1)
# array1 = osc.next()
# array1 = np.concatenate((array1,osc.next()),axis=None)
# plt.plot(array1)
# plt.show()
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