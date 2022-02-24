#reproductor simple 
import numpy as np         # arrays    
import sounddevice as sd   # modulo de conexión con portAudio
import soundfile as sf
from sqlalchemy import true     # para lectura/escritura de wavs
import kbhit 

# leemos wav en array numpy (data)
# por defecto lee en formato dtype="float64". No hay problema para reproducción simple (hace conversiones internas)
data, SRATE = sf.read('piano.wav',dtype="float32")


# informacion de wav
print("\n\nInfo del wav ",SRATE)
print("  Sample rate ",SRATE)
print("  Sample format: ",data.dtype)
print("  Num channels: ",len(data.shape))
print("  Len: ",data.shape[0])



kb = kbhit.KBHit()
c=''
while True:
 if kb.kbhit():
        c = kb.getch()
        if (c=='C'): sd.play(data, SRATE)
sd.wait()
 

        

# a reproducir!


# bloqueamos la ejecución hasta que acabe
