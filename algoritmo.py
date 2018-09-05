# funciones del parametro
def usup(ysup,yi,yf ):
   global a
   a=(ysup - yi)/(yf-yi)
   if a > 0 and a <1:
   		return print("*************************** \n usuperior\n\n",a,": Se encuentra dentro del parametro por lo tanto continuamos. \n")

   else:
   		return print("**************************\n usup\n\n", a,"No se encuentra dentro del parametro por lo tanto no es punto de recorte.\n")

#parametros de la ventana
def uinf(yinf,yi, yf):
    global b
    b=(yinf - yi)/(yf-yi)
    if b >0 and b < 1:
   		
   		return print("*************************** \n uinf\n\n",b,": Se encuentra dentro del parametro por lo tanto continuamos. \n")
    else:
   		return print("**************************\n uinf\n\n", b,"No se encuentra dentro del parametro por lo tanto no es punto de recorte.\n")


def uder(xder,xi,xf):
   global c
   c= (xder - xi)/(xf-xi)
   if c > 0 and c < 1:
   		return print("*************************** \n usuperior\n\n",c,": Se encuentra dentro del parametro por lo tanto continuamos. \n")

   else:
   		return print("**************************\n usup\n\n", c,"No se encuentra dentro del parametro por lo tanto no es punto de recorte.\n")


def uizq(xizq,xi,xf):
   global d
   d=(xizq - xi)/(xf - xi)
   if d > 0 and d < 1:
   		
   		return print("*************************** \n uizq\n\n",d,": Se encuentra dentro del parametro por lo tanto continuamos. \n")

   else:
   		return print("**************************\n uizq\n\n", d,"No se encuentra dentro del parametro por lo tanto no es punto de recorte.\n")
def xinf(b,xi,xf,xizq,yinf):
	if b > 0 and b < 1:
		xinfe=(xi+b*(xf-xi))
		if xinfe >= xizq and xinfe <= xder:
			print("EL punto de recorte se encuentra en: (",xinfe,",",yinf,")")
		return 0
		
	else:
		return  0
def yizq(d,yi,yf):
	if d > 0 and d < 1:
		yiz=(yi+d*(yf-yi))
		if yiz >= yinf and yiz<= ysup:
			print("EL punto de recorte se encuentra en: (",xizq,",",yiz,")")
		return 0
	else:
		return  0

def yder(c,yi,yf):
	if c > 0 and c < 1:
		yde=(yi+c*(yf-yi))
		if yde >= yinf and yde<= ysup:
			print("EL punto de recorte se encuentra en: (",xizq,",",yde,")")
		return 0 
	else:
		return  0
def xsup(a,xi,xf):
	if a > 0 and a < 1:
		xsupe=(xi+a*(xf-xi))
		if xsupe >= xizq and xsupe <= xder:
			print("EL punto de recorte se encuentra en: (",xsupe,",",yinf,")")
		return 0 
	else:
		return  0



print("Numeros de ventana")


# entrada de los puntos
yinf = float(input("Ingresa yinf: "))
ysup = float(input("Ingresa ysup: "))
xizq = float(input("Ingresa xizq: "))
xder = float(input("Ingresa xder: "))
xi = float(input("ingresa xi: "))
xf = float(input("Ingresa xf: "))
yi = float(input("Ingresa yi: "))
yf = float(input("Ingresa yf: "))


uinf(yinf,yi,yf)
uizq(xizq,xi,xf)
uder(xder,xi,xf)
usup(ysup,yi,yf)
print("**************************************************************************************")
print("\n\n\n")
xinf(b,xi,xf,xizq,yinf)
yder(c,yi,yf)
yizq(d,yi,yf)
xsup(a,xi,xf)
