# Import any necessary libraries
import ply.lex as lex 

# Define your parsing function(s) here
class MyLexer(object):
    # This is the class that will build the Lexer 

    # Let's start with having our Lexer recognize print statements 

    # Define the tokens that the lexer will recognize 
    tokens = (
        'PRINT',
        'STRING',
        'LPAREN',
        'RPAREN',
    ) 

    # Define the regular expressions for the tokens
    t_PRINT = r'print'
    t_STRING = r'\".*?\"'
    t_LPAREN = r'\('
    t_RPAREN = r'\)'

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