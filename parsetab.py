
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AND ARRAY BREAK COLON COMMA COMMENT DEF DIVIDE DOUBLE_EQUALS ELIF ELSE EQUALS FALSE FOR IF IN LIST LPAREN MINUS NONE NOT NP_ADD NP_DOT_PRODUCT NP_SUBTRACT NP_SUM NUMBER OR PLUS PRINT RANGE RETURN RPAREN STRING TIMES TRUE VARIABLE WHILEstatement : PRINT LPAREN STRING RPAREN \n                     | PRINT LPAREN NUMBER RPAREN\n                     | PRINT LPAREN statement RPARENstatement : NUMBER PLUS NUMBER \n                     | statement PLUS NUMBER\n                     | NUMBER PLUS statement\n                     | statement PLUS statementstatement : NUMBER MINUS NUMBER \n                     | statement MINUS NUMBER\n                     | NUMBER MINUS statement\n                     | statement MINUS statementstatement : NUMBER TIMES NUMBER \n                     | statement TIMES NUMBER\n                     | NUMBER TIMES statement\n                     | statement TIMES statementstatement : NUMBER DIVIDE NUMBER\n                     | statement DIVIDE NUMBER\n                     | NUMBER DIVIDE statement\n                     | statement DIVIDE statementstatement : LPAREN statement RPARENstatement : statement DOUBLE_EQUALS statement\n                     | NUMBER DOUBLE_EQUALS NUMBER\n                     | STRING DOUBLE_EQUALS STRING\n                     | statement DOUBLE_EQUALS NUMBER\n                     | NUMBER DOUBLE_EQUALS statement\n                     | statement DOUBLE_EQUALS STRING\n                     | STRING DOUBLE_EQUALS statement\n                     | STRING DOUBLE_EQUALS NUMBER\n                     | NUMBER DOUBLE_EQUALS STRINGstatement : IF statement COLON statementstatement : VARIABLE EQUALS ARRAY LPAREN LIST RPARENstatement : VARIABLE EQUALS NP_ADD LPAREN VARIABLE COMMA VARIABLE RPARENstatement : VARIABLE EQUALS NP_SUBTRACT LPAREN VARIABLE COMMA VARIABLE RPARENstatement : VARIABLE EQUALS NP_SUM LPAREN VARIABLE RPARENstatement : VARIABLE EQUALS NP_DOT_PRODUCT LPAREN VARIABLE COMMA VARIABLE RPAREN'
    
