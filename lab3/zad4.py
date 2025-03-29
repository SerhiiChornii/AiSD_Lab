def eval_rpn(expression: str):
    expression = expression.split()
    stos = []

    for i in expression:
        if i == '=':
            return stos.pop()
        elif i.isnumeric():
            stos.append(i)
        else:
            if i == '^': 
                symbol = '**'
            else: symbol = i
            v2 = stos.pop()
            v1 = stos.pop()

            stos.append(str(eval(f"{v1} {symbol} {v2}")))

print(eval_rpn(" 5 6 + 4 - 3 * ="))
print(eval_rpn("10 5 - 3 ^ 7 + ="))
print(eval_rpn("9 3 1 - * ="))
print(eval_rpn("6 2 + 4 / ="))

