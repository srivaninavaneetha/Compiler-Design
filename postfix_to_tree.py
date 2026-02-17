class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def construct_tree(postfix):
    stack = []

    for char in postfix:
        if char.isalnum():
            stack.append(Node(char))
        else:
            node = Node(char)
            node.right = stack.pop()
            node.left = stack.pop()
            stack.append(node)

    return stack[-1]

def inorder(root):
    if root:
        inorder(root.left)
        print(root.value, end='')
        inorder(root.right)

postfix = input("Enter Postfix Expression: ")
root = construct_tree(postfix)

print("Inorder Traversal of Expression Tree:")
inorder(root)
from tree_to_tac import generate_tac

print("\nThree Address Code:")
generate_tac(root)
