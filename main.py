
def calculate(n1, n2, op):
    answer = 0

    if op == '+':
        answer = n1 + n2
    elif op == '-':
        answer = n1 - n2
    elif op == '*':
        answer = n1 * n2
    elif op == '**':
        answer = n1 ** n2
    elif op == '/':
        answer = n1 / n2
    else:
        raise ValueError("operator " + op + " unknown. Valid operators: + - / * **")

    return answer

def calculate_expr(floats, ops):
    res = floats[0]
    for p in range(0,len(ops)):
        res = calculate(res, floats[p+1], ops[p])
    return res

# parse expression to get floats
def get_floats_from_expression(expr_str):
    expression = expr_str.split(' ')
    floats = []
    for i in range(0, len(expression), 2):
        floats.append(float(expression[i]))

    return floats

# parse expression to get operators
def get_operators_from_expression(expr_str):
    expression = expr_str.split(' ')
    ops = []
    for g in range(1, len(expression), 2):
        ops.append(expression[g])
    return ops


if __name__ == '__main__':

    keep_running = 'Y'

    # get expression from user
    f = input("enter equation: ")
    floats = get_floats_from_expression(f)
    ops = get_operators_from_expression(f)
    print(calculate_expr(floats, ops))
