import re

code = input("Enter Source Code: ")

tokens = re.findall(r'\w+|[=+;]', code)

for token in tokens:
    if token in ['int', 'float', 'char']:
        print("Keyword :", token)
    elif token.isdigit():
        print("Number :", token)
    elif token in ['=', '+']:
        print("Operator :", token)
    elif token == ';':
        print("Symbol :", token)
    else:
        print("Identifier :", token)

