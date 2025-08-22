import matplotlib.pyplot as plt
import numpy as np
import sympy as sp
def funcion():
    f = input("Ingrese la funcion: ")
    return f

def evaluacion(funcion,x):
    funcion1 = str(funcion)
    resultado = ""
    for i in range(len(funcion)):
        if funcion1[i] == "x":
            resultado += str(x)
        else:
            resultado += funcion1[i] 
    return float(eval(resultado))

def evaluacion1(funcion,x):
    funcion1 = str(funcion)
    numero = str(x)
    funcion1 = funcion1.replace("x", numero)
    return float(eval(funcion1))

def biseccion():
    iteraciones = 0
    funcion1 = funcion()
    xl = float(input("Ingrese el limite inferior del intervalo: "))
    xu = float(input("Ingrese el limite superior del intervalo: "))
    error = float(input("Ingrese el error: "))
    print("\niteraciones,xl,xu,xr,f(xr),f(xl)*f(xr),f(xu)*f(xr),error")
    while abs(xu-xl)>error:
        xr = (xl+xu)/2
        evaluacion1 = evaluacion(funcion1,xr)
        evaluacion2 = evaluacion(funcion1,xl)*evaluacion(funcion1,xr)
        evaluacion3 = evaluacion(funcion1,xl)*evaluacion(funcion1,xr)
        if evaluacion1==0:
            return xr,iteraciones
        else:
            if evaluacion2<0:
                xu = xr 
            else:
                if evaluacion3>0:
                    xl = xr   
        iteraciones +=1
        print(iteraciones,xl,xu,xr,evaluacion1,evaluacion2,evaluacion3,xu-xl)
    return funcion1,xr

def grafica(funcion,xr):
    puntosy=[]
    xl = int(input("Ingrese el limite inferior de la grafica: "))
    xu = int(input("Ingrese el limite superior de la grafica: "))
    puntosx = np.arange(xl,xu,0.1)
    raizx = xr
    raizy = evaluacion(funcion,xr)
    for i in range(len(puntosx)):
        puntosy.append(evaluacion(funcion,puntosx[i]))
    #print(puntosx,puntosy)
    
    plt.plot(puntosx,puntosy)
    plt.plot(raizx,raizy,"o")
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title(funcion)
    plt.show()

def grafica1(funcion,xr):
    x = sp.Symbol("x")
    f = sp.sympify(funcion)
    px = xr
    py = sp.Subs(f,x,px)

    g1 = sp.plot(f, (x, -10, 60))
    g2 = sp.plot(sp.Point(px,py))
    g1.extend(g2)
    g2.show()
    g1.show()


#funcion = funcion()
#evaluacion = evaluacion(funcion,1)
#print(evaluacion)
funcion, xr = biseccion()
grafica1(funcion, xr)

