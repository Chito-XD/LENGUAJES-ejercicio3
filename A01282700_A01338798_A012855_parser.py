
# INTEGRANTES
# Luis Alberto Caballero Noguez A01282700
# Edgar Rubén Salazar Lugo A01338798
# Diego Alejandro Villarreal Lopez A01282555


# ASIG  -> ide opa EXP
# EXP   -> ARIT | {COND}
# COND  -> EXP opr EXP ? EXP : EXP
# ARIT  -> cte ARIT1 | ide ARIT1 | (ARIT) ARIT1 | {COND}
# ARIT1 -> opb ARIT ARIT1 | e


import sys
from A01282700_A01338798_A012855_obtener_token import (
    obten_token,
    INT, 
    FLT,
    OPB,
    LRP,
    RRP,
    LBS,
    RBS,
    END,
    LOC,
    ROC,
    OPA,
    OPR,
    ORD,
    IDE,
    ERR
)

# Empata y obtiene el siguiente token
def match(tokenEsperado):
    global token

    # print('----')
    # print(f"token {token}")
    # print(f"token esperado {tokenEsperado}")
    # print('----')

    if token == tokenEsperado:
        token = obten_token()
    else:
        error("token equivocado")
        

# Función principal: implementa el análisis sintáctico
def parser():
    global token 
    token = obten_token() # inicializa con el primer token
    asig()
    if token == END:
        print("Expresion bien construida!!")
    else:
        error("expresion mal terminada")

# Módulo que reconoce expresiones
def asig():
    if token == IDE:
        match(token) # match con identificador
        match(OPA) # match con operador de asignación
        exp()
    else:
        error("expresion mal terminada 1")

# Módulo que reconoce expresiones
def exp():
    if token == LBS:
        match(token) # match con delimitador {
        Cond()
        match(RBS) # match con delimitador }
    else:
        Arit()

# Módulo que reconoce expresiones
def Cond():
    exp()
    if token == OPR:
        match(OPR)
    elif token == ORD:
        match(ORD)
    exp()
    match(LOC)
    exp()
    match(ROC)
    exp()

# Módulo que reconoce expresiones
def Arit():
    if token == INT or token == FLT or token == IDE:
        match(token) # match con constante y variables
        Arit1()
    elif token == LRP:
        match(token) # match con delimitador (
        Arit()
        match(RRP) # match con delimitador )
        Arit1()

    elif token == LBS:
        match(token)
        Cond()
        match(RBS)
    else:
        print(token)
        error("Expresion mal hecha 4")

def Arit1():
    if token == OPB:     # or token == OPR:
        match(token) # match con operador binario
        Arit()
        Arit1()


# Termina con un mensaje de error
def error(mensaje):
    print("ERROR:", mensaje)
    sys.exit(1)

parser()