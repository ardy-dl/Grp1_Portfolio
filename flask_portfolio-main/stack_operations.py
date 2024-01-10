class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
        self.size = 0

    def push(self, data):
        new_node = Node(data)
        if self.top:
            new_node.next = self.top
        self.top = new_node
        self.size += 1

    def pop(self):
        if not self.is_empty():
            popped_node = self.top
            self.top = popped_node.next
            popped_node.next = None
            self.size -= 1
            return popped_node.data
        else:
            raise IndexError("pop from an empty stack")

    def peek(self):
        if not self.is_empty():
            return self.top.data
        else:
            raise IndexError("peek from an empty stack")

    def is_empty(self):
        return self.size == 0

def precedence(op):
    if op == '+' or op == '-':
        return 1
    elif op == '*' or op == '/':
        return 2
    return 0

def infixToPostfix(expression):
    ops = Stack()
    output = ''
    for char in expression:
        if char.isalpha():
            output += char
        elif char == '(':
            ops.push(char)
        elif char == ')':
            while not ops.is_empty() and ops.peek() != '(':
                output += ops.pop()
            ops.pop()
        else:
            while not ops.is_empty() and precedence(char) <= precedence(ops.peek()):
                output += ops.pop()
            ops.push(char)
    while not ops.is_empty():
        output += ops.pop()
    return output

'''# Example usage:
infix_expression = "A*(B+C)/D"
print(infixToPostfix(infix_expression))'''