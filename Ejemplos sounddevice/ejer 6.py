# ejer 6
import numpy as np         # arrays    
import sounddevice as sd   # modulo de conexión con portAudio
import soundfile as sf     # para lectura/escritura de wavs
import kbhit               # para lectura de teclas no bloqueante

CHANNELS = 1
CHUNK = 2048


# leemos wav en array numpy (data)
# por defecto lee en formato dtype="float64". No hay problema para reproducción simple (hace conversiones internas)
data, SRATE = sf.read('piano.wav',dtype="float32")


class Sampler:
    # constructura de la clase
    def __init__(self, sample, iniChunk, endChunk):
        self.sample = np.copy(sample)
        self.iniChunk = iniChunk
        self.endChunk = endChunk
        self.looping = True
        self.actChunk = 0
    def nextChunk(self):
        if(self.looping and CHUNK * self.actChunk > self.endChunk):
            self.actChunk = self.iniChunk

        outChunk = self.sample[CHUNK * self.actChunk : CHUNK * (self.actChunk + 1)]
        self.actChunk += 1

        return outChunk
    def setLooping(self, bool):
        self.looping = bool

sampler = Sampler(data, 10, 15)
def callbackO(outdata, frames, time, status):
    outdata[:,0] = sampler.nextChunk()

stream = sd.OutputStream(
    samplerate = SRATE,            # frec muestreo 
    blocksize  = CHUNK,            # tamaño del bloque (muy recomendable unificarlo en todo el programa)
    channels   = 1,
    dtype = np.float32,
    callback=callbackO
    )  # num de canales

# arrancamos stream
stream.start()

kb = kbhit.KBHit()
# bloqueamos ejecucion para recoger respuesta
while True:
 if kb.kbhit():
        c = kb.getch()
        if(c == 'q'): sampler.setLooping(False)

kb.set_normal_term()


