from ply import yacc
import numpy as np

from parsing_lex import main, MyLexer

# Create a class that will build the yacc Parser 
# Based on the mode, it will either call the C or Python parser
class MyParser(object): 
    # Define the tokens that the parser will recognize 
    tokens = MyLexer.tokens

    # Handle print statements 
    def p_print_statement(self, p):
        '''statement : PRINT LPAREN STRING RPAREN'''
        # Based on the mode, we either want to call the C or Python print function 
        if self.mode == 'C':
            # return a print statement in C 
            output = "printf(%s);" % p[3] 
            # print(output)
            p[0] = output
        else:
            # return a print statement in Python 
            output = "print(%s)" % p[3] 
            # print(output)
            p[0] = output

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

    def parse(self, s): 
        # print("Parsing: %s" % s)    
        # print("Output:")
        # print(self.parser.parse(s))
        return self.parser.parse(s)


def main(input, mode):
    # Create a parser object
    parser = MyParser(mode)
    # Parse the input
    return parser.parse(input)

if __name__ == '__main__':
    main()




