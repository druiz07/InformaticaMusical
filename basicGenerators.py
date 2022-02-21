#%%
import numpy as np
import matplotlib.pyplot as plt

SRATE = 44100  # sampling rate Hz

%matplotlib inline



# returns a sinusoidal signal with frec, dur, vol
def osc(frec,dur,vol):
    # number of samples requiered according to SRATE
    nSamples = int(SRATE*dur)
    return vol * np.sin(2*np.pi*np.arange(nSamples)*frec/SRATE)

def noise(dur,vol):
    # random(n)  -> [x0,x1,...xn-1] random sapples in [0,1)
    # xi*2-1   -> random sample in [-1,1]
    return vol*(2.0*np.random.random(int(SRATE*dur))-1.0)


# square, triangular, sawtooth can be generated by composing segments 


# obtains a segment between points (x0,y0) and (x1,y1) in the array v
# x0,x1 denote absolute positions (indexes) in v
def segment(v,x0,y0,x1,y1):
    # conversion of y0,y1 to floats
    y0, y1 = float(y0), float(y1)
    # increment of y between to samples
    step = (y1-y0)/(x1-x0)
    # some mathematics for getting the points
    for i in range(x0,x1):
        v[i] = y0+(i-x0)*step




# returns a signal with the specified segments interpreted as: 
# times (secs) =    [t1,t2,..,tn]    t0 is assumed to be 0
# vals         = [v0,v1,v2,..,vn]
def shape(times, vals): 
    # transformation of times to num of sample (index in the array)
    # adding 0 as the first sample
    nSamples = [0] + [int(SRATE*t) for t in times]
    # vector for generating the shape
    v = np.zeros(nSamples[-1],float)  # last sample = size of the vector   
    # generate the segments
    for i in range(1,len(nSamples)):
        segment(v,nSamples[i-1],vals[i-1],nSamples[i],vals[i])
    return v


# square shape of freq and dur by segments
def square(freq,dur):
    # base array
    v = np.zeros(SRATE*int(dur),dtype=float)
    # one cycle of the square wave. 
    # The value 1.0/SRATE is the duracion corresponding exactly to 1 sample
    s = shape([1/(freq*2), 1/(freq*2)+1.0/SRATE, 1/freq],
            [1,1,-1,-1])
    # concatenate cycles
    for i in range(len(v)):
        v[i] = s[i%len(s)]
    return v

# triangle ...

# sawtooth ...


s = square(1.8,2.3)
plt.plot(s)
plt.show()


