  
# INTEGRANTES
# Luis Alberto Caballero Noguez A01282700
# Edgar Rubén Salazar Lugo A01338798
# Diego Alejandro Villarreal Lopez A01282555

import sys

# tokens
INT = 100  # Número entero
FLT = 101  # Número de punto flotante
OPB = 102  # Operador binario
LRP = 103  # Delimitador: paréntesis izquierdo
RRP = 104  # Delimitador: paréntesis derecho
LBS = 105  # Delimitador: bracket izquierdo
RBS = 106  # Delimitador: bracket derecho
END = 107  # Fin de la entrada
LOC = 108  # Condicional: ?
ROC = 109  # Condicional : 
OPA = 110  # Operador de asignación
OPR = 111  # Operador relacional
ORD = 112  # Operador relacional doble
IDE = 113  # Identificador
ERR = 200  # Error léxico: palabra desconocida

# Matriz de transiciones: codificación del AFD
# [renglón, columna] = [estado no final, transición]
# Estados > 99 son finales (ACEPTORES)
# Caso especial: Estado 200 = ERROR
#      dig   op   (    )    {    }  raro  esp  .   $    ?    :    =    <    >    !   ID
MT = [[  1, OPB, LRP, RRP, LBS, RBS,   4,   0, 4, END, LOC, ROC,   5,   7,   7,   9,   8], # edo 0 - estado inicial
      [  1, INT, INT, INT, INT, INT, INT, INT, 2, INT, INT, INT, INT, INT, INT, INT, INT], # edo 1 - dígitos enteros
      [  3, ERR, ERR, ERR, ERR, ERR,   4, ERR, 4, ERR, ERR, ERR, ERR, ERR, ERR, ERR, ERR], # edo 2 - primer decimal flotante
      [  3, FLT, FLT, FLT, FLT, FLT, FLT, FLT, 4, FLT, FLT, FLT, FLT, FLT, FLT, FLT, FLT], # edo 3 - decimales restantes flotante
      [ERR, ERR, ERR, ERR, ERR, ERR,   4, ERR, 4, ERR, ERR, ERR, ERR, ERR, ERR, ERR, ERR], # edo 4 - estado de error
      [OPA, OPA, OPA, OPA, OPA, OPA,   4, OPA, 4, OPA, OPA, OPA,   6, OPA, OPA, OPA, OPA], # edo 5 - primer =
      [ORD, ORD, ORD, ORD, ORD, ORD,   4, ORD, 4, ORD, ORD, ORD, ORD, ORD, ORD, ORD, ORD], # edo 6 - segundo =
      [OPR, OPR, OPR, OPR, OPR, OPR,   4, OPR, 4, OPR, OPR, OPR,   6, OPR, OPR, OPR, OPR], # edo 7 - primero operador operacional
      [IDE, IDE, IDE, IDE, IDE, IDE,   4, IDE, 4, IDE, IDE, IDE, IDE, IDE, IDE, IDE,   8], # edo 8 - identificador
      [ERR, ERR, ERR, ERR, ERR, ERR,   4, ERR, 4, ERR, ERR, ERR, ORD, ERR, ERR, ERR, ERR]] # edo 9 - !=

# Filtro de caracteres: regresa el número de columna de la matriz de transiciones
# de acuerdo al caracter dado
def filtro(c):
    """Regresa el número de columna asociado al tipo de caracter dado(c)"""
    if c == '0' or c == '1' or c == '2' or \
       c == '3' or c == '4' or c == '5' or \
       c == '6' or c == '7' or c == '8' or c == '9': # dígitos
        return 0
    elif c == '+' or c == '-' or c == '*' or \
         c == '/': # operadores
        return 1
    elif c == '(': # delimitador (
        return 2
    elif c == ')': # delimitador )
        return 3
    elif c == '{': # delimitador {
        return 4
    elif c == '}': # delimitador }
        return 5
    elif c == ' ' or ord(c) == 9 or ord(c) == 10 or ord(c) == 13: # blancos
        return 7
    elif c == '.': # punto
        return 8
    elif c == '$': # fin de entrada
        return 9
    elif c == '?': # operadores condicionales ? 
        return 10
    elif c == ':': # operadores condicionales ? 
        return 11
    elif c == '=': # operador relacional
        return 12
    elif c == '<': # operador relacional
        return 13
    elif c == '>': # operador relacional
        return 14
    elif c == '!': # operador relacional
        return 15
    elif (ord(c) >= 65 and ord(c) <= 90) or (ord(c) >= 97 and ord(c) <= 122): # identificadores
        return 16
    else: # caracter raro
        return 6

_c = None    # siguiente caracter
_leer = True # indica si se requiere leer un caracter de la entrada estándar

# Función principal: implementa el análisis léxico
def obten_token():
    """Implementa un analizador léxico: lee los caracteres de la entrada estándar"""
    global _c, _leer
    edo = 0 # número de estado en el autómata
    lexema = "" # palabra que genera el token
    while (True):
        while edo < 100:    # mientras el estado no sea ACEPTOR ni ERROR
            if _leer: _c = sys.stdin.read(1)
            else: _leer = True
            edo = MT[edo][filtro(_c)]
            if edo < 100 and edo != 0: lexema += _c
        if edo == INT:    
            _leer = False # ya se leyó el siguiente caracter
            print("Entero ", lexema)
            return INT
        elif edo == FLT:   
            _leer = False # ya se leyó el siguiente caracter
            print("Flotante ", lexema)
            return FLT
        elif edo == OPB:   
            lexema += _c  # el último caracter forma el lexema
            print("Operador ", lexema)
            return OPB
        elif edo == LRP:   
            lexema += _c  # el último caracter forma el lexema
            print("Delimitador ", lexema)
            return LRP
        elif edo == RRP:  
            lexema += _c  # el último caracter forma el lexema
            print("Delimitador ", lexema)
            return RRP
        elif edo == LBS:   
            lexema += _c  # el último caracter forma el lexema
            print("Delimitador ", lexema)
            return LBS
        elif edo == RBS:  
            lexema += _c  # el último caracter forma el lexema
            print("Delimitador ", lexema)
            return RBS            
        elif edo == END:
            print("Fin de expresion")
            return END
        elif edo == LOC:
            lexema += _c 
            print("Operador condicional ", lexema)
            return LOC
        elif edo == ROC:
            lexema += _c 
            print("Operador condicional ", lexema)
            return ROC
        elif edo == OPA:
            _leer = False
            print("Operador asignación ", lexema)
            return OPA
        elif edo == OPR:
            _leer = False
            print("Operador relacional ", lexema)
            return OPR
        elif edo == ORD:
            lexema += _c 
            print("Operador relacional ", lexema)
            return ORD
        elif edo == IDE:
            _leer = False
            print("Identificador ", lexema)
            return IDE
        else:   
            _leer = False # el último caracter no es raro
            print("ERROR! palabra ilegal", lexema)
            return ERR
            