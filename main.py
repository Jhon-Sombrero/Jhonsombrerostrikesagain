

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



if __name__ == '__main__':

    keep_running = 'Y'
        
    while keep_running == 'Y':
        n1 = float(input("Enter number: "))
        n2 = float(input("Enter number: "))
        op = input("Operator: ")

        try:
            answer = calculate(n1, n2, op)
            print(answer)
        except ValueError:
            print("Operator " + op + " doesn't exist. Valid operators: + - * / **")


        keep_running = input('would you like to continue? (Y/N) ')


    
