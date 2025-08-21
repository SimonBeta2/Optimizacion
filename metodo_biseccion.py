import matplotlib as plt
import math

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
    while abs(xu-xl)>error:
        xr = (xl+xu)/2
        if evaluacion(funcion1,xr)==0:
            return xr,iteraciones
        else:
            if evaluacion(funcion1,xl)*evaluacion(funcion1,xr)<0:
                xu = xr 
            else:
                if evaluacion(funcion1,xl)*evaluacion(funcion1,xr)>0:
                    xl = xr   
        iteraciones +=1
    return xr,iteraciones

#funcion = funcion()
#evaluacion = evaluacion(funcion,1)
#print(evaluacion)
print(biseccion())

