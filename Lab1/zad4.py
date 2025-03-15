def czy_palindrom(string):
    if len(string) <= 1:
        return True
    if string[0] == string[-1]:
        return czy_palindrom(string[1:-1])
    return False


print(czy_palindrom('dadad'))
