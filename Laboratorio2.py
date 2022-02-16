
#%%
#EJER 1
from array import array
from cmath import pi
from re import A
from sys import float_repr_style
import numpy as np  # alias np=numpy
# linea solo para sacar el gráfico en el notebook
%matplotlib inline
import random

import matplotlib.pyplot as plt
v = np.zeros(44100, dtype=np.float32)
# for x in v:
#   x = random.uniform(0, 2) - 1
#   print(x);
#   print(v);
  

v = [random.uniform(0, 2) - 1 for x in v]

# print(v)

x_ = np.arange(44100, dtype=np.int32)

# Plot the data
plt.plot(x_, v, label='x^2')

# La leyenda x^2
plt.legend()

# título 
plt.title("Una figura sencilla")

# mostrar el resultado
plt.show()



#%%
#EJER 2
import numpy as np  # alias np=numpy
# linea solo para sacar el gráfico en el notebook
%matplotlib inline
import random

import matplotlib.pyplot as plt
import math

srate=44100*2;



y_ = np.zeros(44100*2, dtype=np.float32)

i = 0
while(i < (44100*2)):
  y_[i]=np.sin(((2*math.pi/44100)*i)*3)
  i = i + 1


x_ = np.arange(44100*2, dtype=np.int32)

# Plot the data
plt.plot(x_, y_, label='x^2')

# La leyenda x^2
plt.legend()

# título 
plt.title("Una figura sencilla")

# mostrar el resultado
plt.show()
#%%
#EJER 3
import numpy as np  # alias np=numpy
# linea solo para sacar el gráfico en el notebook
%matplotlib inline
import random

import matplotlib.pyplot as plt
import math

SRATE=44100;

def osc(f,d):
  y_ = np.zeros(44100*d, dtype=np.float32)

  i = 0
  while(i < (44100*d)):
    y_[i]=np.sin(((2*math.pi/44100)*i)*f)
    i = i + 1


  x_ = np.arange(44100*d, dtype=np.int32)

  # Plot the data
  plt.plot(x_, y_, label='x^2')

  # La leyenda x^2
  plt.legend()

  # título 
  plt.title("Una figura sencilla")

  # mostrar el resultado
  plt.show()

osc(1,1)
osc(2,1)
osc(3,2)

#%%
#EJER 3 CONTINUACION
import numpy as np  # alias np=numpy
# linea solo para sacar el gráfico en el notebook
%matplotlib inline
import random

import matplotlib.pyplot as plt
import math

srate=44100*2;

def square(f,d):
  y_ = np.zeros(44100*d, dtype=np.float32)

  i = 0
  while(i < (44100*d)):
    value = np.sin(((2*math.pi/44100)*i)*f)
    if value > np.sin(math.pi): y_[i] = 1
    elif value < np.sin(math.pi): y_[i] = -1
    i = i + 1


  x_ = np.arange(44100*d, dtype=np.int32)

  # Plot the data
  plt.plot(x_, y_, label='x^2')

  # La leyenda x^2
  plt.legend()

  # título 
  plt.title("Una figura sencilla")

  # mostrar el resultado
  plt.show()


square(3,1)
# %%
#%%
import numpy as np  # alias np=numpy
# linea solo para sacar el gráfico en el notebook
%matplotlib inline
import random

import matplotlib.pyplot as plt
import math
from scipy import signal

srate=44100*2;

def square(f,d):
  y_ = np.zeros(44100*d, dtype=np.float32)

  i = 0
  while(i < (44100*d)):
    value = np.sin(((2*math.pi/44100)*i)*f)
    if value > np.sin(math.pi): y_[i] = 1
    elif value < np.sin(math.pi): y_[i] = -1
    i = i + 1


  x_ = np.arange(44100*d, dtype=np.int32)

  
  # Plot the data
  plt.plot(x_, y_, label='x^2')

  # La leyenda x^2
  plt.legend()

  # título 
  plt.title("Una figura sencilla")

  # mostrar el resultado
  plt.show()


square(3,1)
# %%
#EJER 4
import numpy as np  # alias np=numpy
# linea solo para sacar el gráfico en el notebook
%matplotlib inline
import random

import matplotlib.pyplot as plt
import math
from scipy import signal

def vol(sample,vol):
  i = 0
  while(i < sample.size):
    sample[i] *= vol
    i += 1 

y_ = np.arange(44100, dtype=np.float32)
print(y_)
vol(y_, 0.7)
print(y_)

