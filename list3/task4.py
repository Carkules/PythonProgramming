import qrcode
import cv2

def make_qrcode(link, qr_name):
    """Creates a qrcode from a given string and saves it with given name in png format.
    Args:
        link(str): string to make qrcode with it,
        qr_name(str): name of the image with qrcode.
    Returns: Makes a image with qrcode.
    Raises: AnyError: if anything bad happens."""

    qr_img = qrcode.make(link)
    qr_img.save(qr_name + '.png')

def read_qrcode(qr_img):
    """Detects and reads a qrcode from a given image.
    Args: qr_img(str): name/path to the given image with qrcode.
    Returns: data(str): string with data read from qrcode.
    Raises: AnyError: if anything bad happens."""
    
    image = cv2.imread(qr_img)
    detector = cv2.QRCodeDetector()
    data, _, _ =  detector.detectAndDecode(image)
    return data