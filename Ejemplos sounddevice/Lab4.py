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
