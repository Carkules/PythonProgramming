import PyPDF2
import os

def pdf_split(path, split_pages):
    """
    Splits given pdf file to smaller parts.
    Args:
        path (str): path to the pdf file,
        split_pages (list): list of numbers of pages on which given pdf will be split.
    
    Returns: Creates splitted pdf files.

    Raises: 
        ValueError: if number of pages is invalid,
        AnyError: if anything bad happens.
    """
    base_name = os.path.splitext(os.path.basename(path))[0]

    pdf = PyPDF2.PdfReader(path)
    pages = len(pdf.pages)
    if sum(split_pages) > pages:
        raise ValueError("Wrong number of pages")
    k = 0
    p = 0
    for i in range(len(split_pages)):
        pdf_writer = PyPDF2.PdfWriter()
        for j in range(k, k+split_pages[i]):
            pdf_writer.add_page(pdf.pages[j])
            p += 1
        
        output_filename = '{}{}.pdf'.format(base_name, i+1)
        with open(output_filename, 'wb') as out:
            pdf_writer.write(out)
        k = p