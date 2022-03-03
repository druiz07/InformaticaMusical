# #%% sintesis fm con osciladores variables

# import numpy as np         # arrays    
# import sounddevice as sd   # modulo de conexión con portAudio
# import soundfile as sf     # para lectura/escritura de wavs
# import kbhit
# import os  
# import pygame
# from pygame.locals import *          


# SRATE = 44100       # sampling rate, Hz, must be integer
# CHUNK = 1024
# WIDTH = 800
# HEIGHT = 300


# # fc, carrier = pitch, fm frecuencia moduladora, beta = indice de modulacion
# def oscFM(fc,fm,beta,vol,frame):
#     # sin(2πfc+βsin(2πfm))   http://www.mrcolson.com/2016/04/21/Simple-Python-FM-Synthesis.html
#     sample = np.arange(CHUNK)+frame
#     mod = beta*np.sin(2*np.pi*fm*sample/SRATE)
#     res = np.sin(2*np.pi*fc*sample/SRATE + mod)
#     return vol*res
    
# stream = sd.OutputStream(samplerate=SRATE,blocksize=CHUNK,channels=1)  
# stream.start()

# def scaleMouse(mouseX,mouseY):
    
#     mouseXC= ((mouseX*9900)/WIDTH)+100
#     mouseYC= (mouseY*1)/HEIGHT
#     mouseCoords=[mouseXC,mouseYC]
#     return mouseCoords


# kb = kbhit.KBHit()
# c = ' '

# fm = 
# beta = 1
# frame = 0
#fm = 300



# screen = pygame.display.set_mode((WIDTH, HEIGHT))
# pygame.display.set_caption("Theremin")

# mouseX=100
# mouseY=0
# while c!='q':   
#  for event in pygame.event.get():
#     if event.type == pygame.MOUSEMOTION:
#       mouseX, mouseY = event.pos

#     coords= scaleMouse(mouseX,mouseY)
#     samples = oscFM(coords[0],fm,beta,coords[1],frame)
   
#     stream.write(np.float32(0.5*samples)) 


# stream.stop()

# %%

import numpy as np         # arrays    
import sounddevice as sd   # modulo de conexión con portAudio
import soundfile as sf     # para lectura/escritura de wavs
import kbhit
import os  
import pygame
from pygame.locals import *   

SRATE = 44100       # sampling rate, Hz, must be integer
CHUNK = 1024

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
stream.write(KarplusStrong(440,2))

baseFreq = 523.251


# velocidades de reproduccion
mayus= [2.0,
 2**(14/12),
 2**(16/12),
 2**(17/12),
 2**(19/12),
 2**(21/12),
 2**(23/12)]
minus= [1.0,1.12,1.19,1.33,1.5,1.59,1.78]
c=''
kb = kbhit.KBHit()
while True:
 if kb.kbhit():
        c = kb.getch()
        if (c=='q'): sd.play(KarplusStrong(baseFreq * minus[0],1))
        elif (c=='w'): sd.play(KarplusStrong(baseFreq * minus[1],1))
        elif (c=='e'): sd.play(KarplusStrong(baseFreq * minus[2],1))
        elif (c=='r'): sd.play(KarplusStrong(baseFreq * minus[3],1))
        elif (c=='t'): sd.play(KarplusStrong(baseFreq * minus[4],1))
        elif (c=='y'): sd.play(KarplusStrong(baseFreq * minus[5],1))
        elif (c=='u'): sd.play(KarplusStrong(baseFreq * minus[6],1))
        elif (c=='z'): sd.play(KarplusStrong(baseFreq * mayus[0],1))
        elif (c=='x'): sd.play(KarplusStrong(baseFreq * mayus[1],1))
        elif (c=='c'): sd.play(KarplusStrong(baseFreq * mayus[2],1))
        elif (c=='v'): sd.play(KarplusStrong(baseFreq * mayus[3],1))
        elif (c=='b'): sd.play(KarplusStrong(baseFreq * mayus[4],1))
        elif (c=='n'): sd.play(KarplusStrong(baseFreq * mayus[5],1))
        elif (c=='m'): sd.play(KarplusStrong(baseFreq * mayus[6],1))
sd.wait()
# %%
