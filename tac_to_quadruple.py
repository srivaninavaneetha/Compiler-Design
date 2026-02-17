def tac_to_quadruples():
    print("\nEnter Three Address Code Statements (type 'end' to stop):")

    quadruples = []

    while True:
        stmt = input()
        if stmt == 'end':
            break

        parts = stmt.split()

        if len(parts) == 5:
            result = parts[0]
            arg1 = parts[2]
            op = parts[3]
            arg2 = parts[4]

            quadruples.append([op, arg1, arg2, result])

    print("\nQuadruples:")
    print("Op\tArg1\tArg2\tResult")

    for q in quadruples:
        print(f"{q[0]}\t{q[1]}\t{q[2]}\t{q[3]}")

tac_to_quadruples()
