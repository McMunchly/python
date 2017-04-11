#!/Library/Frameworks/Python.framework/Versions/3.5/bin/python3
# makes a folder structure

import os
import sys

if(len(sys.argv) > 1):

    dirname = sys.argv[1]

    if not os.path.exists(dirname):
        os.makedirs(dirname)
    else:
        print(dirname, "already exists")

else:
    print("filename must be provided")

