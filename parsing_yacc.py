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
    
    # Let's start with plus 
    def p_expression_plus(self, p):
        # addition can be done between two numbers, and expression and a number and between two expressions  
        '''statement : NUMBER PLUS NUMBER''' 
        
        output = "%s + %s" % (p[1], p[3]) 
        p[0] = output

    # Let's add the minus operation
    def p_expression_minus(self, p):
        '''statement : NUMBER MINUS NUMBER''' 
        output = "%s - %s" % (p[1], p[3]) 
        p[0] = output

    # Let's add the multiplication operation
    def p_expression_times(self, p):
        '''statement : NUMBER TIMES NUMBER''' 
        output = "%s * %s" % (p[1], p[3]) 
        p[0] = output

    # Let's add the division operation
    def p_expression_divide(self, p):
        '''statement : NUMBER DIVIDE NUMBER''' 
        output = "%s / %s" % (p[1], p[3]) 
        p[0] = output

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




