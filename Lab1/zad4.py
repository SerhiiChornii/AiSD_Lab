def czy_palindrom(string):
    string = string.lower().strip()
    if len(string) <= 1:
        return True
    if string[0] == string[-1]:
        return czy_palindrom(string[1:-1])
    return False


test1 = "Anna"
test2 = "kajak"
test3 = "Serhii "
print(f"Input: {test1} | Output: {czy_palindrom(test1)}")
print(f"Input: {test2} | Output: {czy_palindrom(test2)}")
print(f"Input: {test3} | Output: {czy_palindrom(test3)}")
