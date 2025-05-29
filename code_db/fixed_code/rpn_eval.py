
def rpn_eval(tokens):
    def op(symbol, a, b):
        return {
            '+': lambda a, b: a + b,
            '-': lambda a, b: a - b,
            '*': lambda a, b: a * b,
            '/': lambda a, b: a / b
        }[symbol](a, b)

    stack = []
 
    for token in tokens:
        if isinstance(token, float):
            stack.append(token)
        else:
            # When popping from stack, 'a' is the most recent (second operand),
            # and 'b' is the one before that (first operand).
            a = stack.pop() # Second operand
            b = stack.pop() # First operand
            stack.append(
                op(token, b, a) # Apply operator as b op a
            )

    return stack.pop()
