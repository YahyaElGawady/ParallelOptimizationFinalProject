
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'COLON COMMENT DEF DIVIDE DOUBLE_EQUALS ELIF ELSE EQUALS FALSE FOR IF IN LPAREN MINUS NONE NUMBER PLUS PRINT RANGE RETURN RPAREN STRING TIMES TRUE WHILEstatement : PRINT LPAREN STRING RPAREN'
    
_lr_action_items = {'PRINT':([0,],[2,]),'$end':([1,5,],[0,-1,]),'LPAREN':([2,],[3,]),'STRING':([3,],[4,]),'RPAREN':([4,],[5,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'statement':([0,],[1,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> statement","S'",1,None,None,None),
  ('statement -> PRINT LPAREN STRING RPAREN','statement',4,'p_print_statement','parsing_yacc.py',14),
]
