
def addition(numbers):
    """Creates addition bar.
    Args: numbers (list): list of numbers to add,
    
    Results: Prints the addition bar.
    
    Raises: AnyError: if anything bad happens."""

    result = 0
    lens = []
    for i in numbers:
        result += int(i)
        lens.append(len(i))
    lens.append(len(str(result)))
    maxlen = max(lens)
    for i in range(len(numbers)-1):
        space = " " * (maxlen - len(numbers[i]) +1)
        print(space + numbers[i])
    space = " " * (maxlen - len(numbers[len(numbers)-1]))
    print("+"+space+numbers[len(numbers)-1])
    
    print("-"*(maxlen+1))
    space = " "*(maxlen+1 - len(str(result)))
    print(space + str(result))

def substraction(numbers):
    """Creates substraction bar.
    Args: numbers (list): 2 element list of numbers to substract,
    
    Results: Prints the substraction bar.
    
    Raises: AnyError: if anything bad happens."""

    sa = numbers[0]
    sb = numbers[1]
    a = int(sa)
    b = int(sb)
    maxlen = max(len(sa), len(sb))
    space = " " * abs(len(sa) - len(sb))
    if len(sa) > len(sb):
        print(" " + sa)
        print("-" + space + sb)
    else:
        print(" " + space + sa)
        print("-" + sb)
    
    print("-"*(maxlen+1))
    
    result = str(a - b)
    space = (maxlen+1)-len(result)
    print(" "*space + result)

def multiplying(numbers):
    """Creates multiplication bar.
    Args: numbers (list): list of numbers to multiply,
    
    Results: Prints the multiplication bar.
    
    Raises: AnyError: if anything bad happens."""

    sa = numbers[0]
    sb = numbers[1]
    a = int(sa)
    b = int(sb)
    result = str(a * b)
    maxlen = len(result) +1
    spacea = " " * (maxlen - len(sa))
    spaceb = " " * (maxlen - len(sb) - 1)
    print(spacea + sa)
    print("*"+ spaceb + sb)
    print("-"*maxlen)
    if len(sb) == 1:    
        print(" "+result)
    else:
        adnumbers = []
        for i in range(len(sb)):
            element = a*int(sb[i])*(10**(len(sb)-1-i))
            adnumbers.append(str(element))
        adnumbers.reverse()
        addition(adnumbers)

def operation(op):
    """Checks which operation to use.
    Args: op (str): string with operation.
    
    Returns: calls a funcion with right operation.
    
    Raises: AnyError: if anything bad happens."""
    
    if "+" in op:
        numbers = op.split("+")
        addition(numbers)
    elif "-" in op:
        numbers = op.split("-")
        if len(numbers) == 2:
            substraction(numbers)
        else:
            print("Wrong ammount of numbers")
    elif "*" in op:
        numbers = op.split("*")
        if len(numbers) == 2:
            multiplying(numbers)
        else:
            print("Wrong ammount of numbers")
    else:
        print("Unknown operation")

operation("99+2322")