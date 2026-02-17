def optimize():
    print("Enter Three Address Code Statements (type 'end' to stop):")
    
    expressions = {}
    optimized = []

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
            
            expr = arg1 + op + arg2
            
            if expr in expressions:
                optimized.append(f"{result} = {expressions[expr]}")
            else:
                expressions[expr] = result
                optimized.append(stmt)
    
    print("\nOptimized Code:")
    for line in optimized:
        print(line)

optimize()
