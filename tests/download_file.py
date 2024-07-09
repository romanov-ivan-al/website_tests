import os
import getpass


def get_size_download_file():
    username = getpass.getuser()
    path_to_file =f"/Users/{username}/Downloads/sbisplugin-setup-web.exe"
    file_size_bytes = os.path.getsize(path_to_file)
    file_size_mb = round(file_size_bytes / (1024*1024), 2)
    os.remove(path_to_file)
    return str(file_size_mb)


