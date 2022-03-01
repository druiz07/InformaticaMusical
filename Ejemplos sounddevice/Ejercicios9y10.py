#%%
# basic/record0.py Grabacion de un archivo de audio 'q' para terminar
import numpy as np         # arrays    
import sounddevice as sd   # modulo de conexión con portAudio
import soundfile as sf     # para lectura/escritura de wavs
import kbhit               # para lectura de teclas no bloqueante

CHANNELS = 1
CHUNK = 2048
SRATE = 44100

class Delay:
    # constructura de la clase
    def __init__(self,delayInSecs):
        # self.initialS = initialSample
        # print(self.initialS)
        self.delay= int(SRATE * delayInSecs)
        # 0s de silencio iniciales
        self.buffer = np.zeros(self.delay,dtype=np.float32)
        # self.actSample = 0
        # chunk / SRATE
    

    def delayChunk(self, inChunk):

        self.buffer = np.append(self.buffer, inChunk, axis=0)
       
        outChunk = self.buffer[:CHUNK]
       
        self.buffer = self.buffer[CHUNK:]
        
        return outChunk

# buffer para acumular grabación.
# (0,1): con un canal (1), vacio (de tamaño 0)
delay = Delay(1)
buffer = np.empty((0, 1), dtype="float32")
def callbackInput(indata, outdata, frames, time, status):
    global buffer
    global delay
    global CHUNK
    buffer = np.append(buffer,indata)    # buffer[:] = indata
    y = np.zeros(CHUNK, dtype=np.float32)
    i = 0
    while i < CHUNK:
        y[i] = buffer[i]
        i+=1
    temp = delay.delayChunk(y)
    buffer = buffer[CHUNK:]
    outdata[:, 0] = temp

# stream de entrada con callBack
stream = sd.Stream(
    samplerate=SRATE, dtype="float32",
    channels=CHANNELS,
    blocksize=CHUNK, 
    callback=callbackInput)
stream.start()

# delay = Delay(0.5)

# bucle para grabacion 
kb = kbhit.KBHit()

while not kb.kbhit(): 
    True

kb.set_normal_term()

# %%