_lr_action_items = {'PRINT':([0,3,6,8,9,10,11,12,13,15,16,17,18,19,20,52,],[2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,]),'NUMBER':([0,3,6,8,9,10,11,12,13,15,16,17,18,19,20,52,],[5,5,5,24,26,28,30,32,35,40,41,43,45,47,49,5,]),'LPAREN':([0,2,3,6,8,9,10,11,12,13,15,16,17,18,19,20,52,53,54,55,56,57,],[3,13,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,62,63,64,65,66,]),'STRING':([0,3,6,8,9,10,11,12,13,15,16,17,18,19,20,52,],[4,4,4,4,4,4,4,33,34,38,4,4,4,4,51,4,]),'IF':([0,3,6,8,9,10,11,12,13,15,16,17,18,19,20,52,],[6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,]),'VARIABLE':([0,3,6,8,9,10,11,12,13,15,16,17,18,19,20,52,63,64,65,66,73,74,76,],[7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,68,69,70,71,77,78,79,]),'$end':([1,23,24,25,26,27,28,29,30,31,32,33,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,58,59,60,61,72,75,80,81,82,],[0,-7,-5,-11,-9,-15,-13,-19,-17,-21,-24,-26,-20,-23,-27,-28,-4,-6,-8,-10,-12,-14,-16,-18,-22,-25,-29,-1,-2,-3,-30,-31,-34,-32,-33,-35,]),'PLUS':([1,5,14,21,23,24,25,26,27,28,29,30,31,32,33,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,58,59,60,61,72,75,80,81,82,],[8,16,8,8,8,16,8,16,8,16,8,16,8,16,-26,16,8,-20,-23,8,16,16,8,16,8,16,8,16,8,16,8,-29,-1,-2,-3,8,-31,-34,-32,-33,-35,]),'MINUS':([1,5,14,21,23,24,25,26,27,28,29,30,31,32,33,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,58,59,60,61,72,75,80,81,82,],[9,17,9,9,9,17,9,17,9,17,9,17,9,17,-26,17,9,-20,-23,9,17,17,9,17,9,17,9,17,9,17,9,-29,-1,-2,-3,9,-31,-34,-32,-33,-35,]),'TIMES':([1,5,14,21,23,24,25,26,27,28,29,30,31,32,33,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,58,59,60,61,72,75,80,81,82,],[10,18,10,10,10,18,10,18,10,18,10,18,10,18,-26,18,10,-20,-23,10,18,18,10,18,10,18,10,18,10,18,10,-29,-1,-2,-3,10,-31,-34,-32,-33,-35,]),'DIVIDE':([1,5,14,21,23,24,25,26,27,28,29,30,31,32,33,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,58,59,60,61,72,75,80,81,82,],[11,19,11,11,11,19,11,19,11,19,11,19,11,19,-26,19,11,-20,-23,11,19,19,11,19,11,19,11,19,11,19,11,-29,-1,-2,-3,11,-31,-34,-32,-33,-35,]),'DOUBLE_EQUALS':([1,4,5,14,21,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,58,59,60,61,72,75,80,81,82,],[12,15,20,12,12,12,20,12,20,12,20,12,20,12,20,15,15,20,12,-20,15,12,20,20,12,20,12,20,12,20,12,20,12,15,-1,-2,-3,12,-31,-34,-32,-33,-35,]),'EQUALS':([7,],[22,]),'RPAREN':([14,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,58,59,60,61,67,70,72,75,77,78,79,80,81,82,],[37,-7,-5,-11,-9,-15,-13,-19,-17,-21,-24,-26,58,59,60,-20,-23,-27,-28,-4,-6,-8,-10,-12,-14,-16,-18,-22,-25,-29,-1,-2,-3,-30,72,75,-31,-34,80,81,82,-32,-33,-35,]),'COLON':([21,23,24,25,26,27,28,29,30,31,32,33,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,58,59,60,61,72,75,80,81,82,],[52,-7,-5,-11,-9,-15,-13,-19,-17,-21,-24,-26,-20,-23,-27,-28,-4,-6,-8,-10,-12,-14,-16,-18,-22,-25,-29,-1,-2,-3,-30,-31,-34,-32,-33,-35,]),'ARRAY':([22,],[53,]),'NP_ADD':([22,],[54,]),'NP_SUBTRACT':([22,],[55,]),'NP_SUM':([22,],[56,]),'NP_DOT_PRODUCT':([22,],[57,]),'LIST':([62,],[67,]),'COMMA':([68,69,71,],[73,74,76,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'statement':([0,3,6,8,9,10,11,12,13,15,16,17,18,19,20,52,],[1,14,21,23,25,27,29,31,36,39,42,44,46,48,50,61,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> statement","S'",1,None,None,None),
  ('statement -> PRINT LPAREN STRING RPAREN','statement',4,'p_print_statement','parsing_yacc.py',14),
  ('statement -> PRINT LPAREN NUMBER RPAREN','statement',4,'p_print_statement','parsing_yacc.py',15),
  ('statement -> PRINT LPAREN statement RPAREN','statement',4,'p_print_statement','parsing_yacc.py',16),
  ('statement -> NUMBER PLUS NUMBER','statement',3,'p_expression_plus','parsing_yacc.py',33),
  ('statement -> statement PLUS NUMBER','statement',3,'p_expression_plus','parsing_yacc.py',34),
  ('statement -> NUMBER PLUS statement','statement',3,'p_expression_plus','parsing_yacc.py',35),
  ('statement -> statement PLUS statement','statement',3,'p_expression_plus','parsing_yacc.py',36),
  ('statement -> NUMBER MINUS NUMBER','statement',3,'p_expression_minus','parsing_yacc.py',44),
  ('statement -> statement MINUS NUMBER','statement',3,'p_expression_minus','parsing_yacc.py',45),
  ('statement -> NUMBER MINUS statement','statement',3,'p_expression_minus','parsing_yacc.py',46),
  ('statement -> statement MINUS statement','statement',3,'p_expression_minus','parsing_yacc.py',47),
  ('statement -> NUMBER TIMES NUMBER','statement',3,'p_expression_times','parsing_yacc.py',53),
  ('statement -> statement TIMES NUMBER','statement',3,'p_expression_times','parsing_yacc.py',54),
  ('statement -> NUMBER TIMES statement','statement',3,'p_expression_times','parsing_yacc.py',55),
  ('statement -> statement TIMES statement','statement',3,'p_expression_times','parsing_yacc.py',56),
  ('statement -> NUMBER DIVIDE NUMBER','statement',3,'p_expression_divide','parsing_yacc.py',62),
  ('statement -> statement DIVIDE NUMBER','statement',3,'p_expression_divide','parsing_yacc.py',63),
  ('statement -> NUMBER DIVIDE statement','statement',3,'p_expression_divide','parsing_yacc.py',64),
  ('statement -> statement DIVIDE statement','statement',3,'p_expression_divide','parsing_yacc.py',65),
  ('statement -> LPAREN statement RPAREN','statement',3,'p_expression_parenthesis','parsing_yacc.py',71),
  ('statement -> statement DOUBLE_EQUALS statement','statement',3,'p_expression_equals','parsing_yacc.py',77),
  ('statement -> NUMBER DOUBLE_EQUALS NUMBER','statement',3,'p_expression_equals','parsing_yacc.py',78),
  ('statement -> STRING DOUBLE_EQUALS STRING','statement',3,'p_expression_equals','parsing_yacc.py',79),
  ('statement -> statement DOUBLE_EQUALS NUMBER','statement',3,'p_expression_equals','parsing_yacc.py',80),
  ('statement -> NUMBER DOUBLE_EQUALS statement','statement',3,'p_expression_equals','parsing_yacc.py',81),
  ('statement -> statement DOUBLE_EQUALS STRING','statement',3,'p_expression_equals','parsing_yacc.py',82),
  ('statement -> STRING DOUBLE_EQUALS statement','statement',3,'p_expression_equals','parsing_yacc.py',83),
  ('statement -> STRING DOUBLE_EQUALS NUMBER','statement',3,'p_expression_equals','parsing_yacc.py',84),
  ('statement -> NUMBER DOUBLE_EQUALS STRING','statement',3,'p_expression_equals','parsing_yacc.py',85),
  ('statement -> IF statement COLON statement','statement',4,'p_if_statement','parsing_yacc.py',91),
  ('statement -> VARIABLE EQUALS ARRAY LPAREN LIST RPAREN','statement',6,'p_numpy_array','parsing_yacc.py',103),
  ('statement -> VARIABLE EQUALS NP_ADD LPAREN VARIABLE COMMA VARIABLE RPAREN','statement',8,'p_numpy_add','parsing_yacc.py',125),
  ('statement -> VARIABLE EQUALS NP_SUBTRACT LPAREN VARIABLE COMMA VARIABLE RPAREN','statement',8,'p_numpy_subtract','parsing_yacc.py',142),
  ('statement -> VARIABLE EQUALS NP_SUM LPAREN VARIABLE RPAREN','statement',6,'p_numpy_sum','parsing_yacc.py',159),
  ('statement -> VARIABLE EQUALS NP_DOT_PRODUCT LPAREN VARIABLE COMMA VARIABLE RPAREN','statement',8,'p_numpy_dot_product','parsing_yacc.py',175),
]
