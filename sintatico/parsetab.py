
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'programaASSIGN BEGIN BOOLEAN COLON COMMA DIVIDE DO DOT ELSE END EQ ERROR_UNCLOSED_STRING GE GT ID IF INTEGER LE LPAREN LT MINUS NE NUM_INT NUM_REAL PLUS PROGRAM REAL RPAREN SEMI STRING THEN TIMES VAR WHILEprograma : PROGRAM ID SEMI bloco DOTbloco : parte_declaracoes_variaveis comando_compostoparte_declaracoes_variaveis : VAR declaracao_variaveis_list SEMI\n                                   | emptydeclaracao_variaveis_list : declaracao_variaveis\n                                 | declaracao_variaveis_list SEMI declaracao_variaveisdeclaracao_variaveis : lista_identificadores COLON tipolista_identificadores : ID\n                             | lista_identificadores COMMA IDtipo : INTEGER\n            | REAL\n            | BOOLEANcomando_composto : BEGIN comando_list ENDcomando_list : comando\n                    | comando_list SEMI comandocomando : atribuicao\n               | comando_composto\n               | comando_condicional\n               | comando_repetitivoatribuicao : ID ASSIGN expressaocomando_condicional : IF expressao THEN comando\n                           | IF expressao THEN comando ELSE comandocomando_repetitivo : WHILE expressao DO comandoexpressao : expressao_simples\n                 | expressao_simples relacao expressao_simplesrelacao : EQ\n               | NE\n               | LT\n               | LE\n               | GT\n               | GEexpressao_simples : termo\n                         | expressao_simples PLUS termo\n                         | expressao_simples MINUS termotermo : fator\n             | termo TIMES fator\n             | termo DIVIDE fatorfator : ID\n             | NUM_INT\n             | NUM_REAL\n             | LPAREN expressao RPARENempty :'
    
