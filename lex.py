import re

class Token:
    def __init__(self, type, value):
        self.type = type
        self.value = value

def tokenize(code):
    token_specification = [
        ('NUMBER',   r'\d+'),
        ('PLUS',     r'\+'),
        ('MINUS',    r'-'),
        ('ID',       r'[A-Za-z]+'),
        ('SKIP',     r'[ \t]+'),
    ]
    
    tok_regex = '|'.join('(?P<%s>%s)' % pair for pair in token_specification)
    
    for mo in re.finditer(tok_regex, code):
        kind = mo.lastgroup
        value = mo.group()
        if kind != 'SKIP':
            yield Token(kind, value)

