from PyPDF2 import PdfMerger

def merge_pdfs(pdfs, result_name):
    """Merges given pdfs to the pdf with given name.
    Args:
        pdfs(list of strings): list with names/paths to the pdfs to merge,
        result_name(str): name of the pdf file after merge.
    Returns: Creates merged pdf file.
    Raises: AnyError: if anything bad happens."""
    merger = PdfMerger()
    for pdf in pdfs:
        merger.append(pdf)
    merger.write(result_name)
    merger.close()