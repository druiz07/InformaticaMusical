#LAB 3
#EJER 1
import pyaudio, kbhit

from scipy.io import wavfile # para manejo de wavs
import numpy as np  # arrays    
from format_tools import *
import random

import math
from scipy import signal
CHUNK = 1024
SRATE = 44100
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
        




# arrancamos pyAudio
p = pyaudio.PyAudio()
bloque = np.arange(CHUNK, dtype=np.float32)

stream = p.open(format=p.get_format_from_width(getWidthData(bloque)),
                channels=1,
                rate=SRATE,
                frames_per_buffer=CHUNK,
                output=True)


kb = kbhit.KBHit()
osc = Osc()
c= ' '
while c!= 'q': 
    # nuevo bloque
    bloque = osc.next();  

    # pasamos al stream  haciendo conversion de tipo 
    stream.write(bloque.astype(bloque.dtype).tobytes())

    if kb.kbhit():
        c = kb.getch()

    if(c == 'F'): 
        osc.changeFrec(0.1)
    elif (c == 'f'):
        osc.changeFrec(-0.1)
    print('.',end='')

kb.set_normal_term()        
stream.stop_stream()
stream.close()
p.terminate()


