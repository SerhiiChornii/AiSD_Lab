def czy_palindrom(string):
    if len(string) <= 1:
        return True
    if string[0] != string[-1]:
        return False
    return czy_palindrom(string[1:-1])

print(czy_palindrom('addad'))