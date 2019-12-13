from scipy import optimize
import numpy as np
def f(x):
    return (np.sin(np.cos(np.exp(x))))
root=optimize.bisect(f,-1,1)
print (root)
val=(np.sin(np.cos(np.exp(0.45158270529100264
))))
print (val)
#here val is not equal to zero because output number is less than the epsilon of the computer
