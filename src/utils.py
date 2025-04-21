import random
import os
import shutil

def random_str(len):
    return ''.join([chr(random.randint(ord('A'), ord('Z'))) for i in range(len)])

# https://stackoverflow.com/questions/3167154/how-to-split-a-dos-path-into-its-components-in-python
def split_path(path):
    return os.path.normpath(path).split(os.sep)

def recursive_mkdir(path):
    folders = split_path(path)
    abs_path = ''

    for p in folders:
        abs_path = os.path.join(abs_path, p)
        if not os.path.exists(abs_path):
            os.mkdir(abs_path)

def vider_dossier(dossier):
    shutil.rmtree(dossier)