_lr_action_items = {'PROGRAM':([0,],[2,]),'$end':([1,9,],[0,-1,]),'ID':([2,7,11,23,24,25,27,29,30,38,48,49,50,51,52,53,54,55,56,57,58,59,61,70,],[3,15,22,35,35,15,45,22,35,35,22,35,35,35,-26,-27,-28,-29,-30,-31,35,35,22,22,]),'SEMI':([3,12,13,16,17,18,19,20,21,28,32,33,34,35,36,37,40,41,42,43,44,46,47,62,63,64,65,66,67,68,69,71,],[4,25,-5,29,-14,-16,-17,-18,-19,-13,-24,-32,-35,-38,-39,-40,-6,-7,-10,-11,-12,-15,-20,-21,-25,-33,-34,-36,-37,-41,-23,-22,]),'VAR':([4,],[7,]),'BEGIN':([4,6,8,11,25,29,48,61,70,],[-42,11,-4,11,-3,11,11,11,11,]),'DOT':([5,10,28,],[9,-2,-13,]),'IF':([11,29,48,61,70,],[23,23,23,23,23,]),'WHILE':([11,29,48,61,70,],[24,24,24,24,24,]),'COLON':([14,15,45,],[26,-8,-9,]),'COMMA':([14,15,45,],[27,-8,-9,]),'END':([16,17,18,19,20,21,28,32,33,34,35,36,37,46,47,62,63,64,65,66,67,68,69,71,],[28,-14,-16,-17,-18,-19,-13,-24,-32,-35,-38,-39,-40,-15,-20,-21,-25,-33,-34,-36,-37,-41,-23,-22,]),'ELSE':([18,19,20,21,28,32,33,34,35,36,37,47,62,63,64,65,66,67,68,69,71,],[-16,-17,-18,-19,-13,-24,-32,-35,-38,-39,-40,-20,70,-25,-33,-34,-36,-37,-41,-23,-22,]),'ASSIGN':([22,],[30,]),'NUM_INT':([23,24,30,38,49,50,51,52,53,54,55,56,57,58,59,],[36,36,36,36,36,36,36,-26,-27,-28,-29,-30,-31,36,36,]),'NUM_REAL':([23,24,30,38,49,50,51,52,53,54,55,56,57,58,59,],[37,37,37,37,37,37,37,-26,-27,-28,-29,-30,-31,37,37,]),'LPAREN':([23,24,30,38,49,50,51,52,53,54,55,56,57,58,59,],[38,38,38,38,38,38,38,-26,-27,-28,-29,-30,-31,38,38,]),'INTEGER':([26,],[42,]),'REAL':([26,],[43,]),'BOOLEAN':([26,],[44,]),'THEN':([31,32,33,34,35,36,37,63,64,65,66,67,68,],[48,-24,-32,-35,-38,-39,-40,-25,-33,-34,-36,-37,-41,]),'DO':([32,33,34,35,36,37,39,63,64,65,66,67,68,],[-24,-32,-35,-38,-39,-40,61,-25,-33,-34,-36,-37,-41,]),'RPAREN':([32,33,34,35,36,37,60,63,64,65,66,67,68,],[-24,-32,-35,-38,-39,-40,68,-25,-33,-34,-36,-37,-41,]),'PLUS':([32,33,34,35,36,37,63,64,65,66,67,68,],[50,-32,-35,-38,-39,-40,50,-33,-34,-36,-37,-41,]),'MINUS':([32,33,34,35,36,37,63,64,65,66,67,68,],[51,-32,-35,-38,-39,-40,51,-33,-34,-36,-37,-41,]),'EQ':([32,33,34,35,36,37,64,65,66,67,68,],[52,-32,-35,-38,-39,-40,-33,-34,-36,-37,-41,]),'NE':([32,33,34,35,36,37,64,65,66,67,68,],[53,-32,-35,-38,-39,-40,-33,-34,-36,-37,-41,]),'LT':([32,33,34,35,36,37,64,65,66,67,68,],[54,-32,-35,-38,-39,-40,-33,-34,-36,-37,-41,]),'LE':([32,33,34,35,36,37,64,65,66,67,68,],[55,-32,-35,-38,-39,-40,-33,-34,-36,-37,-41,]),'GT':([32,33,34,35,36,37,64,65,66,67,68,],[56,-32,-35,-38,-39,-40,-33,-34,-36,-37,-41,]),'GE':([32,33,34,35,36,37,64,65,66,67,68,],[57,-32,-35,-38,-39,-40,-33,-34,-36,-37,-41,]),'TIMES':([33,34,35,36,37,64,65,66,67,68,],[58,-35,-38,-39,-40,58,58,-36,-37,-41,]),'DIVIDE':([33,34,35,36,37,64,65,66,67,68,],[59,-35,-38,-39,-40,59,59,-36,-37,-41,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'programa':([0,],[1,]),'bloco':([4,],[5,]),'parte_declaracoes_variaveis':([4,],[6,]),'empty':([4,],[8,]),'comando_composto':([6,11,29,48,61,70,],[10,19,19,19,19,19,]),'declaracao_variaveis_list':([7,],[12,]),'declaracao_variaveis':([7,25,],[13,40,]),'lista_identificadores':([7,25,],[14,14,]),'comando_list':([11,],[16,]),'comando':([11,29,48,61,70,],[17,46,62,69,71,]),'atribuicao':([11,29,48,61,70,],[18,18,18,18,18,]),'comando_condicional':([11,29,48,61,70,],[20,20,20,20,20,]),'comando_repetitivo':([11,29,48,61,70,],[21,21,21,21,21,]),'expressao':([23,24,30,38,],[31,39,47,60,]),'expressao_simples':([23,24,30,38,49,],[32,32,32,32,63,]),'termo':([23,24,30,38,49,50,51,],[33,33,33,33,33,64,65,]),'fator':([23,24,30,38,49,50,51,58,59,],[34,34,34,34,34,34,34,66,67,]),'tipo':([26,],[41,]),'relacao':([32,],[49,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> programa","S'",1,None,None,None),
  ('programa -> PROGRAM ID SEMI bloco DOT','programa',5,'p_programa','parser.py',9),
  ('bloco -> parte_declaracoes_variaveis comando_composto','bloco',2,'p_bloco','parser.py',14),
  ('parte_declaracoes_variaveis -> VAR declaracao_variaveis_list SEMI','parte_declaracoes_variaveis',3,'p_parte_declaracoes_variaveis','parser.py',18),
  ('parte_declaracoes_variaveis -> empty','parte_declaracoes_variaveis',1,'p_parte_declaracoes_variaveis','parser.py',19),
  ('declaracao_variaveis_list -> declaracao_variaveis','declaracao_variaveis_list',1,'p_declaracao_variaveis_list','parser.py',23),
  ('declaracao_variaveis_list -> declaracao_variaveis_list SEMI declaracao_variaveis','declaracao_variaveis_list',3,'p_declaracao_variaveis_list','parser.py',24),
  ('declaracao_variaveis -> lista_identificadores COLON tipo','declaracao_variaveis',3,'p_declaracao_variaveis','parser.py',28),
  ('lista_identificadores -> ID','lista_identificadores',1,'p_lista_identificadores','parser.py',32),
  ('lista_identificadores -> lista_identificadores COMMA ID','lista_identificadores',3,'p_lista_identificadores','parser.py',33),
  ('tipo -> INTEGER','tipo',1,'p_tipo','parser.py',37),
  ('tipo -> REAL','tipo',1,'p_tipo','parser.py',38),
  ('tipo -> BOOLEAN','tipo',1,'p_tipo','parser.py',39),
  ('comando_composto -> BEGIN comando_list END','comando_composto',3,'p_comando_composto','parser.py',44),
  ('comando_list -> comando','comando_list',1,'p_comando_list','parser.py',48),
  ('comando_list -> comando_list SEMI comando','comando_list',3,'p_comando_list','parser.py',49),
  ('comando -> atribuicao','comando',1,'p_comando','parser.py',54),
  ('comando -> comando_composto','comando',1,'p_comando','parser.py',55),
  ('comando -> comando_condicional','comando',1,'p_comando','parser.py',56),
  ('comando -> comando_repetitivo','comando',1,'p_comando','parser.py',57),
  ('atribuicao -> ID ASSIGN expressao','atribuicao',3,'p_atribuicao','parser.py',62),
  ('comando_condicional -> IF expressao THEN comando','comando_condicional',4,'p_comando_condicional','parser.py',67),
  ('comando_condicional -> IF expressao THEN comando ELSE comando','comando_condicional',6,'p_comando_condicional','parser.py',68),
  ('comando_repetitivo -> WHILE expressao DO comando','comando_repetitivo',4,'p_comando_repetitivo','parser.py',73),
  ('expressao -> expressao_simples','expressao',1,'p_expressao','parser.py',78),
  ('expressao -> expressao_simples relacao expressao_simples','expressao',3,'p_expressao','parser.py',79),
  ('relacao -> EQ','relacao',1,'p_relacao','parser.py',83),
  ('relacao -> NE','relacao',1,'p_relacao','parser.py',84),
  ('relacao -> LT','relacao',1,'p_relacao','parser.py',85),
  ('relacao -> LE','relacao',1,'p_relacao','parser.py',86),
  ('relacao -> GT','relacao',1,'p_relacao','parser.py',87),
  ('relacao -> GE','relacao',1,'p_relacao','parser.py',88),
  ('expressao_simples -> termo','expressao_simples',1,'p_expressao_simples','parser.py',92),
  ('expressao_simples -> expressao_simples PLUS termo','expressao_simples',3,'p_expressao_simples','parser.py',93),
  ('expressao_simples -> expressao_simples MINUS termo','expressao_simples',3,'p_expressao_simples','parser.py',94),
  ('termo -> fator','termo',1,'p_termo','parser.py',98),
  ('termo -> termo TIMES fator','termo',3,'p_termo','parser.py',99),
  ('termo -> termo DIVIDE fator','termo',3,'p_termo','parser.py',100),
  ('fator -> ID','fator',1,'p_fator','parser.py',104),
  ('fator -> NUM_INT','fator',1,'p_fator','parser.py',105),
  ('fator -> NUM_REAL','fator',1,'p_fator','parser.py',106),
  ('fator -> LPAREN expressao RPAREN','fator',3,'p_fator','parser.py',107),
  ('empty -> <empty>','empty',0,'p_empty','parser.py',112),
]
