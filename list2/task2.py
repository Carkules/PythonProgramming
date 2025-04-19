from PIL import Image

def create_miniature(filename, size, miniaturename):
    """Creates a minitaure of given picture.
    Args: 
        filename (str): name/path of given picture,
        size (int): size of the miniature,
        miniaturename (str): name of the miniature.
    
    Returns: creates a miniature.
    
    Raises: AnyError: if anything bad happens."""
    
    img = Image.open(filename)
    img.thumbnail((size, size))

    img.save(miniaturename+".jpg")
    img.show()
