#!/Library/Frameworks/Python.framework/Versions/3.5/bin/python3
# create a c boilerplate file

import sys
import glob

write = True

if len(sys.argv) == 1:
    print("You need to supply a filename")

else:
    for name in glob.glob(sys.argv[1] + ".c"):
        if len(sys.argv) < 3:
            print("filename already in use. File not created")
            write = False
        elif sys.argv[2] == "o":
            print(sys.argv[1], "was overwritten")

    if write == True:
        with open(sys.argv[1] + ".c", "w") as file:
            file.write("/*  */\n#include <stdio.h>\n\nint main(void)\n{\n    return 0;\n}")
