#!/usr/bin/env python
# -*- coding: utf-8 -*-
# abrimos el archivo
"""Codigo elaborado por: Hugo Delgadillo Cortez
                         Diego Landeros Cerecero
                         Semestre 2019-1
                         Materia: Computacion Grafica     """
archivo = open("lineas.txt","r") 
print("Algoritmo de Liang Barsky\n\n")
print("A continuación se le pediran los siguentes datos\n\n")
print("a) El punto inferior izquierdo de la ventana")
print("b) Largo y ancho de la ventana")
print("\n\n")
#Datos de entrada de la ventana
xizq = float(input("Inserte el punto x de la ventana: "))
yinf = float(input("Inserte el punto y de la ventana: "))
h = float(input("Alto: "))
l = float(input("Largo: "))

ysup = yinf + h
xder = xizq + l

archivo.readline()
lcontador = 1 #inicio contador en 1 para omitir primera linea
for line in archivo: ##ciclo pera recorrer el archivo
   
    if(lcontador > 3): #maximo tres lineas
        break
    linea = line.split() #con esto omito los caracteres como espacio o saltos de linea
# Recorremos las lineas.
    xi = float(linea[0])
    yi = float(linea[1])
    xf = float(linea[2])
    yf = float(linea[3])
    print("*******************************************")
    print("*******************************************")
    print("Línea ", str(lcontador))#imprimo linea y recorro cada linea
    lcontador += 1
#analisis parametro superior
    try: #excepciones para division entre 0
        a=(ysup - yi)/(yf-yi)
        if a >= 0 and a <=1:
            xsupe=(xi+a*(xf-xi))#punto xsuperior
            print("\n Análisis por el límite superior\n\n Usup: ",a,": Se encuentra dentro del parametro por lo tanto continuamos. \n")
            if xsupe >= xizq and xsupe <= xder:
                print("EL punto de recorte se encuentra en: (",xsupe,",",ysup,")\n")
            else:
                print("EL punto: (",xsupe,",",ysup,") no tiene punto recorte\n\n")
        else:
            print(" Análisis por el límite superior\n\n  Usup: ", a,"No se encuentra dentro del parametro por lo tanto no tiene punto de recorte.\n")
    except:
        print("Analisis superior\n\n División entre cero, no tiene punto de recorte\n")
        
   #analisis parametro inferior
    try: #excepciones para division entre 0
        b=(yinf - yi)/(yf-yi)
        if b >=0 and b <= 1:
            xinfe=(xi+b*(xf-xi)) #punto x inferior
            print(" \n Análisis por el límite inferior\n\n  Uinf: ",b,": Se encuentra dentro del parametro por lo tanto continuamos. \n")
            if xinfe >= xizq and xinfe <= xder:
                print("EL punto de recorte se encuentra en: (",xinfe,",",yinf,")\n")
            else:
                print("EL punto (",xinfe,",",yinf,") no es punto recorte\n\n")
        else:
            print(" Análisis por el límite inferior \n\n  Uinf: ", b,"No se encuentra dentro del parametro por lo tanto no tiene punto de recorte.\n")
    except:
        print("Analisis inferior\n\n División entre cero, no tiene punto de recorte\n")

#analisis parametro derecho
    try:#excepciones para division entre 0
        c= (xder - xi)/(xf-xi)
        if c >= 0 and c <= 1:
            yde=(yi+c*(yf-yi))#punto yderecho
            print(" Análisis por el límite derecho\n\n  Uder: ",c,": Se encuentra dentro del parametro por lo tanto continuamos. \n")
            if yde >= yinf and yde<= ysup:
                print("EL punto de recorte se encuentra en: (",xder,",",yde,")\n")
            else:
                print("EL punto (",xder,",",yde,") no es punto recorte\n\n")
        else:
            print("\n Análisis por el limite derecho\n\n  Uder: ", c,"No se encuentra dentro del parametro por lo tanto no tiene punto de recorte.\n")
    except:
        print("Análisis derecho\n\n División entre cero, no tiene punto de recorte\n")
#Analisis parametro izquierdo
    try: #excepciones para division entre 0
        d=(xizq - xi)/(xf - xi)
        if d >= 0 and d <= 1:
            yiz=(yi+d*(yf-yi)) #punto yizquierdo
            print(" \n Análisis por el límite izquierdo\n\n  Uizq",d,": Se encuentra dentro del parametro por lo tanto continuamos. \n")
            if yiz >= yinf and yiz<= ysup:
                print("EL punto de recorte se encuentra en: (",xizq,",",yiz,")\n")
            else:
                print("EL punto  (",xizq,",",yiz,") no es punto recorte\n\n")
        else:
            print(" Análisis por el limite izquierdo\n\n Uizq", d,"No se encuentra dentro del parametro por lo tanto no tiene punto de recorte.\n")
    except:
        print("Análisis izquierdo\n\n División entre cero, no tiene punto de recorte\n")
         
archivo.close()#cerramos archivo