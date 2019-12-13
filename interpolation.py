import numpy as np
import matplotlib.pyplot as plt
import scipy.interpolate
x= np.array([0,1,2,3,4,5])
y= np.array([1.0,2.0,1.0,0.5,4.0,8.0])
f= scipy.interpolate.InterpolatedUnivariateSpline(x,y,k=1)
f2= scipy.interpolate.InterpolatedUnivariateSpline(x,y,k=2)
f3= scipy.interpolate.InterpolatedUnivariateSpline(x,y,k=3)
f4= scipy.interpolate.lagrange(x,y)
plt.plot()
xs=np.linspace(0,5,100)
plt.plot(x,y,'o',xs,f(xs),xs,f2(xs),'-',xs,f3(xs),'--',xs,f4(xs))
plt.legend(['data','linear','quadratic','cubic','lagrange'])
plt.show()