def osc(f,d):
  y_ = np.zeros(44100*d, dtype=np.float32)
  
  i = 0
  while(i < (44100*d)):
    # sin 1,0
    # y_[i]= 0.5*(1+np.sin(((2*math.pi/44100)*i)*f)) 
    # sin -1, 1
    y_[i] = -np.sin(((2*math.pi/44100)*i)*f)
    i = i + 1


  x_ = np.arange(44100*d, dtype=np.int32)

  # Plot the data
  plt.plot(x_, y_, label='x^2')

  # La leyenda x^2
  plt.legend()

  # título 
  plt.title("Una figura sencilla")

  # mostrar el resultado
  plt.show()

  return y_

def modulaVol(sample,frec):
  # habria que comprobar tamaños
  oscilator = osc(frec, 1)
  i = 0
  print(oscilator.size, sample.size)
  while (i < 44100):
    sample[i] *= sample[i] * oscilator[i]
    i+= 1
  print(sample)
  return sample
modulaVol(y_, 1)

x_ = np.arange(44100, dtype=np.int32)

  
  # Plot the data
plt.plot(x_, y_, label='x^2')

  # La leyenda x^2
plt.legend()

  # título 
plt.title("Una figura sencilla")

  # mostrar el resultado
plt.show()

# %%
#EJER 5
import numpy as np  # alias np=numpy
# linea solo para sacar el gráfico en el notebook
%matplotlib inline
import random

import matplotlib.pyplot as plt
import math
from scipy import signal

def fadeOut(sample,t):
  i = 0
  distancia = sample.size - t;
  i = distancia
  while (t < sample.size):
    sample[t] = sample[t] * (1/distancia)*i
    t += 1
    i -= 1
  x_ = np.arange(44100, dtype=np.int32)

  
    # Plot the data
  plt.plot(x_, sample, label='x^2')

    # La leyenda x^2
  plt.legend()

    # título 
  plt.title("Una figura sencilla")

    # mostrar el resultado
  plt.show()

  return sample

def fadeIn(sample,t):
  i = 0
  distancia = t;
  i = 0
  while (i < t):
    sample[i] = sample[i] * (1/distancia)*i
    i += 1
  x_ = np.arange(44100, dtype=np.int32)

  
    # Plot the data
  plt.plot(x_, sample, label='x^2')

    # La leyenda x^2
  plt.legend()

    # título 
  plt.title("Una figura sencilla")

    # mostrar el resultado
  plt.show()

  return sample

SRATE=44100;

def osc(f,d):
  y_ = np.zeros(44100*d, dtype=np.float32)

  i = 0
  while(i < (44100*d)):
    y_[i]=np.sin(((2*math.pi/44100)*i)*f)
    i = i + 1
  return y_

fadeOutArraySin = fadeOut(osc(1,1), 20000)
fadeOutArrayLineal = fadeOut(
  (np.arange(44100, dtype=np.int32)),
  20000
)

arraySameNumber = np.zeros(44100,dtype=np.float32)
arraySameNumber.fill(10000)
fadeOutArraySameNumber = fadeOut(
   arraySameNumber,
  20000
)

arraySameNumber = np.zeros(44100,dtype=np.float32)
arraySameNumber.fill(10000)
fadeOutArraySameNumber = fadeIn(
   arraySameNumber,
  20000
)



# %%
#EJER 6
import numpy as np  # alias np=numpy
# linea solo para sacar el gráfico en el notebook
%matplotlib inline
import random

import matplotlib.pyplot as plt
import math
from scipy import signal
BUF_SIZE = 1024
SRATE = 44100
class Osc:
    # constructura de la clase
    def __init__(self, frec = 1):
        self.frec = frec
        self.actChunk = 0


        

    
    # método suma
    def next(self):
      iniSample = self.actChunk*BUF_SIZE
      endSample = (self.actChunk + 1)*BUF_SIZE
      tempArray = np.zeros(BUF_SIZE, dtype=np.float32)
      i = 0
      while(i < BUF_SIZE):
        tempArray[i] = np.sin(((2*math.pi/SRATE)*(iniSample + i))*self.frec)
        i += 1
      self.actChunk += 1
      return tempArray

        


osc = Osc()
array1 = osc.next()
i = 0
while (i < 44):
  array1 = np.concatenate((array1,osc.next()),axis=None)
  i += 1
x_ = np.arange(46080, dtype=np.float32)

  
    # Plot the data
plt.plot(x_, array1, label='x^2')

    # La leyenda x^2
plt.legend()

    # título 
plt.title("Una figura sencilla")

    # mostrar el resultado
plt.show()

# %%
