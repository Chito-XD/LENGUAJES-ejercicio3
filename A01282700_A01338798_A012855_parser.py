
# INTEGRANTES
# Luis Alberto Caballero Noguez A01282700
# Edgar Rubén Salazar Lugo A01338798
# Diego Alejandro Villarreal Lopez A01282555

# ASIG = IDE = ( MAT )
# MAT = ARIT MAT1
# MAT1 = opr MAT ? MAT Cond1 | e
# cond = ARIT : ARIT
# Cond1 = opr MAT ? MAT : MAT COND1 | e
# ARIT = cte ARIT1 | ( ARIT ) ARIT1
# ARIT1 = opr ARIT ARIT1 | e


# Gramáticas
import sys
from A01282700_A01338798_A012855_obtener_token import (
    obten_token,
    INT, 
    FLT,
    OPB,
    LRP,
    RRP,
    END,
    LOC,
    ROC,
    OPA,
    OPR,
    IDE
)

# Empata y obtiene el siguiente token
def match(tokenEsperado):
    global token

    if token == tokenEsperado:
        token = obten_token()
    else:
        error("token equivocado")
        
# Función principal: implementa el análisis sintáctico
def parser():
    global token 
    token = obten_token() # inicializa con el primer token
    inicio()
    if token == END:
        print("Expresion bien construida!!")
    else:
        error("expresion mal terminada")

# Módulo que reconoce el inicio de la expresion
def inicio():
    asig()

# Módulo que reconoce expresiones
def asig():
    if token == IDE:
        match(token) # match con identificador
        match(OPA) # match con operador de asignación
        match(LRP)
        Mat()
        match(RRP)
    else:
        error("expresion mal terminada 1")

# Módulo que reconoce expresiones
def Mat():
    Arit()
    Mat1()

# Módulo que reconoce expresiones
def Mat1():
    if token == OPR:
        match(token) # match con operador relacional
        Mat()
        match(LOC) # match con operador ?
        Mat()
        match(ROC) # match con operador :
        Mat()
        Cond1()

# Módulo que reconoce expresiones condicionales
def Cond():
    if token == LOC or token == ROC:
        match(token)
        Arit()
        match(ROC)
        Arit()

# Módulo auxiñiar que reconoce expresiones condicionales
def Cond1():
    if token == OPR:
        match(token) # match con operador relacional
        Mat()
        match(LOC) # match con delimitador ?
        Mat()
        match(ROC) # match con delimitador :
        Mat()
        Cond1()

# Módulo que reconoce expresiones aritmeticas
def Arit():
    if token == INT or token == FLT or token == IDE:
        match(token)
        Arit1()
    elif token == LRP:
        match(token) # match con delimitador (
        Arit()
        
        Arit1()
        match(RRP) # match con delimitador )
    else:
        print(token)
        error("Expresion mal hecha 4")

# modulo auxiliar que reconocer expresiones aritmeticas
def Arit1():
    if token == OPB or token == OPR:
        match(token) # match con operador binario
        Arit()
        Arit1()
    if token == LOC or token == ROC:
        Cond()

# Termina con un mensaje de error
def error(mensaje):
    print("ERROR:", mensaje)
    sys.exit(1)

parser()