import os
import shutil
from datetime import datetime, timedelta

def make_backup(directories, extensions):
    """Creates a backup from given directories with given extensions.
    Args: 
        directories (list of strings): list of paths of directories,
        extensions (list of strings): list of file extensions.
    Returns: Creates a backup.
    Raises: AnyError: if anything bad happens.
    """
    today = datetime.now().strftime("%Y-%m-%d")
    backup_dir = os.path.join("Backup", f"copy-{today}")
    days_ago = datetime.now() - timedelta(days=3)

    if not os.path.exists(backup_dir):
        os.makedirs(backup_dir)
    
    for dir in directories:
        for dirpath, _, files in os.walk(dir):
            for file in files:
                for ext in extensions:
                    if os.path.splitext(file)[1] == ext:
                        file_path = os.path.join(dirpath, file)
                        mod_date = datetime.fromtimestamp(os.path.getmtime(file_path))
                        if mod_date > days_ago:
                            copy_name = f"copy-{file}"
                            copy_path = os.path.join(backup_dir, copy_name)
                            shutil.copy2(file_path, copy_path)