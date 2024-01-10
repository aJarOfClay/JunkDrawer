# extract a series of tar archives to a single destination folder

import tarfile
import os

source_folder = "path_to_source"
dest_folder = "path_to_destination"

list_of_archives = os.listdir(source_folder)
for archive in list_of_archives:
    archive_file_path = os.path.join(source_folder, archive)
    with tarfile.open(archive_file_path, 'r') as tar:
        tar.extractall(dest_folder)
