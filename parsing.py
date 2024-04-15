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
        'LPAREN',
        'RPAREN',
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

    # Define the function to ignore whitespace
    t_ignore = ' \t\n'

    # Define the function to recognize numbers
    def t_NUMBER(self, t):
        r'\d+'
        t.value = int(t.value)
        return t

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