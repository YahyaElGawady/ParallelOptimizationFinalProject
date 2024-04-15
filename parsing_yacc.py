from ply import yacc
import numpy as np

from parsing import MyLexer

#importing token defs from lexer
lexer = MyLexer()
lexer.build()
tokens = lexer.tokens

#handling grammar rule -- print statement 


#handling grammar rule -- matrix multip

#handling grammar rule -- matrix addition

#handling grammar rule -- matrix sub

#handle grammar rule -- matrix

#handle syntax errors
def error(t):
    if t:
        print("Syntax ERROR at token: {t.value}")
    else:
        print("Syntax ERROR at EOF")

#Parser
def parser():
    parser = yacc.yacc(module=parsing_yacc)
    return parser

#testing



