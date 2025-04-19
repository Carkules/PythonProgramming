import random

def gen_password():
    """Generates random password 
    Args: None
    
    Returns: String containing random chain of symbols
    
    Raises: Any error: If anything bad happens."""

    password_ascii = []
    for i in range(8):
        password_ascii.append(random.randint(33, 126))      #generating password using ascii code
    password = ''.join(chr(i) for i in password_ascii)
    return password
print(gen_password())