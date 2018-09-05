#!/usr/bin/env python
# -*- coding: utf-8 -*-
# abrimos el archivo
archivo = open("lineas.txt","r") 
print("Algoritmo de Lyang Barsky\n\n")
print("A continuacion se le pediran los siguentes datos\n\n")
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
    a=(ysup - yi)/(yf-yi)
    if a >= 0 and a <=1:
    	xsupe=(xi+a*(xf-xi))#punto xsuperior
    	print("\n Analisis por el limite superior\n\n Usup: ",a,": Se encuentra dentro del parametro por lo tanto continuamos. \n")
    	if xsupe >= xizq and xsupe <= xder:
    		print("EL punto de recorte se encuentra en: (",xsupe,",",ysup,")")
    	else:
    		print("EL punto: (",xsupe,",",ysup,") no es punto recorte\n\n")
    		

    else:
   		print(" Analisis por el limite superior\n\n  Usup: ", a,"No se encuentra dentro del parametro por lo tanto no es punto de recorte.\n")
   	

   #analisis parametro inferior
    b=(yinf - yi)/(yf-yi)
    if b >=0 and b <= 1:
    	xinfe=(xi+b*(xf-xi)) #punto x inferior
    	print(" \n Analisis por el limite inferior\n\n  Uinf: ",b,": Se encuentra dentro del parametro por lo tanto continuamos. \n")
    	if xinfe >= xizq and xinfe <= xder:
    		print("EL punto de recorte se encuentra en: (",xinfe,",",yinf,")")
    	else:
    		print("EL punto (",xinfe,",",yinf,") no es punto recorte\n\n")
    
    else:
   		print(" Analisis por el limite inferior \n\n  Uinf: ", b,"No se encuentra dentro del parametro por lo tanto no es punto de recorte.\n")
#analisis parametro derecho
    c= (xder - xi)/(xf-xi)
    if c >= 0 and c <= 1:
    	yde=(yi+c*(yf-yi))#punto yderecho
    	print(" Analisis por el limite derecho\n\n  Uder: ",c,": Se encuentra dentro del parametro por lo tanto continuamos. \n")
    	if c > 0 and c < 1:
   			if yde >= yinf and yde<= ysup:
   				print("EL punto de recorte se encuentra en: (",xder,",",yde,")")
   				
   			else:
   				print("EL punto (",xder,",",yde,") no es punto recorte\n\n")

    else:
   		print("\n Analisis por el limite derecho\n\n  Uder: ", c,"No se encuentra dentro del parametro por lo tanto no es punto de recorte.\n")
#Analisis parametro izquierdo
    d=(xizq - xi)/(xf - xi)
    if d >= 0 and d <= 1:
    	yiz=(yi+d*(yf-yi)) #punto yizquierdo
    	print(" \n Analisis por el limite izquierdo\n\n  Uizq",d,": Se encuentra dentro del parametro por lo tanto continuamos. \n")
    	if yiz >= yinf and yiz<= ysup:
    		print("EL punto de recorte se encuentra en: (",xizq,",",yiz,")")
    	else: 
    		print("EL punto  (",xizq,",",yiz,") no es punto recorte\n\n")

    else:
   		print(" Analisis por el limite izquierdo\n\n Uizq", d,"No se encuentra dentro del parametro por lo tanto no es punto de recorte.\n")


archivo.close()#cerramos archivo