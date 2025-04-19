def unix_to_windows(file_path):
    """Changes unix signs at the end of the lines to windows signs.
    Args: file_path(str): string with path to the txt file.
    Returns: Changes the signs from unix to windows in a given file.
    Raises: AnyError: if anything bad happens."""

    with open(file_path, 'rb') as file:
        text = file.read()
    text = text.replace(b'\n', b'\r\n')
    with open(file_path, 'wb') as file:
        file.write(text)

def windows_to_unix(file_path):
    """Changes windows signs at the end of the lines to unix signs.
    Args: file_path(str): string with path to the txt file.
    Returns: Changes the signs from windows to unix in a given file.
    Raises: AnyError: if anything bad happens."""

    with open(file_path, 'rb') as file:
        text = file.read()
    text = text.replace(b'\r\n', b'\n')
    with open(file_path, 'wb') as file:
        file.write(text)

def detect_unix_or_windows(file_path):
    """Detects if signs at the end of the lines are unix or windows and changes them to the other ones.
    Args: file_path(str): string with path to the txt file.
    Returns: Changes the signs at the end of the lines.
    Raises: AnyError: if anything bad happens."""
    
    with open(file_path, 'rb') as file:
        text = file.read()
        if b'\r\n' in text:
            windows_to_unix(file_path)
        else:
            unix_to_windows(file_path)