import numpy as np
import scipy.integrate as integ

def f(x):
    return(np.exp(x))

xs=np.linspace(0,1,1000)
print("Trapezoid",np.trapz(f(xs),x=xs)) #for trapezoid method
print("Simpson",integ.simps(f(xs),x=xs)) #for Simpson method 
print("Romberg",integ.romberg(f,0,1)) # for Romberg method
print("Gaussian",integ.fixed_quad(f,0,1)[0]) #for Gaussian method
