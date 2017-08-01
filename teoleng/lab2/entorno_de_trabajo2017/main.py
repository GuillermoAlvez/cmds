import nltk
import re
import sys


def split_in_terminals(text):
    return re.findall(r"(?:[^\s\.;=<>:\+\*\-\,\/\[\]\(\)]+|;|\.{1,2}|<>|<=|>=|:=|=|<|>|\*|\+|\-|\,|\/|\[|\]|\(|\)|:)", text, flags=re.I)


reserved_words = {
    "program": "PROGRAM",
    "begin": "BEGIN",
    "end": "END",
    "const": "CONST",
    "type": "TYPE",
    "var": "VAR",
    ".": "DOT",
    "..": "DOTDOT",
    ";": "SEMICOLON",
    ":": "COLON",
    ",": "COMMA",
    "=": "EQUAL",
    "<>": "DIFFERENT",
    "<": "LT",
    ">": "GT",
    "<=": "LTE",
    ">=": "GTE",
    ":=": "ASSIGN",
    "+": "ADD",
    "-": "SUB",
    "or": "OR",
    "*": "MUL",
    "/": "RDIV",
    "div": "DIV",
    "mod": "MOD",
    "and": "AND",
    "not": "NOT",
    "while": "WHILE",
    "do": "DO",
    "repeat": "REPEAT",
    "until": "UNTIL",
    "for": "FOR",
    "to": "TO",
    "downto": "DOWNTO",
    "if": "IF",
    "then": "THEN",
    "else": "ELSE",
    ")": "CPAR",
    "(": "OPAR",
    "]": "CSQRBRA",
    "[": "OSQRBRA",
    "array": "ARRAY",
    "of": "OF"
}


def map_to_terminal(terminal):
    lw_terminal = terminal.lower()
    if lw_terminal in reserved_words:
        return reserved_words[lw_terminal]
    elif re.match(r"\d+$", lw_terminal):
        return "NUMBER"
    else:
        return "IDENT"


def load_gramar():
    with open('grammar.txt', 'r') as f:
        return nltk.CFG.fromstring(f.read())


if __name__ == '__main__':
    archivo_entrada = sys.argv[1]
    archivo_salida = sys.argv[2]
    f = open(archivo_entrada, 'r')
    s = f.read()
    f.close()
    lista = [map_to_terminal(terminal) for terminal in split_in_terminals(s)]
    parser = nltk.ChartParser(load_gramar())
    reconoce = False;
    for tree in parser.parse(lista):
        reconoce = True;
    f = open(archivo_salida, 'w')
    if reconoce:
        f.write("PROGRAMA_CORRECTO")
    else:
        f.write("PROGRAMA_INCORRECTO")
    f.close()
