# Project Title

A brief description of what this project does.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Project Files](#project-files)

## Installation

### PLY installation

One of the packages needed for this project is PLY, which implements lex and yacc for Python. PLY requires Python 3.6 and above, so please update the version of Python if needed. 

Instructions on how to install this can be found here: https://pypi.org/project/ply/.  

Installing PLY can be done using pip:

```bash 
pip install ply
```

### CuPy installation 

The project also requires CuPy. First install the setup tools:

```bash 
python -m pip install -U setuptools pip
```



Then install CuPy:

```bash
pip install cupy-cuda12x
```

### Project installation

In order to try out this project, please clone this Github repository to access the files. 

## Project Files 

- `parsing_lex.py` - This file houses the lexical analyzer, or lexer, for the project. The lexer is responsible for breaking down the input source code into individual tokens, such as identifiers, keywords, operators, and literals. It defines rules to recognize these tokens based on regular expressions and generates tokens for consumption by the parser. The lexer plays a crucial role in the initial phase of the parsing process, providing the parser with a stream of tokens to analyze and parse.
- `parsing_yacc.py` - Within this file lies the parser for the project. The parser is responsible for analyzing the sequence of tokens generated by the lexer and determining whether they conform to the specified grammar rules of the programming language or domain-specific language being parsed. It utilizes parsing techniques to construct a parse tree or an abstract syntax tree (AST) representing the syntactic structure of the input code. In the context of this project, this file also determines which functions to call from either `pythonToC.py` or `pythonToPython2.py` in order to translate the code. 
- `parser.out` - This file usually contains information about the parser generated by PLY. It's primarily used for debugging purposes and understanding the behavior of the parser.
- `parsetab.py` - This file contains the tables and logic necessary for the parsing process. It's generated based on the grammar rules provided to the parsing tool. `parsetab.py` typically includes the parsing tables, which are data structures used by the parser to recognize the syntax of the input according to the specified grammar rules.
- `parsing_testing.ipynb` - This is a Python notebook that contains a series of unit tests centered around the application of the parser. In this tests, an input is defined. The input is then processed either by the Lexer or the Parser, and the output is printed out. 
- `pythonToC.py` - This file contains the Python to C translation functions which will then be called in `parsing_yacc.py`. 
- `pythonToPython2.py`  - This file containtains the NumPy to CuPy translation functions which will then be called in `parsing_yacc.py`. 

## Usage

Examples and instructions on how to use the project.