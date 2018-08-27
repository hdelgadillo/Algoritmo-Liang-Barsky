# This function adds two numbers 
def usup(ysup,yi,yf ):
   a=(ysup - yi)/(yf-yi)
   if a > 0 and a <1:
   		return print("*************************** \n usuperior\n\n",a,": Se encuentra dentro del parametro por lo tanto continuamos. \n")

   else:
   		return print("**************************\n usup\n\n", a,"No se encuentra dentro del parametro por lo tanto no es punto de recorte.\n")

#parametros de la ventana
def uinf(yinf,yi, yf):
    b=(yinf - yi)/(yf-yi)
    if b >0 and b < 1:
   		return print("*************************** \n usuperior\n\n",b,": Se encuentra dentro del parametro por lo tanto continuamos. \n")

    else:
   		return print("**************************\n usup\n\n", b,"No se encuentra dentro del parametro por lo tanto no es punto de recorte.\n")


def uder(xder,xi,xf):
   c= (xder - xi)/(xf-xi)
   if c > 0 and c < 1:
   		return print("*************************** \n usuperior\n\n",c,": Se encuentra dentro del parametro por lo tanto continuamos. \n")

   else:
   		return print("**************************\n usup\n\n", c,"No se encuentra dentro del parametro por lo tanto no es punto de recorte.\n")


def uizq(xizq,xi,xf):
   d=(xizq - xi)/(xf - xi)
   if d > 0 and d < 1:
   		return print("*************************** \n usuperior\n\n",d,": Se encuentra dentro del parametro por lo tanto continuamos. \n")

   else:
   		return print("**************************\n usup\n\n", d,"No se encuentra dentro del parametro por lo tanto no es punto de recorte.\n")

print("Numeros de ventana")


# Take input from the user 
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