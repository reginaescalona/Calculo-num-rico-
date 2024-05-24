import numpy as np

#verifica los caracteres permitidos 
def verificar_digitos(cadena):
    caracteres_permitidos = "1234567890,=-."
    for caracter in cadena.replace("\n" , ""):
        if caracter not in caracteres_permitidos:
            print("No caracteres permitidos ")
            return False
    return True


#CREO UN VECTOR Y ESTE ME LEE LOS CARACTERES INVALIDOS  
def verificar_combinaciones_invalidas(cadena):
    cadena = cadena.replace(" ", "")
    datos_invalidos = [",,", ",=", ",.", "==", "=,", "=.", "--", "-,", "-=", "-.",
                            "..", ".=", ".-", ".,", "0-", "1-", "2-", "3-", "4-", "5-", "6-", "7-", "8-", "9-"]
    for combinaciones in datos_invalidos:
        if combinaciones in cadena:
            return False
    return True


#verifica si la entrada de datos esta correcta 
def formateo(cadena):
    lineas = cadena.replace(" ", "").split("\n")
    for linea in lineas:
        if(linea == ""):
            
            return False
        else:
            if linea[0] == "," or linea[0] == "=" or linea[0] == "."  or linea[len(linea) -1] == "," or linea[len(linea) -1] == "=" or linea[len(linea) -1] == "-" or linea[len(linea) -1] == "." :
                
                return False
    return True

#verifica si la fila tiene la sntaxis del =  bien
def iguales(cadena):
    lineas = cadena.replace(" ", "").split("\n")
    for linea in lineas:
        if str(linea).count("=") != 1:
            
            return False
    return True

#verifica que sea una matriz cuadrada
def es_cuadrada(cadena):
    lineas = cadena.replace(" ", "").split("\n")
    tamaño_columnas = len(lineas[0].split(","))
    tamaño_filas = len(lineas)
    if tamaño_columnas != tamaño_filas:
        
        return False
    for linea in lineas:
        fila = linea.split(",")
        if(tamaño_columnas != len(fila)):
            
            return False
    return True


def sacar_matrizA(cadena):
    lineas = cadena.replace(" " , "").split("\n")
    a = list()
    for linea in lineas:
        b = list()
        fila = linea.split(",")
        fila[len(fila) - 1] = fila[len(fila) - 1][0: fila[len(fila) - 1].index("=")]
        for i in fila:
            b.append(float(i))
        a.append(b)
    return a



def sacar_matrizB(cadena):
    lineas = cadena.replace(" " , "").split("\n")
    a = list()
    for linea in lineas:
        elemento = linea[linea.index("=")+1:]
        a.append(float(elemento))
    return a

def gaussElim(a,b):
    n = len(b)
   
    for k in range(0,n-1):
        for i in range(k+1,n):
            if a[i,k] != 0.0:
            
                landa = a [i,k]/a[k,k]
                
                a[i,k+1:n] = a[i,k+1:n] - landa*a[k,k+1:n]
                b[i] = b[i] - landa*b[k]
                
    for k in range(n-1,-1,-1):
        b[k] = (b[k] - np.dot(a[k,k+1:n],b[k+1:n]))/a[k,k]
    
    return b


def binario(cadena):
    for i in cadena:
        if i not in "01":
            return False
    return True


def ternario(cadena):
    for i in cadena:
        if i not in "012":
            return False
    return True




def octal(cadena):
    for i in cadena:
        if i not in "01234567":
            return False
    return True


def decimal(cadena):
    for i in cadena:
        if i not in "0123456789":
            return False
    return True


def hexadecimal(cadena):
    for i in cadena:
        if i not in "0123456789ABCDEFabcdef":
            return False
    return True


def llevar_decimal(numero , base):
    decimal = 0
    n = len(numero)-1
    if base == 16:
        for digito in numero:
            if digito == "A" or digito == "a":
                digito = 10
            elif digito == "B" or digito == "b":
                digito = 11
            elif digito == "C" or digito == "c":
                digito = 12
            elif digito == "D" or digito == "d":
                digito = 13
            elif digito == "E" or digito == "e":
                digito = 14
            elif digito == "F" or digito == "f":
                digito = 15
            decimal += int(digito)*base**n
            n-=1
    else:
        for digito in numero:
            decimal += int(digito)*base**n
            n-=1
    return decimal



def decimal_binario(numero):
    return bin(numero)[2:]


def decimal_ternario(numero):
    if numero == 0:
        return "0"
    ternario = ""
    while numero>0:
        ternario = str(numero%3) + ternario
        numero//=3
    return ternario



def decimal_octal(numero):
    return oct(numero)[2:]


def decimal_hexadecimal(numero):
    return hex(numero)[2:]


