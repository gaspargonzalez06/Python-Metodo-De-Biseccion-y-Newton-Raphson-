import matplotlib.pyplot as plt
import numpy as np
from sympy import symbols
from sympy import lambdify
from sympy import sympify

print("")
x = symbols('x') # es una variable simbolica que se utilizara en la funcion
fn = sympify(input("Ingrese La Funcion")) #define la funcion quenos interesa
f = lambdify(x, fn)

#Iniciar las Variables

a=float(input("Ingrece el valor inicial de a : ")) #valor inicial de a
b=float(input("Ingrece el valor inicial de b : ")) #valor inicial de b
crit = float(input("Dame el criterio de paro o tolerancia"))  #valor de tolerancia
i=0 #contador inicial
ea=1   #variable de error inicial
x_anterior=0

#primera validacion inicial para verificar si la solucion esta en el intervalo ingresado
if f(a) * f(b) <0:

    #Encabezado de la tabla
    print("")
    print("{:^60}".format("Metodo De Biseccion"))
    print("{:^10} {:^10} {:^10} {:^10} {:^10}".format("i","a","b","xr","ea(%)"))

    while ea > crit:
        xr=(a+b)/2
        ea=abs((xr - x_anterior) / xr)

        if f(xr) * f(a) < 0:
            b=xr
        else:
            a=xr

        x_anterior=xr

        #Impresion de valores de Tabla
        print("{:^10} {:^10} {:^10} {:^10} {:^10}".format(i,a,b,xr,round(ea *100, 9)))
        i=i+1

    print("")
    print("El valor de x es ", round(xr,9),"con un error de ",round(ea *100 ,9),"%")

    #Graficar la funcion e indicar el punto
    xpts=np.linspace(-10,10) # Regresa un vector en numpy formado por n numeros con los mismo espacios

    plt.plot(xpts,f(xpts))
    plt.title("Grafica de la funcion")

    plt.axhline(color="black")
    plt.axvline(color="black")
    plt.scatter(xr,0, c="red")

    plt.annotate(round(xr, 9), xy=(xr, 0.5))

    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.grid(True,which='both')
    plt.ylim(-15 , 15)
    plt.show()


else: # f(a)*f(b) >=0

    # Si no hay raiz o bien se seleccionaron 2 raices en un intervalo
    print("La funcion no tiene una raiz en el intervalo de "+"x= "+str(a)+"a x= "+str(b))

    print("Ingrese otros valores iniciales")

    xpts=np.linspace(-10,10) # Regresa un vector en numpy formado por n numeros con los mismo espacios

    plt.plot(xpts,f(xpts))
    plt.title("Grafica de la funcion")

    plt.axhline(color="black")
    plt.axvline(color="black")
    
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.grid(True,which='both')
    plt.ylim(-15 , 15)
    plt.show()
