# Implementación de un parser
# Reconoce expresiones mediante la gramática:
# EXP -> EXP op EXP | EXP -> (EXP) | cte
# la cual fué modificada para eliminar ambigüedad a:
# EXP  -> cte EXP1 | (EXP) EXP1
# EXP1 -> op EXP EXP1 | vacío
# los elementos léxicos (delimitadores, constantes y operadores)
# son reconocidos por el scanner
#
# Autor: Dr. Santiago Conant, Agosto 2014 (modificado Agosto 2015)

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
    IDE,
    ERR
)

# Empata y obtiene el siguiente token
def match(tokenEsperado):
    global token

    # print('----')
    print(f"token {token}")
    print(f"token esperado {tokenEsperado}")
    print('----')

    if token == tokenEsperado:
        token = obten_token()
    else:
        # print("error")
        # print(token)
        # print(tokenEsperado)
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
    # else:
    #     error("Expresion mal hecha 2")

# Módulo que reconoce expresiones
def Cond():
    Arit()
    match(OPR) # match con operador relacional
    Mat()
    match(LOC) # match con delimitador ?
    Mat()
    match(ROC) # match con delimitador :
    Mat()
    Cond1()

# Módulo que reconoce expresiones
def Cond1():
    if token == OPR:
        match(token) # match con operador relacional
        Mat()
        match(LOC) # match con delimitador ?
        Mat()
        match(ROC) # match con delimitador :
        Mat()
        Cond1()
    # else:
    #     error("Expresion mal hecha 3")

# Módulo que reconoce expresiones
def Arit():

    if token == INT or token == FLT or token == IDE:
        match(token)
        Arit1()
    elif token == LRP:
        match(token) # match con delimitador (
        Arit()
        match(RRP) # match con delimitador )
        Arit1()
    else:
        print(token)
        error("Expresion mal hecha 4")

def Arit1():
    if token == OPB:
        match(token) # match con operador binario
        Arit()
        Arit1()
    # else:
    #     print(token)
    #     error("Expresion mal hecha 5")

# Termina con un mensaje de error
def error(mensaje):
    print("ERROR:", mensaje)
    sys.exit(1)

parser()