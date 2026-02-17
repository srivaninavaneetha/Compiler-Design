def parse(expr):
    stack = []
    operators = ['+', '-', '*', '/']

    for ch in expr:
        if ch.isalnum():
            stack.append(ch)
        elif ch in operators:
            if len(stack) < 2:
                print("Syntax Error")
                return
            stack.pop()
            stack.pop()
            stack.append('E')

    if len(stack) == 1:
        print("Syntax is Correct")
    else:
        print("Syntax Error")

exp = input("Enter Expression: ")
parse(exp)
