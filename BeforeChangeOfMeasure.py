from   numpy.random import Generator, PCG64       #  numpy randon number generator routines
import numpy             as np
import matplotlib.pyplot as plt

#-------------------- The strategy simulator, an Ito integral  --------------------

def sim( n , x0, c, T):
    
    dt = T/n   # time step
    sqdt = np.sqrt(dt)  # standard deviation of dW
    
    dW = rg.normal(loc = 0., scale = sqdt, size = n)
    
    dX = 0
    W = x0
    for i in range(n):
        W = W + dW[i]
    
    X = np.sqrt(c)* W
    
    return X
    
        
#------------------ The main program ---------------------------------------------------

bg = PCG64(12345)        # instantiate a bit generator with seed 12345
rg = Generator(bg)       # instantiate a random number generator

#    Problem parameters

T   = 1.0          # final time 
x0  = 0            # initial value
c   = 0.25           # parameter a > 0
n   = 1000          # number of time steps
Np  = 1000            # number of experiment 
Nb  = 50             # number of bins for histogram
Ng1 = 0             # count the num. of samples that > 1

X = np.zeros([Np])
for path in range(Np):
    X[path] = sim( n, x0, c, T)

    
Xmax = X.max()
Xmin = X.min()
dX = ( Xmax - Xmin)/(Nb-1)
bc = np.zeros( Nb, dtype = int)

for path in range(Np):
    bin = int( ( X[path] - Xmin )/dX )
    bc[bin] += 1
    if X[path] > 1: 
        Ng1 = Ng1 + 1 

pdf = np.zeros( Nb)
for bin in range(Nb):
    pdf[bin] = bc[bin]/(Np)
    
Sax = np.linspace( Xmin, Xmax-dX, Nb)

pc = Ng1/Np 
print(pc)
print(-c*np.log(pc))






#        Setop for the cdf plots

fig, ax = plt.subplots()                       # Create a figure containing a single axes.

ax.plot( Sax, pdf, 'b*' )        # add this pdf to the figure
title = "PDF of X at T = 1 "
# title = title.format( T = T, mu = mu, sig1 = sig1)
ax.set_title(title)
ax.set_ylabel('PDF of the Stopping Time T = 1')
ax.set_xlabel('Bins')
ax.legend()
    
ax.grid()                  #  details of the plot, the grid for readibility

plt.show()

