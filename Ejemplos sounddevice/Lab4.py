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
    
    mouseXC= ((mouseX*9900)/WIDTH)+100
    mouseYC= (mouseY*1)/HEIGHT
    mouseCoords=[mouseXC,mouseYC]
    return mouseCoords


kb = kbhit.KBHit()
c = ' '
fm = 0
beta = 1
frame = 0
fm = 300



screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Theremin")

mouseX=100
mouseY=0
while c!='q':   
 for event in pygame.event.get():
    if event.type == pygame.MOUSEMOTION:
      mouseX, mouseY = event.pos

    coords= scaleMouse(mouseX,mouseY)
    samples = oscFM(coords[0],fm,beta,coords[1],frame)
   
    stream.write(np.float32(0.5*samples)) 


stream.stop()
#%%
import numpy as np         # arrays    
import sounddevice as sd   # modulo de conexión con portAudio
import soundfile as sf     # para lectura/escritura de wavs
import pygame             
import kbhit
from pygame.locals import *
import os

SRATE = 44100
CHUNK = 1024

stream = sd.OutputStream(
    samplerate = SRATE,            # frec muestreo 
    blocksize  = CHUNK,            # tamaño del bloque (muy recomendable unificarlo en todo el programa)
    channels   = 1)  # num de canales




def KarplusStrong(frec, dur):
    N = SRATE // int(frec) # la frecuencia determina el tamanio del buffer
    buf = np.random.rand(N) * 2 - 1 # buffer inicial: ruido
    nSamples = int(dur*SRATE)
    samples = np.empty(nSamples, dtype="float32") # salida
    # generamos los nSamples haciendo recorrido circular por el buffer
    for i in range(nSamples):
        samples[i] = buf[i % N] # recorrido de buffer circular
        buf[i % N] = 0.5 * (buf[i % N] + buf[(1 + i) % N]) # filtrado
    return samples
# una nota


# tabla de ondas -> se copia la tabla cíclicamente hasta rellenenar un CHUNK
def synthWaveTable(wavetable, frame):
    samples = np.zeros(CHUNK)
    t = frame % len(wavetable)
    for i in range(CHUNK):
        samples[i] = wavetable[t]
        t = (t+1) % len(wavetable)
    return samples




baseFreq = 523.251

mayus= [2.0,
 2**(14/12),
 2**(16/12),
 2**(17/12),
 2**(19/12),
 2**(21/12),
 2**(23/12)]
minus= [1.0,1.12,1.19,1.33,1.5,1.59,1.78]
# tabla de ondas para un seno de 800 Hz: se almacena un ciclo
frec = 800
waveTables = [(KarplusStrong(baseFreq * minus[0],1)), (KarplusStrong(baseFreq * minus[1],1)), 
              (KarplusStrong(baseFreq * minus[2],1)), (KarplusStrong(baseFreq * minus[3],1)),
              (KarplusStrong(baseFreq * minus[4],1)), (KarplusStrong(baseFreq * minus[5],1)),
              (KarplusStrong(baseFreq * minus[6],1)), 
              (KarplusStrong(baseFreq * mayus[0],1)), (KarplusStrong(baseFreq * mayus[1],1)),
              (KarplusStrong(baseFreq * mayus[2],1)), (KarplusStrong(baseFreq * mayus[3],1)),
              (KarplusStrong(baseFreq * mayus[4],1)), (KarplusStrong(baseFreq * mayus[5],1)),
              (KarplusStrong(baseFreq * mayus[6],1)) ]

frame = 0
stream.start()
c=''
kb = kbhit.KBHit()

samplesSonando = np.array([waveTables[0], waveTables[1], waveTables[2]])
framesSonando = np.array([0,1500,4000])
while True:

    if kb.kbhit():
        c = kb.getch()
        if (c=='q'): 
             samplesSonando = np.append(samplesSonando, [waveTables[0]], axis=0)
             framesSonando = np.append([framesSonando], 0) 
        elif (c=='w'): 
             samplesSonando = np.append(samplesSonando, [waveTables[1]], axis=0)
             framesSonando = np.append([framesSonando], 0)
        elif (c=='e'): 
             samplesSonando = np.append(samplesSonando, [waveTables[2]], axis=0)
             framesSonando = np.append([framesSonando], 0)
        elif (c=='r'): 
            samplesSonando = np.append(samplesSonando, [waveTables[3]], axis=0)
            framesSonando = np.append([framesSonando], 0)
        elif (c=='t'): 
             samplesSonando = np.append(samplesSonando, [waveTables[4]], axis=0)
             framesSonando = np.append([framesSonando], 0)
        elif (c=='y'):
            samplesSonando = np.append(samplesSonando, [waveTables[5]], axis=0)
            framesSonando = np.append([framesSonando], 0)
        elif (c=='u'): 
            samplesSonando = np.append(samplesSonando, [waveTables[6]], axis=0)
            framesSonando = np.append([framesSonando], 0)

        elif (c=='z'):
            samplesSonando = np.append(samplesSonando, [waveTables[7]], axis=0)
            framesSonando = np.append([framesSonando], 0)
        elif (c=='x'):
            samplesSonando = np.append(samplesSonando, [waveTables[8]], axis=0)
            framesSonando = np.append([framesSonando], 0)
        elif (c=='c'): 
            samplesSonando = np.append(samplesSonando, [waveTables[9]], axis=0)
            framesSonando = np.append([framesSonando], 0)
        elif (c=='v'): 
            samplesSonando = np.append(samplesSonando, [waveTables[10]], axis=0)
            framesSonando = np.append([framesSonando], 0)
        elif (c=='b'): 
            samplesSonando = np.append(samplesSonando, [waveTables[11]], axis=0)
            framesSonando = np.append([framesSonando], 0)
        elif (c=='n'): 
            samplesSonando = np.append(samplesSonando, [waveTables[12]], axis=0)
            framesSonando = np.append([framesSonando], 0)
        elif (c=='m'): 
            samplesSonando = np.append(samplesSonando, [waveTables[13]], axis=0)
            framesSonando = np.append([framesSonando], 0)


    samples = np.zeros(CHUNK)
    indexDelete = np.empty(0)

    for i in range(samplesSonando.shape[0]):
        # aaaaaaaa =  len(samplesSonando.shape[0])
        samples += synthWaveTable(samplesSonando[i],framesSonando[i])
        framesSonando[i] += CHUNK
        if(framesSonando[i] > len(samplesSonando[i])-1500):
            indexDelete = np.append(indexDelete, i)
    #len(samplesSonando) no te da el número de indices, et dice lo que ocupa entero
    for x in range(len(indexDelete)):           
        samplesSonando = np.delete(samplesSonando, int(indexDelete[x]), 0)
        framesSonando = np.delete(framesSonando, int(indexDelete[x]),0)


    stream.write(np.float32(0.5*samples))
