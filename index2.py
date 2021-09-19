import math
# Ciclos
#4.1
def tablaConFor(numero):
    print("La tabla del ", numero, " es: ")
    for i in range(1,11):
        print(numero , "  X ", i , " = " , (numero * i))

#4.1
def tablaConWhile(numero):
     print("La tabla del ", numero, " es: ")
     i = 1
     while(i <= 10):
         print(numero , "  X ", i , " = " , (numero * i))
         i+=1

# 4.2
def secuenciaFor(inf,sup,salto):
    print("La secuencia entre ", inf, " y ", sup, " de ", salto, " en ", salto , " : " )
    for i in range(inf,sup + 1,salto):
        print(i)

#4.2
def secuenciaWhile(inf,sup,salto):
    i=inf
    print("La secuencia entre ", inf, " y ", sup, " de ", salto, " en ", salto , " : " )
    while(i <= sup):
         print(i)
         i+=salto

#4.3
def secuenciaPlus(inf,sup,salto,paridad):
     if(paridad == 0):
        print("La secuencia entre ", inf, " y ", sup, " de ", salto, " en ", salto , " y par es: " )
        for i in range(inf,sup,salto * 2):
            print(i)
     elif(paridad == 1):
         print("La secuencia entre ", inf, " y ", sup, " de ", salto, " en ", salto , " y impar es: " )
         i = inf
         while(i <= sup):
             i+=salto
             if(i % 2 == 1):
                 print(i)
     else:
        print("La secuencia entre ", inf, " y ", sup, " de ", salto, " en ", salto , " : " )
        for i in range(inf,sup,salto):
            print(i)


#4.4
def validarIngresos(inf,sup,valorParidad):
    if((inf > 0 and inf <= 100)):
        valido = True
    else:
        valido = False
    if(sup > 0 and sup <= 100):
        valido = True
    else:
        valido = False
    if(valorParidad >= 0 and valorParidad <= 2):
        valido = True
    else: 
        valido = False
    return valido
    

#4.4
def pedirDatosSecuenciaPlus():
    inf = int(input("Ingrese el numero inferior"))
    infValido = validarIngresos(inf)
    if(infValido != True):
        return "Error"
    sup = int(input("Ingrese el numero superior"))
    supValido = validarIngresos(sup)
    if(supValido != True):
        return "Error"
    salto = int(input("Ingrese el salto"))
    paridad = int(input("Ingrese la paridad"))
    paridadValido = validarIngresos(paridad)
    if(paridadValido != True):
        return "Error"
    numerosValidos = validarIngresos(inf,sup,paridad)
    resultado = secuenciaPlus(inf,sup,salto,paridad)
        
            
#4.5 
def esPrimo(n):
	if(n<2):
		return False
	root=int(math.sqrt(n))
	for a in range(2,root+1):
		if n % a==0:
			return False
	return True


def listadoNumerosSiniestros(numero):
    print("Numero primos entre 1 y ", numero)
    i = 1
    while(i <= numero):
        i+=1
        if(esPrimo(numero)):
            print(i)



def main():
    #tablaConFor(4) 4.1
    #tablaConWhile(6) 4.1
    #secuenciaFor(4,20,4) 4.2
    #secuenciaWhile(4,20,4) 4.3
    #pedirDatosSecuenciaPlus() 4.4
    resultado = esPrimo(2)
    print(resultado)
    #resultado= listadoNumerosSiniestros(57)
    #print(resultado)
main()