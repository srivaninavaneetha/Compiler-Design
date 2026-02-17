def generate_target_code():
    print("\nEnter Quadruples (Op Arg1 Arg2 Result) - type 'end' to stop:")

    while True:
        quad = input()

        if quad == 'end':
            break

        op, arg1, arg2, result = quad.split()

        print(f"MOV {arg1}, R1")

        if op == '+':
            print(f"ADD {arg2}, R1")
        elif op == '-':
            print(f"SUB {arg2}, R1")
        elif op == '*':
            print(f"MUL {arg2}, R1")
        elif op == '/':
            print(f"DIV {arg2}, R1")

        print(f"MOV R1, {result}")

generate_target_code()
