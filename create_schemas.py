"""
This script creates schema documents of Common Data Model (CDM) for the Orange Juice dataset. 
"""

import os
import shutil


def copytree(src, dst, symlinks=False, ignore=None):
    for item in os.listdir(src):
        s = os.path.join(src, item)
        d = os.path.join(dst, item)
        if os.path.isdir(s):
            shutil.copytree(s, d, symlinks, ignore)
        else:
            shutil.copy2(s, d)

if __name__ == "__main__":
    src = os.path.join(".", "CDM", "schemaDocuments")
    des = os.path.join(".", "schemaDocuments")
    copytree(src, des)