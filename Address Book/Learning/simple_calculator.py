def user_prompt():
    x = float(input("What is x? "))
    y = float(input("what is y? "))
    return x, y

def arithmetic_operations():
    print("Please select an arithmetic operation:")
    print("1: add (+)")
    print("2: Sub (-)")
    print("3: Mult (*)")
    print("4: Div (/)")
    
    choice = input("Enter your choice (1/2/3/4) ")
    valid_choices = ['1', '2','3', '4']
    if choice not in valid_choices:
        print("Invalid choice")
        choice = input("Enter your choice (1/2/3/4) ")
        
    x, y = user_prompt()
    
    if choice == '1':
        result = x + y
        print("Result: ", result)
    elif choice == '2':
        result = x - y
        print("Result: ", result)
    elif choice == '3':
        result = x * y
        print("Result: ", result)
    elif choice == '4':
        try:
            if y != 0:
                result = float(x / y)
                print("Result: ", result)
        except ZeroDivisionError:
            print("Invalid division")
        except TypeError:
            pass
    else:
        print("Invalid choice,:\n[+, -, *,/]")
arithmetic_operations()