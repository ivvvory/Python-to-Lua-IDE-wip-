##Python Lua compiler 
##half working tokenizer

import re

class LuaLexer:
    def __init__(self):
        self.token_specification = [
            ('NUMBER',    r'\b\d+(\.\d*)?\b'),     # Integer or decimal number
            ('STRING',    r'"([^"\\]|\\.)*"'),      # Double-quoted string
            ('ID',        r'[A-Za-z_][A-Za-z0-9_]*'),  # Identifier (variable or function name)
            ('KEYWORD',   r'\b(if|then|else|end|while|for|do|return|function|local)\b'),
            ('OPERATOR',  r'[\+\-\*/=<>!]'),        # Operators
            ('ASSIGN',     r'='),                    # Assignment
            ('LPAREN',    r'\('),                    # Left Parenthesis
            ('RPAREN',    r'\)'),                    # Right Parenthesis
            ('LBRACE',    r'\{'),                    # Left brace
            ('RBRACE',    r'\}'),                    # Right brace
            ('COMMA',     r','),                     # Comma
            ('SEMI',      r';'),                     # Semicolon
            ('WHITESPACE', r'\s+'),                  # Skip over whitespace
            ('MISMATCH',  r'.'),                     # Any other character
        ]
        self.regex = '|'.join(f'(?P<{pair[0]}>{pair[1]})' for pair in self.token_specification)
        self.re = re.compile(self.regex)

    def tokenize(self, code):
        line_num = 1
        line_start = 0
        for match in self.re.finditer(code):
            kind = match.lastgroup
            value = match.group()
            if kind == 'WHITESPACE':
                continue
            elif kind == 'MISMATCH':
                raise SyntaxError(f'Unexpected character: {value}')
            yield kind, value
