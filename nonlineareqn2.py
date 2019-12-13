from scipy import optimize
import numpy as np
def f(x):
    return (np.sin(np.cos(np.exp(x))))
def g(x):
    return (-1*np.exp(x)*np.cos(np.cos(np.exp(x)))*np.sin(np.exp(x))) #derivative
root1= optimize.newton(f,-1,g)
root2= optimize.newton(f,-0.1,g)
print (root1,root2)

#On changing my initial guess the root changes and the reason is the different slope at these two points.



from scipy import optimize
import numpy as np
def f(x):
    return (np.sin(np.cos(np.exp(x))))
root3= optimize.newton(f,-0.1)
print ("secant method root=",root3)
