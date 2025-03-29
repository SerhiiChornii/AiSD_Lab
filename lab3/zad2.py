string = "(()(()))"

def is_closed(string):
    stack = []

    for i in string:
        if i == '(':
            stack.append(i)
        if i == ')':
            if not stack:
                return False
            stack.pop()

    return len(stack) == 0

print(is_closed(string))
