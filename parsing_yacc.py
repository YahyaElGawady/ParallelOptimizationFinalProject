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
        '''statement : PRINT LPAREN STRING RPAREN 
                     | PRINT LPAREN NUMBER RPAREN
                     | PRINT LPAREN statement RPAREN'''
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
        '''statement : NUMBER PLUS NUMBER 
                     | statement PLUS NUMBER
                     | NUMBER PLUS statement
                     | statement PLUS statement''' 
        
        output = "%s + %s" % (p[1], p[3]) 
        p[0] = output

    # Let's add the minus operation
    def p_expression_minus(self, p):
        '''statement : NUMBER MINUS NUMBER 
                     | statement MINUS NUMBER
                     | NUMBER MINUS statement
                     | statement MINUS statement''' 
        output = "%s - %s" % (p[1], p[3]) 
        p[0] = output

    # Let's add the multiplication operation
    def p_expression_times(self, p):
        '''statement : NUMBER TIMES NUMBER 
                     | statement TIMES NUMBER
                     | NUMBER TIMES statement
                     | statement TIMES statement''' 
        output = "%s * %s" % (p[1], p[3]) 
        p[0] = output

    # Let's add the division operation
    def p_expression_divide(self, p):
        '''statement : NUMBER DIVIDE NUMBER
                     | statement DIVIDE NUMBER
                     | NUMBER DIVIDE statement
                     | statement DIVIDE statement''' 
        output = "%s / %s" % (p[1], p[3]) 
        p[0] = output

    # Let's handle parenthesis in binary operations 
    def p_expression_parenthesis(self, p):
        '''statement : LPAREN statement RPAREN'''
        output = "(%s)" % p[2] 
        p[0] = output

    # Let's handle equals equals  
    def p_expression_equals(self, p):
        '''statement : statement DOUBLE_EQUALS statement
                     | NUMBER DOUBLE_EQUALS NUMBER
                     | STRING DOUBLE_EQUALS STRING
                     | statement DOUBLE_EQUALS NUMBER
                     | NUMBER DOUBLE_EQUALS statement
                     | statement DOUBLE_EQUALS STRING
                     | STRING DOUBLE_EQUALS statement
                     | STRING DOUBLE_EQUALS NUMBER
                     | NUMBER DOUBLE_EQUALS STRING'''
        output = "%s == %s" % (p[1], p[3]) 
        p[0] = output

    # Handle if-statements
    def p_if_statement(self, p):
        '''statement : IF statement COLON statement'''
        if self.mode == 'C':
            output = "if (%s) {\n\t%s\n}" % (p[2], p[4])
            p[0] = output
        else:
            output = "if %s:\n\t%s" % (p[2], p[4])
            p[0] = output

    # Handle numpy operations

    # Handle creating a numpy array from a list  
    def p_numpy_array(self, p):
        '''statement : ARRAY LPAREN LIST RPAREN'''
        if self.mode == 'C': 
            # Create a C array from the contents of the list 
            # Strip the brackets from the list 
            list_contents = p[3][1:-1] 
            # Get the length of the list 
            list_length = len(list_contents.split(',')) 
            # Create a C array
            output = "int array[%d] = {%s};" % (list_length, list_contents)
            p[0] = output
        else: 
            # TODO: Call the Python function 
            print("Converting numpy array to cupy array") 
            pass

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




