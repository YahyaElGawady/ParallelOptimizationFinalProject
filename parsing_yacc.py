from ply import yacc
import numpy as np
import pythonToC as pytoc
import pythonTopython2 as pytopy

from parsing_lex import main, MyLexer
# Create a class that will build the yacc Parser
# Based on the mode, it will either call the C or Python parser
class MyParser(object): 
    # Define the tokens that the parser will recognize 
    tokens = MyLexer.tokens

    #handling advanced expressions:

    #handling logical AND operator
    def p_expression_and(self, p):
        '''statement : NUMBER AND NUMBER 
                     | NUMBER AND statement
                     | statement AND NUMBER
                     | statement AND statement'''
        if self.mode == 'C':
            output = "%s && %s" % (p[1], p[3])
        else:
            output = "%s and %s" % (p[1], p[3])
        p[0] = output

    #handling logical OR operator
    def p_expression_or(self, p):
        '''statement : NUMBER OR NUMBER 
                     | NUMBER OR statement
                     | statement OR NUMBER
                     | statement OR statement'''
        if self.mode == 'C':
            output = "%s || %s" % (p[1], p[3])
        else:
            output = "%s or %s" % (p[1], p[3])
        p[0] = output

    
    #handling logical NOT operator
    def p_expression_not(self, p):
        '''statement : NOT NUMBER 
                     | NOT statement'''
        if self.mode == 'C':
            output = "!%s" % p[2]
        else: 
            output = "not %s" % p[2]
        p[0] = output

    
    #handling exponentiation 
    def p_expression_exponentiation(self, p):
        '''statement : NUMBER POWER NUMBER 
                     | NUMBER POWER statement
                     | statement POWER NUMBER
                     | statement POWER statement''' 
        if self.mode == 'C':
            output = "pow(%s, %s)" % (p[1], p[3]) 
        else:
            output = "%s ** %s" % (p[1], p[3]) 
        p[0] = output

    
    #handling increment operator
    def p_expression_increment(self, p):
        '''statement : INCREMENT NUMBER 
                     | INCREMENT statement
                     | INCREMENT VARIABLE'''
        if self.mode == 'C':
            output = "%s++" % p[2]
        else:
            output = "%s += 1" % p[2]
        p[0] = output 

    
    #handling decrement operator
    def p_expression_decrement(self, p):
        '''statement : DECREMENT NUMBER 
                     | DECREMENT statement
                     | DECREMENT VARIABLE'''
        if self.mode == 'C':
            output = "%s--" % p[2]
        else:
            output = "%s -= 1" % p[2]
        p[0] = output
    
    def p_expression_np_sin(self, p):
        '''statement : NP_SIN LPAREN statement RPAREN
                     | NP_SIN LPAREN NUMBER RPAREN'''
        if self.mode == 'C':
            output = "sin(%s)" % p[3]
        else:
           output = "np.sin(%s)" % p[3]
        p[0] = output


    def p_expression_np_cos(self, p):
        '''statement : NP_COS LPAREN statement RPAREN
                     | NP_COS LPAREN NUMBER RPAREN'''
        if self.mode == 'C':
            output = "cos(%s)" % p[3]
        else:
           output = "np.cos(%s)" % p[3]
        p[0] = output


    # Handle print statements 
    def p_print_statement(self, p):
        '''statement : PRINT LPAREN STRING RPAREN 
                     | PRINT LPAREN NUMBER RPAREN
                     | PRINT LPAREN statement RPAREN
                     | PRINT LPAREN VARIABLE RPAREN'''
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


    # Handling for loop with range 
    def p_for_loop(self, p):
        '''statement : FOR VARIABLE IN RANGE LPAREN NUMBER RPAREN COLON statement'''
        if self.mode == 'C':
            output = "for (int %s = 0; %s < %s; %s++) {\n\t%s\n}" % (p[2], p[2], p[6], p[2], p[9])
            p[0] = output
        else:
            output = "for %s in range(%s):\n\t%s" % (p[2], p[6], p[9])
            p[0] = output

    # Handle numpy operations

    # Handle creating a numpy array from a list  
    def p_numpy_array(self, p):
        '''statement : VARIABLE EQUALS ARRAY LPAREN LIST RPAREN'''
        # print("Creating a numpy array from a list")
        # Iterate through p 
        variable_name = p[1]
        list_values_with_brackets = p[5]
        list_values = list_values_with_brackets[1:-1]
        length_of_list = len(list_values.split(','))

        # print("Variable name: %s" % variable_name)
        # print("List values: %s" % list_values)

        if self.mode == 'C':
            #output = "int %s[%d] = {%s};" % (variable_name, length_of_list, list_values)
            output = pytoc.set_arr(variable_name, list_values_with_brackets,list_values, "test")
            p[0] = output
            pass
        else:
            # TODO: Call the Python function
            output = pytopy.array_to_py(variable_name, list_values)
            p[0] = output


    # Handle numpy add
    def p_numpy_add(self, p):
        '''statement : VARIABLE EQUALS NP_ADD LPAREN VARIABLE COMMA VARIABLE RPAREN'''
        # print("Adding two numpy arrays")
        # The inputs are p[5] and p[7]
        # print(p[5]) 
        # print(p[7])
        if self.mode == 'C': 
            # TODO: Call the C function
            result = pytoc.numpy_add_to_c(p[5],p[7],p[1])
            p[0]=result
            # print("Calling C function")
            pass 
        else:
            # TODO: Call the Python function 
            # print("Calling Python function")
            result = pytopy.numpy_add_to_py(p[5], p[7])
            p[0] = result

    # Handle numpy subtract
    def p_numpy_subtract(self, p):
        '''statement : VARIABLE EQUALS NP_SUBTRACT LPAREN VARIABLE COMMA VARIABLE RPAREN'''
        # print("Subtracting two numpy arrays")
        # Inputs are p[5] and p[7]
        if self.mode == 'C':
            # TODO: Call the C function
            result = pytoc.numpy_sub_to_c(p[5],p[7],p[1])
            p[0]= result
            # print("Calling C function")
            pass
        else:
            # TODO: Call the Python function
            # print("Calling Python function")
            result = pytopy.numpy_subtract_to_py(p[5], p[7])
            p[0] = result

    # Handle numpy sum
    def p_numpy_sum(self, p):
        '''statement : VARIABLE EQUALS NP_SUM LPAREN VARIABLE RPAREN'''
        # print("Summing a numpy array")
        # Input is p[5]
        if self.mode == 'C':
            # TODO: Call the C function
            result = pytoc.numpy_sum_to_c(p[5], p[1])
            p[0]=result
            # print("Calling C function")
            pass
        else:
            # TODO: Call the Python function
            # print("Calling Python function")
            result = pytopy.numpy_sum_to_py(p[5])
            p[0] = result

    # Handle numpy dot product
    def p_numpy_dot_product(self, p):
        '''statement : VARIABLE EQUALS NP_DOT_PRODUCT LPAREN VARIABLE COMMA VARIABLE RPAREN'''
        # print("Taking the dot product of two numpy arrays")
        # Inputs are p[5] and p[7]
        if self.mode == 'C':
            # TODO: Call the C function
            result = pytoc.numpy_dot_product_to_c(p[5],p[7],p[1])
            # print("Calling C function") 
            pass
        else:
            # TODO: Call the Python function
            # print("Calling Python function")
            result = pytopy.numpy_dot_to_py(p[5], p[7])
            p[0] = result

    def p_space(self, p):
        '''statement : '''
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




