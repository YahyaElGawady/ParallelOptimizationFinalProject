# Import any necessary libraries
import ply.lex as lex 

# Define your parsing function(s) here
class MyLexer(object):
    # This is the class that will build the Lexer 

    # Let's have our Lexer handle reserved keywords 
    reserved = {
        'if': 'IF',
        'else': 'ELSE',
        'elif': 'ELIF',
        'while': 'WHILE',
        'for': 'FOR',
        'in': 'IN',
        'range': 'RANGE',
        'def': 'DEF',
        'return': 'RETURN',
        'True': 'TRUE',
        'False': 'FALSE',
        'None': 'NONE',
        'and': 'AND',
        'or': 'OR',
        'not': 'NOT',
        'break': 'BREAK',
    }

    # Define the tokens that the lexer will recognize 
    tokens = [
        'PRINT', 
        'STRING',
        'COMMENT', # This is a comment token that will be ignored by the lexer
        'NUMBER', # This is a number token that will be used to represent integers and floats
        'PLUS', # This is a token that will be used to represent the addition operation
        'MINUS', # This is a token that will be used to represent the subtraction operation
        'TIMES', # This is a token that will be used to represent the multiplication operation
        'DIVIDE', # This is a token that will be used to represent the division operation
        'EQUALS', # This is a token that will be used to represent the assignment operation
        'DOUBLE_EQUALS', # This is a token that will be used to represent the equality operation
        'LPAREN',
        'RPAREN',
        'COLON', # This is a token that will be used to represent the colon character
        # Add a token for a list object 
        'LIST', 
        # Add a token for an array object 
        'ARRAY',
        # Add a token for numpy add 
        'NP_ADD',
        # Add a token for numpy subtract
        'NP_SUBTRACT',
        # Add a token for numpy sum
        'NP_SUM',
        # Add a token for numpy dot product
        'NP_DOT_PRODUCT',
        #Add a token for numpy sin 
        'NP_SIN'
        #Add a token for numpy cos
        'NP_COS'
        #Add a token for nump exp
        'NP_EXP'
        #Add a token for numpy log
        'NP_LOG'
        #Add a token for numpy log10
        'NP_LOG10'
        #Add a token for numpy sqrt
        'NP_SQRT'
        #Add a token for numpy power
        'NP_POWER'
        #Add a token for numpy abs 
        'NP_ABS'
        #Add a token for sign
        'NP_SIGN'
        # Comma 
        'COMMA', 
        # Add a token for a variable
        'VARIABLE', 
    ] + list(reserved.values())

    # Define the regular expressions for the tokens
    t_PRINT = r'print'
    t_STRING = r'\".*?\"'
    t_PLUS = r'\+'
    t_MINUS = r'\-'
    t_TIMES = r'\*'
    t_DIVIDE = r'/'
    t_LPAREN = r'\('
    t_RPAREN = r'\)'
    t_EQUALS = r'='
    t_DOUBLE_EQUALS = r'=='
    t_COLON = r':'
    t_NUMBER = r'\d+'
    t_LIST = r'\[.*?\]' 
    # Array will come in the format np.array or numpy.array
    t_ARRAY = r'(?:np|numpy)\.(?:array)'
    # Numpy add will come in the format np.add or numpy.add
    t_NP_ADD = r'(?:np|numpy)\.(?:add)'
    # Numpy subtract will come in the format np.subtract or numpy.subtract
    t_NP_SUBTRACT = r'(?:np|numpy)\.(?:subtract)'
    # Numpy sum will come in the format np.sum or numpy.sum
    t_NP_SUM = r'(?:np|numpy)\.(?:sum)'
    # Numpy dot product will come in the format np.dot or numpy.dot
    t_NP_DOT_PRODUCT = r'(?:np|numpy)\.(?:dot)'
    #Numpy sin will come in format np.sin or numpy.sin
    t_NP_SIN = r'(?:np|numpy)\.(?:sin)'
    #Numpy cos will come in format np.cos or numpy.cos
    t_NP_COS = r'(?:np|numpy)\.(?:cos)'
    #Numpy exp will come in the format np.exp or numpy.exp
    t_NP_EXP = r'(?:np|numpy)\.(?exp)'
    #Numpy log will come in the format np.log or numpy.log
    t_NP_LOG = r'(?:np|numpy)\.(?log)'
    #Numpy log10 will come in the format np.log10 or numpy.log10
    t_NP_LOG10 = r'(?:np|numpy)\.(?log10)'
    #Numpy sqrt will come in format np.sqrt or numpy.sqrt
    t_NP_SQRT = r'(?:np|numpy)\.(?sqrt)'
    #Numpy power will come in format np.power or numpy.power
    t_NP_POWER = r'(?:np|numpy)\.(?power)' 
    #Numpy absolute will come in format np.abs or numpy.abs
    t_NP_ABS = r'(?:np|numpy)\.(?abs)'
    #Numpy sign will come in format np.sign or numpy.sign
    t_NP_SIGN = r'(?:np|numpy)\.(?sign)'
    t_COMMA = r','
    t_VARIABLE = r'(?!np\.|numpy\.)[a-zA-Z_][a-zA-Z_0-9]*'

    #  Handle if statements 
    def t_IF(self, t):
        r'if'
        return t
    
    # Handle else statements
    def t_ELSE(self, t):
        r'else'
        return t
    
    # Handle elif statements
    def t_ELIF(self, t):
        r'elif'
        return t

    # Define the function to ignore whitespace
    t_ignore = ' \t\n'

    # Define the function to ignore comments
    def t_COMMENT(self, t):
        r'\#.*'
        pass

    # Define the function to handle errors
    def t_error(self, t):
        print("Illegal character '%s'" % t.value[0])
        t.lexer.skip(1)

    # Define the function to build the lexer
    def build(self, **kwargs):
        self.lexer = lex.lex(module=self, **kwargs)

    # Define the function to test the lexer
    def test(self, data):
        self.lexer.input(data)
        while True:
            tok = self.lexer.token()
            if not tok:
                break
            print(tok)

def main(input):
    # Call your parsing function(s) here
    
    # Let input be a string that contains the code to be parsed 
    m = MyLexer() 
    m.build() 
    m.test(input)

if __name__ == "__main__":
    main()