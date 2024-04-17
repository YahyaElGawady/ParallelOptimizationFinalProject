from ply import yacc
import numpy as np

from parsing_lex import MyLexer

# Create a class that will build the yacc Parser 
# Based on the mode, it will either call the C or Python parser
class MyParser(object): 
    # Define the tokens that the parser will recognize 
    tokens = MyLexer.tokens

    # Handle print statements 

    # Handle binary numerical operations 

    # Handle if-statements

    # Create an error handler
    def p_error(self, p):
        print("Syntax error in input!")

    # Define the parser 
    def __init__(self, mode):
        self.lexer = MyLexer()
        self.parser = yacc.yacc(module=self)
        self.mode = mode

    def parse(self, s, mode):
        return self.parser.parse(s, lexer=self.lexer.lexer, mode=mode)





