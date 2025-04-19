import zipfile
import os
import datetime

def zip_directory(folder_path):
    """Creates a zip archive of given folder.
    Args: 
        folder_path (str): path to the folder to zip.
    
    Returns: creates a zip archive.
    
    Raises: AnyError: if anything bad happens."""

    date = datetime.date.today()
    archive_name = str(date) + ' ' + folder_path +'.zip'
    ziparchive = zipfile.ZipFile(archive_name, 'w')

    for dirpath, dirnames, filenames in os.walk(folder_path):
        for filename in filenames:
            filepath = os.path.join(dirpath, filename)
            ziparchive.write(filepath)
    
    ziparchive.close()