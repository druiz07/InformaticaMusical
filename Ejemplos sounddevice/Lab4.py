#%% sintesis fm con osciladores variables

import numpy as np         # arrays    
import sounddevice as sd   # modulo de conexión con portAudio
import soundfile as sf     # para lectura/escritura de wavs
import kbhit
import os  
import pygame
from pygame.locals import *          


SRATE = 44100       # sampling rate, Hz, must be integer
CHUNK = 1024
WIDTH = 800
HEIGHT = 300


# fc, carrier = pitch, fm frecuencia moduladora, beta = indice de modulacion
def oscFM(fc,fm,beta,vol,frame):
    # sin(2πfc+βsin(2πfm))   http://www.mrcolson.com/2016/04/21/Simple-Python-FM-Synthesis.html
    sample = np.arange(CHUNK)+frame
    mod = beta*np.sin(2*np.pi*fm*sample/SRATE)
    res = np.sin(2*np.pi*fc*sample/SRATE + mod)
    return vol*res
    
stream = sd.OutputStream(samplerate=SRATE,blocksize=CHUNK,channels=1)  
stream.start()

def scaleMouse(mouseX,mouseY):
    
    mouseXC= (mouseX*10000)/WIDTH
    if mouseXC<100 : mouseXC=1000
    mouseYC= (mouseY*1)/HEIGHT
    if mouseYC<0: mouseYC=0
    mouseCoords=[mouseXC,mouseYC]
    return mouseCoords


kb = kbhit.KBHit()
c = ' '

fc = 440
fm = 300
beta = 1
vol = 0.8
frame = 0




screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Theremin")

mouseX=100
mouseY=0
while c!='q':   
 for event in pygame.event.get():
    if event.type == pygame.MOUSEMOTION:
      mouseX, mouseY = event.pos

    coords= scaleMouse(mouseX,mouseY)
    samples = oscFM(fc,coords[0],beta,coords[1],frame)
   
    stream.write(np.float32(0.5*samples)) 

    
    frame += CHUNK

stream.stop()

# %%

import numpy as np         # arrays    
import sounddevice as sd   # modulo de conexión con portAudio
import soundfile as sf     # para lectura/escritura de wavs
import kbhit
import os  
import pygame
from pygame.locals import *   


def KarplusStrong(frec, dur):
 N = SRATE // int(frec) # la frecuencia determina el tamanio del buffer
 buf = np.random.rand(N) * 2 - 1 # buffer inicial: ruido
 nSamples = int(dur*SRATE)

 samples = np.empty(nSamples, dtype=np.float32) # salida

 # generamos los nSamples haciendo recorrido circular por el buffer
 for i in range(nSamples):
     samples[i] = buf[i % N] # recorrido de buffer circular
     buf[i % N] = 0.5 * (buf[i % N] + buf[(1 + i) % N]) # filtrado
     return samples

stream = sd.OutputStream(samplerate=SRATE,blocksize=CHUNK,channels=1)  
stream.start()
stream.write(np.float32(KarplusStrong(1000,2)))



# %%
#Intento de juntar una tabla de ondas con el algoritmo 

import numpy as np         # arrays    
import sounddevice as sd   # modulo de conexión con portAudio
import soundfile as sf     # para lectura/escritura de wavs
import kbhit
import os  
import pygame
from pygame.locals import *          


SRATE = 44100       # sampling rate, Hz, must be integer
CHUNK = 1024
WIDTH = 800
HEIGHT = 300

#Algoritmo usando una tabla de ondas
def karplus_strong(wavetable, dur):
    """Synthesizes a new waveform from an existing wavetable, modifies last sample by averaging."""
    samples = []
    current_sample = 0
    previous_value = 0
    n_samples= int(dur*SRATE)

    while len(samples) < n_samples:
        wavetable[current_sample] = 0.5 * (wavetable[current_sample] + previous_value)
        samples.append(wavetable[current_sample])
        previous_value = samples[-1]
        current_sample += 1
        current_sample = current_sample % wavetable.size
    return np.array(samples)


def synthWaveTable(wavetable, frame):
    samples = np.zeros(CHUNK)
    t = frame % len(wavetable)
    for i in range(CHUNK):
        samples[i] = wavetable[t]
        t = (t+1) % len(wavetable)
        return samples

    
stream = sd.OutputStream(samplerate=SRATE,blocksize=CHUNK,channels=1)  
stream.start()

kb = kbhit.KBHit()
c = ' '
#Probamos con un seno de 800 hz
frec=800
waveTable = np.sin(2*np.pi*frec*np.arange(SRATE/frec)/SRATE)

while c!='q':   
    samples=synthWaveTable(waveTable,frame)
    stream.write(np.float32(0.5*karplus_strong(samples,1))) 
   
   

stream.stop()