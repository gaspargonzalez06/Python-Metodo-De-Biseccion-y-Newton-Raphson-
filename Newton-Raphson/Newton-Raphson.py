#Parte II Newton raphson

import numpy
import pylab
from sympy import Symbol
from scipy.misc import derivative 


x=1.0
error=0.0001
maxit = 100
i=0
print("Metodo de Newton-Raphson")
print("x=%s error =%s  maxit=%s ")
print("i    x      x1      fx     fpx    error")
while True:
    #x=Symbol('x')
    fx=x**3+2*x**2+10*x-20
    fpx= 3*x**2+4*x+10

    #fx=input("Ingrese la funcion  =   ")
    #derivada=fx.diff(x)
    #f=lambda x:3*x*3+4*x+10
    #fpxtry=derivative(f,1.0,dx=1e-6)
   
    x1=x-(fx/fpx)
    e=abs(x1 - x)
    print("%s       %s      %s      %s      %s      %s" % (i,x,x1,fx,fpx,e))
    if e < error:
        print ("La Raiz de la funcion es %s" % x1)
        print("fx en la raiz seleccionada es %s " % {x1**3+2*x1**2+10*x1-20})
        break
    if i > maxit :
        
        print("Realice %s interaciones y no encotre la raiz de la funcion" %  i)
        break
    i = i +1
    x=x1
x= numpy.arange(-10,10,0.00001)
fx=x**3+2*x**2+10*x-20
pylab.plot(x,fx)
pylab.xlabel("x")
pylab.ylabel("fx")
pylab.title("fx=x**3+2*x**2+10*x-20")
pylab.grid(True)
pylab.show()