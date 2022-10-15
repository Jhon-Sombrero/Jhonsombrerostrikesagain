

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



def assertEqual(actual, expected, error_message):
    if actual != expected:
        print(error_message)
        return False

    return True
    



def test_calculate_can_add_floats():
    (success, answer) = calculate(1.2, 4.5, '+')

    test_passed = assertEqual(success, True, "test_calculate_can_add_floats failed: success = False")
    if test_passed:
        test_passed = assertEqual(answer, 5.7, "test_calculate_can_add_floats failed: answer = " + str(answer))

    return test_passed
    


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
    

    