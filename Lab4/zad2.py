string = "(()(())"
string1 = "(()(()))"
string3 = ")("

def is_closed(string):
    stack = []

    for i in string:
        if i == '(':
            stack.append(i)
        if i == ')':
            if not stack:
                return False
            stack.pop()

    return not stack

print(f"{string} -> {is_closed(string)}")
print(f"{string1} -> {is_closed(string1)}")
print(f"{string3} -> {is_closed(string3)}")
