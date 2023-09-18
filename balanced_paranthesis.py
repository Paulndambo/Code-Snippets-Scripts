def balanced(expression):
    # Create an empty stack to store opening parentheses
    stack = []

    # Define a dictionary to map closing parentheses to their corresponding opening parentheses
    parentheses_map = {')': '(', '}': '{', ']': '['}

    # Iterate through each character in the expression
    for char in expression:
        # If the character is an opening parenthesis, push it onto the stack
        if char in '({[':
            stack.append(char)
        # If the character is a closing parenthesis
        elif char in ')}]':
            # Check if the stack is empty or if the top of the stack matches the expected opening parenthesis
            if not stack or stack.pop() != parentheses_map[char]:
                return False

    # After processing all characters, the stack should be empty if the parentheses are balanced
    return not stack

# Test cases
print(balanced("(x+y)*(z-2*(6))"))  # True
print(balanced("7-(3(2*9))4) (1"))  # False
