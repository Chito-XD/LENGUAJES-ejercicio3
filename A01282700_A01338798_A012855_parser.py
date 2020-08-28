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

# INTEGRANTES
# Luis Alberto Caballero Noguez A01282700
# Edgar Rubén Salazar Lugo A01338798
# Diego Alejandro Villarreal Lopez A01282555


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
    if token == tokenEsperado:
        token = obten_token()
    else:
        error("token equivocado")

# Función principal: implementa el análisis sintáctico
def parser():
    global token 
    token = obten_token() # inicializa con el primer token
    exp()
    if token == END:
        print("Expresion bien construida!!")
    else:
        error("expresion mal terminada")

# Módulo que reconoce expresiones
def exp():
    if token == INT or token == FLT:
        match(token) # reconoce Constantes
        exp1()
    elif token == LRP:
        match(token) # reconoce Delimitador (
        exp()
        match(RRP)
        exp1()
    else:
        error("expresion mal iniciada")

# Módulo auxiliar para reconocimiento de expresiones
def exp1():
    if token == OPB:
        match(token) # reconoce operador
        exp()
        exp1()

# Termina con un mensaje de error
def error(mensaje):
    print("ERROR:", mensaje)
    sys.exit(1)
    
        
parser()