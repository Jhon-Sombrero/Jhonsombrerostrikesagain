

def calculate(n1, n2, op):
    answer = 0
    success = True
        
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
        success = False

    return (success, answer)



if __name__ == '__main__':

    keep_running = 'Y'
        
    while keep_running == 'Y':
        n1 = float(input("Enter number: "))
        n2 = float(input("Enter number: "))
        op = input("Operator: ")

        (success, answer) = calculate(n1, n2, op)
        
        if success:
            print (answer)
        else:
            print('operator ' + op + ' unknown, try again')

            
        keep_running = input('would you like to continue? (Y/N) ')
    

    
