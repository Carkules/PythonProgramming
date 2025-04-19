def check_brackets(chain):
    """Checks if brackets are correct in arithmetical operation.
    Args: chain(str): string with an operation to check.
    Returns: 
        True: when brackets are correct,
        False: when bracets are incorrect.
    Raises: AnyError: if anything bad happens."""
    opening_brackets = ['(', '[', '{']
    closing_brackets = [')', ']', '}']
    brackets_dict = {')': '(', ']': '[', '}': '{'}
    operations = ['+', '-', '*', '/']
    stack = []
    
    for i in range(len(chain)):
        if chain[i] in opening_brackets:
            stack.append(chain[i])
        elif chain[i] in closing_brackets:
            if stack == [] or brackets_dict[chain[i]] != stack.pop():
                print("Brackets are incorrect")
                return False
            k = 1
            while chain[i-k] == " ":
                k += 1
            if chain[i-k] in operations:
                print("Brackets are incorrect")
                return False
    if stack == []:
        print("Brackets are correct")
        return True
    else:
        print("Brackets are incorrect")
        return False

check_brackets('[(1+)+{5+[3]}]')