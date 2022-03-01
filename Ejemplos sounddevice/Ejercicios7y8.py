
# %%
#reproductor simple e
import numpy as np         # arrays    
import sounddevice as sd   # modulo de conexión con portAudio
import soundfile as sf
#from sqlalchemy import true     # para lectura/escritura de wavs
import kbhit 
from enum import Enum,unique

# leemos wav en array numpy (data)
# por defecto lee en formato dtype="float64". No hay problema para reproducción simple (hace conversiones internas)
data, SRATE = sf.read('piano.wav',dtype="float32")


# informacion de wav
print("\n\nInfo del wav ",SRATE)
print("  Sample rate ",SRATE)
print("  Sample format: ",data.dtype)
print("  Num channels: ",len(data.shape))
print("  Len: ",data.shape[0])




minus= [2.0,2.12,2.19,2.33,2.5,2.59,2.78]
mayus= [1.0,1.12,1.19,1.33,1.5,1.59,1.78]
c=''
kb = kbhit.KBHit()
while True:
 if kb.kbhit():
        c = kb.getch()
        if (c=='q'): sd.play(data, SRATE*minus[0])
        elif (c=='w'): sd.play(data, SRATE*minus[1])
        elif (c=='e'): sd.play(data, SRATE*minus[2])
        elif (c=='r'): sd.play(data, SRATE*minus[3])
        elif (c=='t'): sd.play(data, SRATE*minus[4])
        elif (c=='y'): sd.play(data, SRATE*minus[5])
        elif (c=='t'): sd.play(data, SRATE*minus[6])
        elif (c=='z'): sd.play(data, SRATE*mayus[0])
        elif (c=='x'): sd.play(data, SRATE*mayus[1])
        elif (c=='c'): sd.play(data, SRATE*mayus[2])
        elif (c=='v'): sd.play(data, SRATE*mayus[3])
        elif (c=='b'): sd.play(data, SRATE*mayus[4])
        elif (c=='n'): sd.play(data, SRATE*mayus[5])
        elif (c=='m'): sd.play(data, SRATE*mayus[6])

           
    

   
sd.wait()


# %%
