temp_count = 0

def generate_tac(node):
    global temp_count

    if node.left is None and node.right is None:
        return node.value

    left = generate_tac(node.left)
    right = generate_tac(node.right)

    temp = "t" + str(temp_count)
    temp_count += 1

    print(f"{temp} = {left} {node.value} {right}")

    return temp
