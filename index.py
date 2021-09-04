'''
def validar(txt,s):
    cond1 = (s in txt) and len(txt) % 7 == 0
    cond2 = len(s) % 2 == 1 and len(txt) % 2 == 1
    res = cond1 or cond2
    return res

print(validar("hhhhooo", "h")) 

'''

import random
import math

# Ejercicios Trigila

#1 Entrada/Salida/Variables/Operadores

# 1.1 
def pedirDataUser():
    inputUser = int(input("Ingrese un numero: "))
    print("Usted ingreso: " , inputUser)

# 1.2
def areaPerimetroRectangulo():
    ladoUno= int(input("Ingresar lado 1: "))
    ladoDos = int(input("Ingrese lado 2: "))
    calculoArea = ladoUno * ladoDos
    calculoPerimetro = (ladoUno * 2) + (ladoDos * 2)
    print("Area: " , calculoArea)
    print("Perimetro: " , calculoPerimetro)

# 1.3
def operaciones():
    numeroUno= int(input("Ingresar numero 1: "))
    numeroDos = int(input("Ingrese numero 2: "))
    print("Los resultados para " , numeroUno , " y ", numeroDos, " son: ")
    suma = numeroUno + numeroDos
    resta = numeroUno - numeroDos
    multiplicacion = numeroUno * numeroDos
    division = numeroUno / numeroDos
    print("La suma: " , suma)
    print("La resta: ", resta)
    print("La multiplicacion: ", multiplicacion)
    print("La division: ", division)

# 1.4 
def parteRealYEntera():
     numero= input("Ingrese un numero: ")
     divisionNumero = numero.split(".")
     print("Los resultados para ", numero, " son: ")
     print("Parte entera: " , divisionNumero[0])
     print("Parte decimal: 0.",divisionNumero[1])

# 2 Funciones

# 2.1
def convertir(segundosUser):
    dias = segundosUser // (60 * 60 * 24)
    segundosResultado = segundosUser % (60 * 60 * 24)
    horas = segundosResultado // (60 * 60 )
    segundosNumero = segundosResultado % (60 * 60)
    minutos = segundosNumero // 60
    segundos = segundosNumero % 60
    return dias  , " dias(s) " , horas , "hora(s)" , minutos , "minuto(s)", segundos , " segundos(s)"

# 2.1
def pedirSegundos():
    segundosNumero = int(input("Ingresar tiempo en segundos: "))
    salida = convertir(segundosNumero)
    print(salida)

# 2.2
def mostrarProducto(multiplicando,multiplicador):
    return

# 2.2
def pedirNumerosProducto():
    multiplicando = input("Ingrese el multiplicando: ")
    multiplicador = input("Ingrese el multiplicador: ")
    mostrarProducto(multiplicando, multiplicador)


# 2.4
def calcularLimite(numeroInferior,numeroSuperior):
    numeroEntre = random.randint(numeroInferior,numeroSuperior)
    return numeroEntre

# 2.5
def numeroAleatorio():
     numeroInferior = int(input("Ingrese el limite inferior: "))
     numeroSuperior = int(input("Ingrese el limite superior: "))
     primerLlamado = calcularLimite(numeroInferior,numeroSuperior)
     segundoLlamado = calcularLimite(primerLlamado,numeroSuperior)
     tercerLlamado = calcularLimite(numeroInferior,segundoLlamado)
     print("1-Limite inferior" , numeroInferior, " limite superior", numeroSuperior , "Numero generado: ", primerLlamado)
     print("1-Limite inferior" , primerLlamado, " limite superior", numeroSuperior , "Numero generado: ", segundoLlamado)
     print("1-Limite inferior" , numeroInferior, " limite superior", segundoLlamado , "Numero generado: ", tercerLlamado)
      

# 3 Condicionales

# 3.1
def operar(numeroUno,numeroDos, operador):
    if(operador == "+"):
        resultado = numeroUno + numeroDos
    elif(operador == "-"):
        resultado = numeroUno - numeroDos
    elif(operador == "*"):
        resultado = numeroUno * numeroDos
    elif(operador == "/"):
        resultado = numeroUno / numeroDos
    elif(operador == "**"):
        resultado = math.pow(numeroUno,numeroDos)
    else:
        return "Operador invalido"    
    return resultado    

# 3.1
def calculadora():
     numeroUno = int(input("Ingrese el numero uno: "))
     numeroDos = int(input("Ingrese el numero dos: "))
     operador = input("Ingrese la operacion: ")
     resultado = operar(numeroUno,numeroDos,operador)
     print(numeroUno , operador , numeroDos , " = " , resultado)


# 3.2

def definirNumero(numero):
    if(numero == 0 ):
        mensaje = "El numero es 0 y entero"
    
    return mensaje

def ingresarNumeroEvaluacion():
     numero = int(input("Ingrese un numero: "))
     definirNumero(numero)

def main():
    #1 Entrada/Salida/Variables/Operadores
    #pedirDataUser() 1.1
    #areaPerimetroRectangulo() 1.2
    #operaciones() 1.3
    #parteRealYEntera() 1.4
    # 2 Funciones
    #pedirSegundos() 2.1
    #pedirNumerosProducto 2.2
    #numeroAleatorio()  #2.4
    # 3 Condicionales
    #calculadora()  3.1
    ingresarNumeroEvaluacion() # 3.2


main()    
